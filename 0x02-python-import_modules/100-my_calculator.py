#!/usr/bin/python3
import calculator_1 as ca
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if not(n == 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, ca.add(a, b)))
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, ca.sub(a, b)))
        elif op == "*":
            print("{} {] {} = {}".format(a, op, b, ca.mul(a, b)))
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, ca.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
