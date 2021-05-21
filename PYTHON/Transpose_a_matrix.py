#given a matrix of n dimension find and print its transpose
m=int(input("give n:-"))
matric=[]
for i in range(m):
    a=[]
    for j in range(m):
        a.append(int(input("Enter number:- ")))
    matric.append(a)
           
for i in range(m):
    for j in range(m):
        print(matric[j][i], end=" ")
    print()
'''
n= int(input())
matrix=[list(map(int,input().split()))for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        temp=matrix[i][j]
        matrix[i][j]=matrix[j][i]
        matrix[j][i]=temp
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end="")
    print()'''