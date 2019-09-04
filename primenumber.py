

# take input from the user
User = int(input("Enter a number: "))

# prime numbers are greater than 1
if User > 1:
   # check for factors
   for i in range(2,User):
        if (User % i) == 0:
            print(User,"is not a prime number")
            break
   else:
       print(User,"is a prime number")
       
