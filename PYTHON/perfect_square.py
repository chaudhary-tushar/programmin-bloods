#checking wether a given number is a perfect square or not
import math
x=int(input("Enter the number:-"))
root=math.sqrt(x)
if root- math.floor(root)==0:
    print(f"The number {x} is a perfect square")
else:
    print(f"{x} is not a perfect square")
