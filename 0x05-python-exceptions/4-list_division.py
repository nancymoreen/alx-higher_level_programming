#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        element_1 = my_list_1[i]
        element_2 = my_list_2[i]
        division_result = element_1 / element_2
        result.append(division_result)
        except ZeroDivisionError:
            print("Division by zero")
            return.append(0)
        except (TypeError, ValueError):
            print ("Incorrect type")
            result.append(0)
        except IndexError:
            print("Not in range")
        finally:
            return result[:list_length]
