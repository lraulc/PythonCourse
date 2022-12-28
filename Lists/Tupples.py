# Is a Read-only list

point = (1,2,3,10)
print(point[0:2])

x,y,z,w = point
print(x,y,z,w)

if 10 in point:
    print("exists")