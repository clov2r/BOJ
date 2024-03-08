x, y, z = input().split()  
x = int(x)  
y = int(y)  
z = int(z)  

if x == y == z:
    print(10000 + x * 1000)
elif x == y or y == z or x == z:
    if x == y or x == z:
        print(1000 + x * 100)
    else:  # y == z
        print(1000 + y * 100)
else:
    print(max(x, y, z) * 100)