def is_anagram(name1, name2):
    name1 = name1.lower()
    arr1 = list(name1)
    arr1.sort()

    name2 = name2.lower()
    arr2 = list(name2)
    arr2.sort()

    return arr2 == arr1
