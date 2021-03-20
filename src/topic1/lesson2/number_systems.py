if __name__ == '__main__':
    print("number systems")

    """
    Number systems - Binary, Octal, and Hexadecimal Integers in Python  
    """

    '''
    Binary:
    Binary integers are the number represented with base two. 
    Which means in the binary number system, there are only two symbols used to represent numbers: 0 and 1.

    HOWTO:
    Representation number - '5' in decimal system, in the binary - '101'
    Convert binary '101' to the decimal - (1 * (2^2)) + (0 * (2^1)) + (1 * (2^0)) = 5
    
    1    0   1
    -----------
    2^2 2^1 2^0
    ============
     4   2   1
    +++++++++++ 
     4 + 0 + 1
    '''
    print(int("101101"))

    binary_number_string = "101"
    print("Binary - %s, to decimal = %d " % (binary_number_string, int(binary_number_string, base=2)))

    '''
    Octal:
    Octal is base eight, which means that eight symbols are used to represent all the quantities.
    They are 0, 1, 2, 3, 4, 5, 6 and 7. After 7 is 10, since 8 doesn't exist.

    HOWTO:
    Just like you used powers of two in binary to determine the value of a number,you will use powers of 8.
    Octal Number = 117
    Decimal value = (1*(8^2)) + (1*(8^1)) + (7*(8^0)) = 79
    '''
    octal_number_string = "117"
    print("Octal - %s, to decimal = %d " % (octal_number_string, int(octal_number_string, base=8)))

    '''
        Hexadecimal:
        Hexadecimal is a base 16 number system. Unlike binary and octal, hexadecimal has six additional symbols 
        that it used beyond the numbers found in the decimal number system.
        So in hexadecimal, the total list of symbols used is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F.

        HOWTO:
        Hexadecimal Number = 4F 
        Decimal value = (4*(16^1)) + (F*(16^0)) = 79
        '''
    hexadecimal_number_string = "4F"
    print("Hexadecimal - %s, to decimal = %d " % (hexadecimal_number_string, int(hexadecimal_number_string, base=16)))

    print("lesson 2")

    a, b = 3, 4
    print(a, b)


def variables_task1():
    """
    The 'my_string' should contain string 'hello', my_float - 11.025, my_int - 7.
    """
    "my_string, my_float, my_int = None, None, None"

    my_string = "string"
    my_float = 11
    my_int = 123

    # TODO write the code
    return my_string, my_float, my_int
