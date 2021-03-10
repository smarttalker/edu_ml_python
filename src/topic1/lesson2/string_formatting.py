if __name__ == '__main__':
    """
    The "%" operator is used to format a set of variables enclosed in a "tuple"
    Any object which is not a string can be formatted using the %s operator as well
    
    %s - String (or any object with a string representation, like numbers)
    %d - Integers
    %f - Floating point numbers
    %x/%X - Integers in hex representation (lowercase/uppercase
    
    """
    name = "John"
    print("Hello, %s!" % name)

    name = "Oleg"
    age = 23
    print("%s is %d years old." % (name, age))

    mylist = [1, 2, 3]
    print("A list: %s" % mylist)


def string_formatting_task1():
    """
    You will need to write a format string which prints out the data using the following syntax:
    Hello John Doe. Your current balance is $53.44.
    """
    data = ("John", "Doe", 53.44)
    format_string = "Hello"
    # TODO write the code
    res = "%s %s %s. Your current balance is $%s" % (format_string, data[0], data[1], data[2])
    print(res)
    return res
