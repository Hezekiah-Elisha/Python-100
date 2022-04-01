#!/usr/bin/python3
from sys import argv


def greedy_cash(x):
    """
    Algorithm:

        Sort the array of coins in decreasing order.
        Initialize result as empty.
        Find the largest denomination that is smaller than current amount.
        Add found denomination to result. Subtract value of found denomination\
        from amount.
        If amount becomes 0, then print result.
        Else repeat steps 3 and 4 for new value of V.
    """

    coins = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    result = []

    for coin in coins:
        while x >= coin:
            result.append(coin)
            x = x - coin

    return result


if __name__ == '__main__':

    print(greedy_cash(int(argv[1])))
