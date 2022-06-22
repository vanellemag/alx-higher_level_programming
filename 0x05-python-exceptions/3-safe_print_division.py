#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError or TypeError:
        raise ZeroDivisionError('Division by zero!')
    finally:
        if res:
            print("Inside result: {}".format(res))
            return res
        else:
            print("Inside result: None")
            return None
