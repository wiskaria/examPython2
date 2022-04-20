
list = [1, 2, 3, 4, 5, 1]


def get_indexes(my_list, value_to_get):
    for i, e in enumerate(my_list):
        if e == value_to_get:
            print(i, end="")


get_indexes(list, 1)
pass
