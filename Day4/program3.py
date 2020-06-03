size = int(input("Enter the no of items you want to add in Dictionary: "))
dicty = dict()
for i in range(size):
    keyvalue = input("Enter the key for item " + str(i + 1) + " in dictionary: ")
    value = int(input("Enter the value for item " + str(i + 1) + " in dictionary: "))
    dicty[keyvalue] = value
    
print("The second largest value in the Dictionary is", list(sorted(dicty.values()))[-2])
