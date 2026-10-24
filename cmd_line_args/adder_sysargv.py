import sys


# Check if enough arguments are provided
if len(sys.argv) < 3:
    print("Usage: python adder_sysargv.py <num1> <num2>")
    sys.exit(1)

# Extract arguments (skip sys.argv[0] which is the script name)
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# Perform addition
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")
