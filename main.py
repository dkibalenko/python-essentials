from __future__ import annotations

import asyncio
import functools
import inspect
import logging
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, TypeVar

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout


logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


# -------------- Retry -------------------------------------


def retry(
    max_attempts:   int                  = 3,
    exceptions:     tuple[type, ...]     = (Exception,),
    backoff_factor: float                = 2.0,
) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                delay = 1.0
                for attempt in range(1, max_attempts + 1):
                    try:
                        logger.debug("[%s] Attempt %d/%d", func.__name__, attempt, max_attempts)
                        result = await func(*args, **kwargs)
                        logger.debug("[%s] Success on attempt %d", func.__name__, attempt)
                        return result
                    except exceptions as e:
                        logger.warning(
                            "[%s] Attempt %d caught: %s: %s",
                            func.__name__, attempt, type(e).__name__, e,
                        )
                        if attempt == max_attempts:
                            logger.error("[%s] All %d attempts failed", func.__name__, max_attempts)
                            raise
                        logger.info("Retrying in %.1fs...", delay)
                        await asyncio.sleep(delay)
                        delay *= backoff_factor
            return async_wrapper  # type: ignore[return-value]

        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug("[%s] Attempt %d/%d", func.__name__, attempt, max_attempts)
                    result = func(*args, **kwargs)
                    logger.debug("[%s] Success on attempt %d", func.__name__, attempt)
                    return result
                except exceptions as e:
                    logger.warning(
                        "[%s] Attempt %d caught: %s: %s",
                        func.__name__, attempt, type(e).__name__, e,
                    )
                    if attempt == max_attempts:
                        logger.error("[%s] All %d attempts failed", func.__name__, max_attempts)
                        raise
                    logger.info("Retrying in %.1fs...", delay)
                    time.sleep(delay)
                    delay *= backoff_factor
        return sync_wrapper  # type: ignore[return-value]
    return decorator  # type: ignore[return-value]


@retry(max_attempts=3, exceptions=(HTTPError, Timeout, ConnectionError))
def fetch_success():
    response = requests.get("https://httpbin.org/get", timeout=5)
    response.raise_for_status()
    return response.json()


# -------------- RBAC -----------------------------


class PermissionError(Exception):
    pass


def require_role(*allowed_roles: str):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            user = kwargs.get("user") or (args[0] if args else None)

            if not user:
                raise PermissionError("Authentication required.")

            if user.role not in allowed_roles:
                raise PermissionError(
                    f"Role '{user.role}' not authorized. "
                    f"Required: {allowed_roles}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@dataclass
class User:
    name: str
    role: str


@require_role("admin")
def delete_post(user: User, post_id: int):
    print(f"{user.name} delete post {post_id}")


alice = User(name = "Alice", role = "admin")
bob   = User(name = "Bob", role = "viewer")

# delete_post(user = alice, post_id = 1)
delete_post(user = bob, post_id = 2)
