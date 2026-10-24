import argparse


parser = argparse.ArgumentParser(description="Greet someone.")
parser.add_argument("name", help="Name of the person to greet")
parser.add_argument("--shout", action="store_true", help="Shout the greeting")

args = parser.parse_args()

greeting = f"Hello, {args.name}!"
if args.shout:
    greeting = greeting.upper()

print(greeting)
