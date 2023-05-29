#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for n in my_list[:x]:
            try:
                print(":{d}".format(n), end=' ')
                count += 1
            except ValueError:
                pass
            except TypeError:
                raise
            finally:
                print()
                return count
