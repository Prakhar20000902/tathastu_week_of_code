n = int(input("enter a number:"))
for i in range(n):
    print(" " * i + "" + " " * (n - 1 - i) + "")
for i in range(n):
    print((n - 1 - i) * " " + "" + " " * i + "")
