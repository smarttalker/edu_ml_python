"""
 Functions are a convenient way to divide your code into useful blocks,
 allowing us to order our code, make it more readable, reuse it and save some time.
 Also functions are a key way to define interfaces so programmers can share their code.
"""
from functools import reduce


def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    '''
    Functions may return a value to the caller, using the keyword- 'return' . For example:
    '''
    res = a + b
    return res


lambda_multiply_2 = lambda x: x * 2
lambda_sqrt_2 = lambda x: x ** 2

if __name__ == '__main__':
    print(lambda_multiply_2(5))
    print(lambda_sqrt_2(5))

    my_pets = ['alfred', 'tabitha', 'william', 'arla', "test"]
    for i in my_pets:
        print(i.upper())

    # HOF High order function
    # map
    # map(func, *iterables) --> map object
    res = list(map(str.upper, my_pets))
    print(res)

    # map with lambda example
    list_number = [1, 2, 3, 4]
    res = map(lambda x: x ** 2, list_number)
    print(list(res))

    # zip example
    list_number = [1, 2, 3, 4]
    list_words = ["one", "qwer", "ett", "rttr"]
    res_zip = list(zip(list_number, list_words))
    print(res_zip)

    # filter example

    my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, 100]
    my_list_str = ["geeks", "geeg", "keegs", "practice", "to", "hi", "apple", "amazon"]
    print("filter 1", list(filter(lambda x: x[0] == 'a', my_list_str)))
    print("filter 2", list(filter(lambda x: x % 2 == 0, my_list)))

    # reduce example
    list_reduce = [1, 2, 3, 4]

    # reduce example
    print("Reduce implementation", reduce(lambda x, y: x + y, list_reduce))
    # TODO
    #filter()
    #reduce()


def function_task1():
    """
    Modify this function to return a list of strings
    """
    # TODO write the code
    return list()


def function_task2(list1, list2):
    """
    Modify this function to return concatenated lists
    """
    # TODO write the code
    return None
