#This programme finds if a number is prime or not using for loops
num=int(input("Enter a number to find out wether it is prime or not: - "))
P=bool
for i in range(2,num):
    if num%i==0:
        print(f"{num} is not a prime number")
        p=False
        break
    else:
        p=True
    
    
if p==True:
    print(f"{num} is a prime number")
