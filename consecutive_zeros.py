#!/usr/bin/pytho3
def consecutive_zeros(x):
    c = list(x)
    count = 0
    result = 0

    for i in range(0, len(c)):
        if(c[i] == '1'):
            count = 0
        else:
            count += 1
            result = max(result, count)

    return result


if __name__ == '__main__':
    print(consecutive_zeros("10101010100010101"))
