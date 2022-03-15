def add_dots(name):
    return ".".join(name)


def remove_dots(name):
    return name.replace(".", "")


add_dots("hezekiah")
remove_dots("h.e.z.e.k.i.a.h")
print(remove_dots(add_dots("hezekiah")))
