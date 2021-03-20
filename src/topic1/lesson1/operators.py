if __name__ == '__main__':
    print("operators")
    """
    Arithmetic Operators, Assignment Operators, Comparison Operators, 
    """

    # Addition
    a = 5
    b = 2
    print("Addition a + b = ", a + b)
    # Subtraction
    print("Subtraction 5 - 2 = ", 5 - 2)
    # Multiplication
    print("Multiplication 5 * 2 = ", 5 * 2)
    # Division
    print("Division 5 / 2 = ", 5 / 2)

    # Exponent "This is the same as 5 * 5"
    print("Exponent 5 ** 2 = ", 5 ** 2)
    # Floor Division
    print("Floor Division 5 // 2 = ", 5 // 2)
    # Modulus
    print("Modulus 5 % 2 = ", 5 % 2)

    # Assignment Operators +=, -=, /=, *=, **=, //=, %=
    balance = 100
    print("balance = ", balance)
    balance += 10
    print("balance = ", balance)
    balance -= 60
    print("balance = ", balance)

    # Comparison Operators
    print("Comparison Operators")
    a = 1
    b = 50

    print("a == b ", a == b)  # Equal
    print("a != b ", a != b)  # Not equal
    print("a > b ", a > b)  # Greater than
    print("a < b ", a < b)  # Less than
    print("a >= b ", a >= b)  # Greater than or equal to
    print("a <= b ", a <= b)  # Less than or equal to
    print("'Hello' == 'World' - ", 'Hello' == 'World')
    print("'Python' != 'R' - ", "Python" != "R")

    # Logical Operators 'or', 'and', 'not'
    print("Logical Operators 'or', 'and', 'not' ")
    print(True and True and True and True)
    print(True and True and True and False)
    print(False or False or True or False)
    print(False or False or False or True)
    print(not False or True)


def operators_task1():
    a = 0
    return a


def operators_task2():
    return True and True and False


def operators_task3():
    a = 10
    b = 5
    return a < b
