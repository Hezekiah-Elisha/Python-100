![Logo](images/logo.png)
# Python-100
This is a #100DaysOfCode

## Challenge 1: Capital Indexes
Write a function named ```capital_indexes```. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling ```capital_indexes("HeLlO")``` should return the list ```[0, 2, 4]```.

## Challenge 2: Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, ```mid("abc")``` should return "b" and ```mid("aaaa")``` should return "".

## Challenge 3: Online Status

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

```
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
```

In this case, the number of people online is ```2```.

Write a function named ```online_count``` that takes one parameter. The parameter is a dictionary that maps from strings of names to the string ```"online"``` or ```"offline"```, as seen above.

Your function should return the number of people who are online.

## Challenge 4: Randomness

Define a function, ```random_number```, that takes no parameters. The function must generate a random integer between ```1``` and ```100```, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling ```random_number()``` some times might first return ```42```, then ```63```, then ```1```.

## Challenge 5: Type check

Write a function named ```only_ints``` that takes two parameters. Your function should return ```True``` if both parameters are integers, and ```False``` otherwise.

For example, calling ```only_ints(1, 2)``` should return ```True```, while calling ```only_ints("a", 1)``` should return ```False```.
## Challenge 6: Double Letters

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string ```"hello"``` has ```l``` twice in a row, while the string ```"nono"``` does not have two identical letters in a row.

Define a function named ```double_letters``` that takes a single parameter. The parameter is a string. Your function must return ```True``` if there are two identical letters in a row in the string, and ```False``` otherwise.

## Challenge 7: Adding and removing dots

Write a function named ```add_dots``` that takes a string and adds ```"."``` in between each letter. For example, calling ```add_dots("test")``` should return the string ```"t.e.s.t"```.

Then, below the ```add_dots``` function, write another function named ```remove_dots``` that removes all dots from a string. For example, calling ```remove_dots("t.e.s.t")``` should return ```"test"```.

If both functions are correct, calling ```remove_dots(add_dots(string))``` should return back the original ```string``` for any string.

(You may assume that the input to ```add_dots``` does not itself contain any dots.)

## Challenge 8: Counting syllables

Define a function named ```count``` that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

```
"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
```

Your function should count the number of syllables and return it.

For example, the call ```count("ho-tel")``` should return ```2```.

## Challenge 9: Anagrams

Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named ```is_anagram``` that takes two strings as its parameters. Your function should return ```True``` if the strings are anagrams, and ```False``` otherwise.

For example, the call ```is_anagram("typhoon", "opython")``` should return True while the call ```is_anagram("Alice", "Bob")``` should return ```False```.

## Challenge 10: Flatten a list

Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function ```flatten```. It should take a single parameter and return a list.

For example, calling:

```
flatten([[1, 2], [3, 4]])
```

Should return the list:

```
[1, 2, 3, 4]
```

## Challenge 11: Min-maxing

Define a function named ```largest_difference``` that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call ```largest_difference([1, 2, 3])``` should return ```2``` because ```3 - 1``` is ```2```.

You may assume that no numbers are smaller or larger than ```-100``` and ```100```.

## Challenge 12: Divisible by 3

Define a function named ```div_3``` that returns ```True``` if its single integer parameter is divisible by 3 and ```False``` otherwise.

For example, ```div_3(6)``` is True because ```6/3``` does not leave any remainder. However ```div_3(5)``` is False because ```5/3``` leaves ```2``` as a remainder.

## Challenge 13: Tic tac toe input

Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

```
1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
```
The board is represented as a 2D list:
```
board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
```
Imagine if your user enters ```"C1"``` and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string ```"C1"``` to row 0 and column 2 so that you can check ```board[row][column]```.

Your task is to write a function that can translate from strings of length 2 to a tuple ```(row, column)```. Name your function ```get_row_col```; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, ```calling get_row_col("A3")``` should return the tuple ```(2, 0)``` because A3 corresponds to the row at index ```2``` and column at index ```0``` in the board.
