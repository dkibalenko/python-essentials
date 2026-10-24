import argparse


# Create parser object
parser = argparse.ArgumentParser(description="Add two numbers.")

# Define arguments
parser.add_argument("num1", type=float, help="First number to add")
parser.add_argument("num2", type=float, help="Second number to add")

# Parse arguments
args = parser.parse_args()

# Perform addition
result = args.num1 + args.num2
print(f"The sum of {args.num1} and {args.num2} is {result}")
