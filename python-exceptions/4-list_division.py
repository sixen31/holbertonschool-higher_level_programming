#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division par zéro")
            result = 0
        except IndexError:
            print("indice hors limite")
            result = 0
        except (TypeError, ValueError):
            print("mauvais type")
            result = 0
        finally:
            result_list.append(result)
    return result_list