items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# Use for using function as an argument to a function
items.sort(key=lambda item:item[1])
print(items)