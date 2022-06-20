#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    finally:
        if res:
            print("Inside result: {}".format(res))
        else:
            print("Inside result: None")
    return res
