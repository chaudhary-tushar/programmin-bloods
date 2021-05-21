#This programme is to calculate the difference between two coordinates  on a 2-D plane
import math
x1=float(input("X1 : "))
y1=float(input("Y1 : "))
x2=float(input("X2 : "))
y2=float(input("Y2 : "))
distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
print("The distance between the two points is {:.3f}".format(distance))