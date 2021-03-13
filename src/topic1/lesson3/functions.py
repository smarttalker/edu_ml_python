"""
 Functions are a convenient way to divide your code into useful blocks,
 allowing us to order our code, make it more readable, reuse it and save some time.
 Also functions are a key way to define interfaces so programmers can share their code.
"""


def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    '''
    Functions may return a value to the caller, using the keyword- 'return' . For example:
    '''
    return a + b


if __name__ == '__main__':
    my_function()
    my_function_with_args("Student", "good luck")


def function_task1():
    """
    Modify this function to return a list of strings
    """
    # TODO write the code

    return list([1, 2, 3, 4, 5, 6])


def function_task2(list1, list2):
    """
    Modify this function to return concatenated lists
    """
    # TODO write the code
    ##[1, 2, 3], [1, 2, 3]
    return list1 + list2
