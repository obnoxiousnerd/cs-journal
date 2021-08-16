# Menu based program to perform stack operations.

class Stack:
    """
    Class Stack is a classic implementation of the stack data structure.
    """
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        """
        Method push pushes an item in the stack.
        """
        return self.items.append(item)

    def pop(self):
        """
        Method pop pops an item from the stack.
        """
        return self.items.pop()
    
    def peek(self):
        """
        Method peek returns the top of the stack
        """
        if len(self.items) == 0:
            print("Stack is empty.")
            return None
        return self.items[-1]

    def size(self):
        """
        Method size returns the length of the underlying buffer. 
        """
        return len(self.items)


stack = Stack()

def menu_loop():
    menu = """
1. Push
2. Pop
3. Display
4. Size
5. Value of top
6. Quit
"""
    print("Menu for stack operations")
    print(menu)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter item to push (integer): "))
        stack.push(item)

    elif choice == 2:
        popped_item = stack.pop()
        print(popped_item)

    elif choice == 3:
        print(stack.items)

    elif choice == 4:
        print(stack.size())

    elif choice == 5:
        print(stack.peek())
    elif choice == 6:
        exit(0)
    else:
        print("You entered a wrong choice.")
        second_choice = input("Do you want to continue?"
                +" If so, then type 'yes': ")
        if second_choice == "yes":
            menu_loop()
        else:
            exit(0)
    menu_loop()

menu_loop()
