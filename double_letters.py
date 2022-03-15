#!/usr/bin/python3
def double_letters(name):
    new_string = list(name)
    sm = False
    for i, x in enumerate(new_string):
        # print(x)
        if (i + 1 < len(new_string) and i - 1 >= -1):
            prev_el = str(new_string[i-1])
            curr_el = str(x)
            next_el = str(new_string[i+1])
            print("{} {}".format(curr_el, next_el))
            if curr_el == next_el:
                sm = True
                # print("{} {}".format(prev_el, curr_el))
                # return True

    # if name == False:
    #     return False
    # else:
    return sm


print(double_letters('aa'))
