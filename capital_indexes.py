def capital_indexes(param):
    new_string = list(param)
    arr = []
    for index, letter in enumerate(name_string):
        if str(letter).isupper():
            arr.append(index)
    return arr
