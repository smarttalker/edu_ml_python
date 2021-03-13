if __name__ == '__main__':
    """
    A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
    Each value stored in a dictionary can be accessed using a key, 
    which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.
    """
    phonebook = {}
    phonebook["Alex"] = +380972121211
    phonebook["Oleg"] = +380972121222
    phonebook["Ivan"] = +380972121233
    print(phonebook)

    # Alternatively, a dictionary can be initialized with the same values in the following notation:
    phonebook = {
        "Alex": +380972121211,
        "Oleg": +380972121222,
        "Ivan": +380972121233
    }
    print(phonebook)

    # Iterating over dictionaries
    print("iterate dictionary:")
    for key, value in phonebook.items():
        print(key, value)

    # Removing a value
    print("Removing a value from dictionary:")
    del (phonebook["Oleg"])
    print(phonebook)
    phonebook.pop("Ivan")
    print(phonebook)


def dictionary_task1():
    """
    Create new dictionary with contact list - Alex, Igor, Ilon, Nikola.
    Add "Max" to the phonebook with the phone number +38097212199, and remove Alex from the phonebook.
    """
    my_dictionary = {}
    # TODO write the code
    my_dictionary["Alex"] = +380972121211
    my_dictionary["Igor"] = +380972121222
    my_dictionary["Ilon"] = +380972121233
    my_dictionary["Nikola"] = +380972121244
    my_dictionary.update({"Max": +38097212199})
    my_dictionary.pop("Alex")
    return my_dictionary
