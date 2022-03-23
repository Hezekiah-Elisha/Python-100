#!/usr/bin/python3
def gcd(a, b):
    if (b != 0):
        if b % a == 0:
            return a
        else:
            c = a
            a = b % a
            b = c
            return gcd(a, b)
    else:
        return "One or both of your parameters are/is zero(0)"


if __name__ == '__main__':
    print(gcd(78, 128))
