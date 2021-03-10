if __name__ == '__main__':
    """
    Strings are bits of text. They can be defined as anything between quotes.
    """
    astring = "Hello world!"
    print("single quotes are ' '")
    print("len of '" + astring + "' - %d" % len(astring))

    # That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
    print("index of 'o' - %d" % astring.index("o"))

    print("Occurrence latter in the string - %d" % astring.count("l"))
    # Reverse a string with slicing
    print(astring[::-1])

    # Check string starting and ending with
    print(astring.startswith("Hello"))
    print(astring.endswith("world!"))

    # Slit string by specific character
    print(astring.split(" "))


def string_operations_task1():
    """
    Split string by the empty space and return LIST
    """
    quote = "I am the wisest man alive, for I know one thing, and that is that I know nothing."
    # TODO write the code
    return quote.split(" ")


def string_operations_task2():
    """
    Return in the upper case
    """
    word = "wisest"
    # TODO write the code
    return word.upper()


def string_operations_task3():
    """
    Reverse tne string
    """
    word = "wisest"[::-1]
    # TODO write the code
    return word
