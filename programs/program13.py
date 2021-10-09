# Write a random number generator that generates
# random numbers between 1 and 6 (simulates a dice).

import random


def roll_dice():
    """
    Function roll_dice simulates a dice, returning a random number inclusive
    in the range [1,6] on every execution.
    """
    return random.randint(1, 6)


def continue_prompt():
    """
    Function continue_prompt asks if user wants to continue and returns a
    boolean for the result.
    """
    prompt = input("Do you want to continue? [y/N]: ")

    if prompt == "":
        return False
    elif prompt in "yY":
        return True
    else:
        return False


# Main code
if __name__ == "__main__":
    print("Random number generator")

    print(f"The random number is: {roll_dice()}")

    while True:
        should_continue = continue_prompt()
        if should_continue:
            print(f"The random number is: {roll_dice()}")
        else:
            break
