# this code is to print pattern like 
''' 12345
    1234
    123
    12
    1'''
x=int(input("enter height of pattern :- "))
for i in range(x,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()