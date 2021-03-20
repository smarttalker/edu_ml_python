"""
Objects are an encapsulation of variables and functions into a single entity.
Objects get their variables and functions from classes.
Classes are essentially a template to create your objects.
"""


class MyClass:
    variable = "custom class var"

    def function(self):
        print("This is a message inside the class.")


class Food():
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color

    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color)


if __name__ == '__main__':
    """
    There are two types of loops in Python, for and while.
    """
    # example 1
    my_object = MyClass()

    # Accessing Object Variables
    print(my_object.variable)
    my_object.variable = 123
    print(my_object.variable)
    my_object.function()

    # example 2
    apple = Food("apple", "red")
    grapes = Food("grapes", "green")
    print(apple.fruit, apple.color)


def class_task1():
    """
    Create the class for describing a 'car'
    """

    class Car:
        name = ""
        color = ""
        # TODO write the code

    return Car()
