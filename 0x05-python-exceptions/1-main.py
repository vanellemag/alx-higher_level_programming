#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer
value = 89
has = safe_print_integer(value)
if not has:
    print("{} is mot am integer".format(value))
value = - 89
has = safe_print_integer(value)
if not has:
    print("{} is not an integer".format(value))
value = "School"
has = safe_print_integer(value)
if not has:
    print("{} is not an integer".format(value))
