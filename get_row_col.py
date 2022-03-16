#!/usr/bin/python3
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return(row, column)

# solution2

# def get_row_col(position):
#     tuple_thing = tuple(position)
#     row = tuple_thing[0]
#     column = int(tuple_thing[1])
#
#     if row not in list(map(chr, range(65, 68))):
#         return f"{row} Should be between A and C"
#     if column not in range(1, 4):
#         return f"{column} Should be between 1, 3"
#
#     # print(tuple( (row, column) ))
#
#     if row == "A":
#         return tuple((0, column-1))
#     elif row == "B":
#         return tuple((1, column-1))
#     else:
#         return tuple((2, column-1))


if __name__ == '__main__':
    print(get_row_col("B1"))
