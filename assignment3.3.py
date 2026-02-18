# calculator for list operations using case statement (match case in python) and has to take input from the user for the operation they want to perform and the list they want to perform the operation on
my_list=[]
while True: 
    print("""Select operation
 1.Append
2.Extend
3.Insert
4.Remove
5.Pop
6.Clear
7.Index
8.Count
9.Sort
10.Reverse 
""") 
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
    if choice == '1':
        element = input("Enter element to append: ")
        my_list.append(element)
        print("List after append: ", my_list)
    elif choice == '2':
        elements = input("Enter elements to extend (separated by space): ").split()
        my_list.extend(elements)
        print("List after extend: ", my_list)
    elif choice == '3':
        
        index = int(input("Enter index to insert: "))
        element = input("Enter element to insert: ")
        my_list.insert(index, element)
        print("List after insert: ", my_list)
    elif choice == '4':
        element = input("Enter element to remove: ")
        my_list.remove(element)
        print("List after remove: ", my_list)   
    elif choice == '5':
        index = int(input("Enter index to pop: "))
        popped_element = my_list.pop(index)
        print(f"Element '{popped_element}' popped from index {index}. List after pop: ", my_list)
    elif choice == '6':
        my_list.clear()
        print("List after clear: ", my_list)
    elif choice == '7':
        element = input("Enter element to find index: ")
        index = my_list.index(element)
        print(f"Element '{element}' found at index {index}.")
    elif choice == '8':
        element = input("Enter element to count: ")
        count = my_list.count(element)
        print(f"Element '{element}' appears {count} times in the list.")
    elif choice == '9':
        my_list.sort()
        print("List after sort: ", my_list)
    elif choice == '10':
        my_list.reverse()
        print("List after reverse: ", my_list)
    else:
        print("Invalid input")
    break 

#the same above code can be written using match case statement 
my_list=[]
while True:
    print("""Select operation
1.Append
2.Extend
3.Insert
4.Remove
5.Pop
6.Clear
7.Index
8.Count
9.Sort
10.Reverse 
""")
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
    match choice:
        case '1':
            element = input("Enter element to append: ")
            my_list.append(element)
            print("List after append: ", my_list)
        case '2':
            elements = input("Enter elements to extend (separated by space): ").split()
            my_list.extend(elements)
            print("List after extend: ", my_list)
        case '3':
            index = int(input("Enter index to insert: "))
            element = input("Enter element to insert: ")
            my_list.insert(index, element)
            print("List after insert: ", my_list)
        case '4':
            element = input("Enter element to remove: ")
            my_list.remove(element)
            print("List after remove: ", my_list)   
        case '5':
            index = int(input("Enter index to pop: "))
            popped_element = my_list.pop(index)
            print(f"Element '{popped_element}' popped from index {index}. List after pop: ", my_list)
        case '6':
            my_list.clear()
            print("List after clear: ", my_list)
        case '7':
            element = input("Enter element to find index: ")
            index = my_list.index(element)
            print(f"Element '{element}' found at index {index}.")
        case '8':
            element = input("Enter element to count: ")
            count = my_list.count(element)
            print(f"Element '{element}' appears {count} times in the list.")
        case '9':
            my_list.sort()
            print("List after sort: ", my_list)
        case '10':
            my_list.reverse()
            print("List after reverse: ", my_list)
        case _:
            print("Invalid input")
    break