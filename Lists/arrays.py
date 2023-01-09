from array import array

# Used to generate an array of signed ints ("i")
numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(0, 1)
numbers.pop()
# numbers[0] = "hello"
# Will not work since the array must be of signed ints.
