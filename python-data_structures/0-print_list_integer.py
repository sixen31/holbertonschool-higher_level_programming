#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        print('\n'.join("{:d}".format(num) for num in my_list))

    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
