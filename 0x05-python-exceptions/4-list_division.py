#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_result = []
    for i in range(list_length):
        try:
           result = (my_list_1[i] / my_list_2[i])
        except TypeError:
            result = 0
            print('wrong type')
            continue
        except IndexError:
            result = 0
            return my_result
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        finally:
            my_result.append(result)

    return my_result
