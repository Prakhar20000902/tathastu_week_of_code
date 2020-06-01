num = int(input("Enter a number: "))

if (num % 2) == 0:
   print("num is Even",num)
else:
   print("num is Odd",num)


if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

org=num
tem=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(tem==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

sum = 0
temp = org
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if org == sum:
    print(org, "is armstrong number")
else:
    print(org, "is not a armstrong number")

