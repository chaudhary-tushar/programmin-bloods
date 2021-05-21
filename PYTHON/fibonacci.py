x=int(input("Enter fibonacci length:- "))
y,z=0,1
for i in range(x):
    if i <2:
        print(i,end=" ")
    else:
        a=y+z
        y=z
        z=a
        
        print(a, end=" ")