# Key - Value
# point = {"x": 1, "y": 2}

# x=1 "Keyword argument"
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20

if "a" in point:
    print(point["a"])
# Try to find, and if it doesn't return something
print(point.get("a", 0))
del point["x"]
print(point)

for key, value in point.items():
    # print(key, point[key])
    print(key, value)
