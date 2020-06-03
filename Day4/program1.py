Size = int(input("Enter the size of tuple: "))
print("Enter the elements in tuple one by one")
ele = []
for i in range(Size):
    ele.append(input())
ele = tuple(ele)
element = input("Enter the element whose occurrences you want to know: ")
print("Tuple contains the element", ele.count(element), "times")
