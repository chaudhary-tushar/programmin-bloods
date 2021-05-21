#for patterns like these
  #
 ##
###
 ##
  #
'''
n= int(input("give half the height :- "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''
n= int(input({"lkh"}))
for x in range(n,-(n+1),-1):
    for y in range(abs(x),0,-1):
        print(" ",end=" ")
    for z in range(abs(x),n+1):
        print("x",end=" ")
    print()