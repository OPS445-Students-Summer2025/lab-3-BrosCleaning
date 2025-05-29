#!/usr/bin/env python3

# Declare the global list before any function
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all items unchanged
    return my_list

def give_first_item():
    # Returns the first item as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list with first and last items
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list with second and third items
    return my_list[1:3]


if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
