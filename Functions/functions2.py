def increment(number, by=1):
    return number + by

# print(increment(number=2,by=1))
print(increment(2))
# Keywords "number" and "by" used to reference arguments in a function
# Also called "Keyword arguments"


# Variable Multi-parameter function
# Tupples = Collection of objects - Cannot add more objects
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,4,5))

# Create dictionary / object from function parameters
def save_user(**user):
    print(user["name"])

save_user(id=1, name="John", age=22)