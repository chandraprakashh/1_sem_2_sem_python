nterms = 10

n1 = int(input("enter the first number::"))
n2 = int(input("enter the second number::"))
count = 0

# check if the number of terms is valid

if nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    
