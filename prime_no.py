num = int(input("Enter a number: "))
if num == 1:
    print(num, "is not a prime number")
elif num == 2:
    print(num, "is a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")
