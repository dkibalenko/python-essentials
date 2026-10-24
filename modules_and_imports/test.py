# import demo_packages.lifecycle_demo.once as once_mod


# print()
# print(f'__name__    = {once_mod.__name__!r}')
# print(f'__file__    = {once_mod.__file__!r}')
# print(f'__package__ = {once_mod.__package__!r}')

# import sys

# print([p for p in sys.path])

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
    force=True,
)

logger = logging.getLogger(__name__)

# logger.debug("starting up — DEBUG visible because level=DEBUG")
# logger.info("user logged in — user_id=42")
# logger.warning("rate limit at 85% for ip=1.2.3.4")
# logger.error("payment service unreachable — order_id=101")
# logger.critical("database connection pool exhausted — all 20 connections in use")

root = logging.getLogger()
print(logger.name)
print(root)
print(logger.parent is root)
