#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for n in my_list[:x]:
            print(n, end=' ')
            count += 1
    except TypeError as e:
        print("Error:", e)
    finally:
        print()
        return count
