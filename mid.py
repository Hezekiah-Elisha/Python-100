#!/usr/bin/python3
def mid(name):
    new_name = list(name)
    if len(new_name) % 2 == 0:
        return ""
    else:
        index = int(len(new_name) / 2)
        return new_name[index]


print(mid("hezekiaha"))
