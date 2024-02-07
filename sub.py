import sys
import subprocess

my_input = sys.argv


def sum_two_values(a=int(my_input[1]), b=int(my_input[2])):
    return a + b


if __name__ == "__main__":
    result = subprocess.run(
        ["MYCODES';", "fileOp.py", "2", "4"], capture_output=True, text=True
    )
    print("Result:", result.stdout)
    print("Sum of two values:", sum_two_values())