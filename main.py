#!/usr/bin/python3

# list = [1, 2, 3, 4, 5]
# list = [6, 7, 8, 9, 10]
# list = [11, 12, 13, 14, 15]

def create_number_list(n):
    number_list = []

    for i in range(1, n + 1):
        number_list.append(i)

    return number_list

def create_filled_list(value, size):
    copy_list = []

    for i in range(1, size + 1):
        copy_list.append(value)

    return copy_list

def double_list_values(numbers):
    doubled_list = []
    
    for num in numbers:
        doubled_list.append(num * 2)

    return doubled_list

def add_to_end(items, new_item):
    items.append(new_item)

    return items

def add_to_start(items, new_item):
    items.insert(0, new_item)

    return items



## create_number_list TESTS
# test1 = create_number_list(5)
# test2 = create_number_list(9)
# test3 = create_number_list(12)

## create_filled_list TESTS
# test1 = create_filled_list("x", 5)
# test2 = create_filled_list("*", 9)
# test3 = create_filled_list(".", 12)

## double_list_values TESTS
# test1 = double_list_values(list)

## add_to_end TESTS
# test1 = add_to_end(list, "test, test")

## add_to_start TESTS
# test1 = add_to_start(list, "test, test")



# print(test1)
# print(test2)
# print(test3)