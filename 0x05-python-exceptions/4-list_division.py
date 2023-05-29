#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    n = 0
    for n in range(list_length):
        result = 0
        try:
            result = my_list_1[n]/my_list_2[n]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
