import sys

__original_input_fn = input


def input(arg):
    try:
        result = __original_input_fn(arg)
        print(result)
        return result
    except EOFError:
        print(
            "The program is trying to accept input",
            "but the input file is empty.",
            "Please add the inputs in the respective file.",
            file=sys.stderr,
        )
        exit(1)
