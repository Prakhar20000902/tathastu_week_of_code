x = int(input("enter a number:"))
a = 0
b = 1
print("the fibonacci series upto ", x , "is")
for i in range(x):
    print(a)
    c = a + b
    a = b
    b = c
