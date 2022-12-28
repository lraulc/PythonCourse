letters = ["a","b","c","d"]
letters[0] = "A"

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

numbers = [1,2,3,4,5,6]
# list unpacking
first,*other, last = numbers
print(first,last, other)