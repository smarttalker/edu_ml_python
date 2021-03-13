if __name__ == '__main__':
    """
    There are two types of loops in Python, for and while.
    """
    # For loops iterate over a given sequence.
    list_numbers = [2, 4, 6, 8]
    for number in list_numbers:
        print(number)

    # For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
    for n in range(5):
        print("range(5)", n)

    for n in range(3, 5):
        print("range(3, 5)", n)

    # "while" loops
    count = 0
    while count < 5:
        print("while loop ", count)
        count += 1  # This is the same as count = count + 1

    # "break" and "continue" statements
    '''
    break is used to exit a for loop or a while loop,
    Whereas continue is used to skip the current block, and return to the "for" or "while" statement.
    '''
    count = 0
    while True:
        print("count True - ", count)
        if count >= 5: break
        count += 1

    # Unlike languages like C,CPP.. we can use else for loops. When the loop condition of "for" or "while"
    count = 0
    while (count < 5):
        print("count - ", count)
        count += 1
    else:
        print("count value reached %d" % (count))


def loops_task1():
    """
    Use loop for creation list with 500 integer elements
    """
    task_list = []
    count = 0
    while (count < 500):
        task_list.append(count)
        count += 1
    # TODO write the code
    return task_list


