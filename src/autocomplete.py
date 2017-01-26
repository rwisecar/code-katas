"""Take in an input string and a dictionary array.
Return the values from the dictionary that start with the input string.
Account for dictionary order and capitalization."""


def autocomplete(input_, dictionary):
    return_arr = []
    input_ = "".join([i for i in list(input_) if i.isalpha()])
    for d in dictionary:
        if d.lower().startswith(input_.lower()):
            return_arr.append(d)
    return return_arr[:5]
