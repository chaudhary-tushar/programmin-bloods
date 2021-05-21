# for patterns like 
#####
 ###
  #  
x=int(input("give length:-  "))
for i in range(1,x+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(1,(x-i+1)*2):
        print("*",end="")
    print()