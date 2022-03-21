#!/usr/bin/python3
def palindrome(i):
    if i == i[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(palindrome('aba'))
