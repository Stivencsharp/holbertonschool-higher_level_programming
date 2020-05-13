#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
num_args = len(sys.argv)
if num_args != 4:
    print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
    exit(1)
num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
sign = sys.argv[2]
if sign == '+':
    print("{:d} {:s} {:d} = {:d}".format(num1, sign, num2, add(num1, num2)))
elif sign == '-':
    print("{:d} {:s} {:d} = {:d}".format(num1, sign, num2, sub(num1, num2)))
elif sign == '*':
    print("{:d} {:s} {:d} = {:d}".format(num1, sign, num2, mul(num1, num2)))
elif sign == '/':
    print("{:d} {:s} {:d} = {:d}".format(num1, sign, num2, div(num1, num2)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
