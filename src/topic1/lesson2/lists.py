if __name__ == '__main__':
    print("lists")
    """
    Lists and arrays:
    Lists are very similar to arrays. But lists are just like dynamic sized arrays. 
    They can contain any type of variable, and they can contain as many variables as you wish.
    For example list may contain DataTypes like Integers, Strings, as well as Objects. 
    Lists are mutable, and hence, they can be altered even after their creation. 


    List can be created by just placing the sequence inside the square brackets [].
    [1,2,3,4,5,6,7,"hello"]
    Unlike Sets, list doesn’t need a built-in function for creation of list.
    
    Main list methods:
    append() Add an element to the end of the list
    extend() Add all elements of a list to the another list
    insert() Insert an item at the defined index
    remove() Removes an item from the list
    pop() Removes and returns an element at the given index
    clear()	Removes all items from the list
    index()	Returns the index of the first matched item
    count()	Returns the count of number of items passed as an argument
    sort() Sort items in a list in ascending order
    reverse() Reverse the order of items in the list
    copy() Returns a copy of the list
    
    """
    print("REVERSE ")
    reverse_list = [1, 2, 3, 4, 5, 6, 7]
    reverse_list.reverse()
    print("reverse ==>>", reverse_list)

    copied_list = reverse_list.copy()

    print("copy == >", copied_list)

    new_list = [1]
    print("new_list => ", new_list)
    new_list.append("Артем")
    print("new_list after element append => ", new_list)
    new_list.insert(0, "Артем")
    print("new_list after element insert => ", new_list)
    new_list.remove("Артем")
    print("new_list after element remove => ", new_list)

    a = 1
    a = new_list.pop(0)
    print("a = ", a)
    print("new_list after element pop => ", new_list)

    print("POP == ", new_list)
    new_list.append("element A")
    print("POP after append == ", new_list)
    new_list.insert(0, "element B")
    print("POP after insert == ", new_list)
    new_list.pop(1)
    new_list.append("element B")
    new_list.append("element B")
    print("POP index 1 == ", new_list)
    new_list.remove("element B")

    print("STEP 1 - remove == ", new_list)

    a = 10
    b = 20
    c = "HELLO"
    index = new_list.index("element B")
    print("index Artem == ", index)
    new_list.index("element A")
    print("STEP 2 - index == ", new_list)
    new_list.append("A")

    count = new_list.count("element B")
    print("COUNT == ", count)

    new_list.append("AA")
    print("EXTENDED =>> ", new_list)

    new_list.sort()
    print("SORT ==> ", new_list)

    new_list.append(5)
    new_list.append(10)
    new_list.extend([3, 2, 3, 4, 10])

    print("after APPEND", new_list)
    print(new_list.index(10))

    print("count()", new_list.count(10))

    new_list.clear()
    print("Після видалення", new_list)

    new_list_1 = [1, 2, 3]
    new_list_2 = [10, 20, 30, 10]
    new_list_3 = []

    # Результат склеивания листов ПРИСВОИТЬ новой переменной "variable"
    new_list_3.extend(new_list_1)
    new_list_3.extend(new_list_2)
    new_list_3.append("Альбина")
    new_list_3.insert(1, "Альбина")
    new_list_3.insert(0, "Женя")

    print("new_list_3", new_list_3)

    a = 1
    print("a = 1 === ", a)

    print("new_list_3 == ", new_list_3)

    print("++++ ", new_list_1.extend(new_list_2))

    print("EXTEND", new_list_1, new_list_2)
    print("EXTEND", )

    print("HELLO new_list_1 = ", new_list_1)

    my_boxes = [1, 2, 3, 4, 15, 100, "hello", "hello", "hello"]
    my_boxes.extend("123")

    """indexes= 0  1  2  3  4  """
    print(my_boxes)

    # Accessing elements from the List
    print("Accessing element by index = ", my_boxes[6])

    # Accessing elements with negative indexing. Negative index represents positions from the end of the list.
    print("Accessing with negative index - ", my_boxes[-1])

    # Knowing the size of List
    print("Size of list - ", len(my_boxes))

    # append() - adding elements to a List
    print(my_boxes)
    my_boxes.append(100)
    print(my_boxes)
    my_boxes.append(200)
    print(my_boxes)
    my_boxes.append("hello")
    print(my_boxes)
    print("get first element of list - ", my_boxes[0])
    print("Size of list - ", len(my_boxes))

    # insert() - Insert element to the specific position. Method requires two arguments(position, value).
    my_boxes.insert(0, "new list element")
    print(my_boxes)

    # extend() - this method is used to add multiple elements at the same time at the end of the list.
    print("extend")
    my_boxes_new_list = ["new 1", "new 2", "new 3"]
    #                      0         1       2
    my_boxes.extend(my_boxes_new_list)
    # [1, 2, 3, 4, 15, 100, 'hello', 100, 200, 'hello', +++ 'new 1', 'new 2', 'new 3']
    print(my_boxes)

    print("initial list =>> ", my_boxes)
    my_boxes.insert(0, "new_inserted_element")
    print("new_inserted_element =>> ", my_boxes)

    # remove() - Removing Elements from the List. Method removes only one element at a time.
    my_boxes.remove("hello")
    my_boxes.remove("hello")
    my_boxes.remove("hello")
    my_boxes.remove("hello")

    my_boxes.remove(200)
    print("After removing == ", my_boxes)

    # pop() - Remove and return an element from the set
    print("Get and remove last element -", my_boxes.pop())
    print("Get and remove first element -", my_boxes.pop(0))
    print(my_boxes)

    # Slicing of a List
    new_list = ['l', 'e', 's', 'o', 'n', 'o', 'n', 'e']
    print("Sliced new_list - ", new_list[2:5])
    print("Sliced new_list - ", new_list[:5])
    print("Sliced new_list - ", new_list[5:])

    # Negative index List slicing
    print("Sliced new_list with negative index - ", new_list[-8:-3])

    """
    My lab 1
    """
    my_boxes
