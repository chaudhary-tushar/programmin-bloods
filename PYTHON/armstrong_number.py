#To find Armstrong number
""" A positive integer is called an armstrong number of oreder n if:-
abcd... = a^n + b^n + c^n + d^n..."""
n=input("Enter the number tpo be tested upon:- ")
m=len(n)
N=int(n)
sum=0
for i in range(m):
    sum+=int(n[i])**int(m)
if sum==N:
    print(f"The given number {n} is an armstrong number")
else:
    print(f"The given number {n} is not an armstrong number")
