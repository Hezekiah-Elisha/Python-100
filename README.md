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
