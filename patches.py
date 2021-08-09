__original_input_fn = input
def input(arg):
    result = __original_input_fn(arg)
    print(result)
    return result

