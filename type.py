def only_ints(param1, param2):
    if type(param1) == int and type(param2) == int:
        return True
    else:
        return False

print(only_ints(2, 4))
