# Menu based program to perform queue operations.


class Queue:
    """
    Class Queue is a classic implementation of the queue data structure.
    """

    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            print("Queue is empty.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


queue = Queue()

menu = """
1. Enqueue
2. Dequeue
3. Display
4. Size
5. Value of rear
6. Quit
"""
print("Menu for queue operations")
print(menu)


def menu_loop():
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter item to enqueue (integer): "))
        queue.enqueue(item)
    elif choice == 2:
        print(queue.dequeue())
    elif choice == 3:
        print(queue.items)
    elif choice == 4:
        print(queue.size())
    elif choice == 5:
        print(queue.peek())
    elif choice == 6:
        exit(0)
    else:
        print("You entered a wrong choice.")
        second_choice = input("Do you want to continue?" + " If so, then type 'yes': ")
        if second_choice == "yes":
            menu_loop()
        else:
            exit(0)
    menu_loop()


menu_loop()
