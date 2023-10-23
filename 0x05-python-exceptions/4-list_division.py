#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_result = []
    for i in range(list_length):
        try:
            my_result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            my_result.append(0)
            print('wrong type')
            continue
        except IndexError:
            print('out of range')
            my_result.append(0)
            return my_result
        except ZeroDivisionError:
            my_result.append(0)
            print('division by 0')
            continue

    return my_result
