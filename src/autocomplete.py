"""Take in an input string and a dictionary array.
Return the values from the dictionary that start with the input string.
Account for dictionary order and capitalization."""


def autocomplete(input_, dictionary):
    return_arr = []
    cap_input = input_.capitalize()
    for d in dictionary[:5]:
        if d[:len(input_)] == input_ or d[:len(input_)] == cap_input:
            return_arr.append(d)
    return return_arr