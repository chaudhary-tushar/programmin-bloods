#The formulae for compound interest is "A=P(1+r/n)**(n*t)" 
''' A = Final amount
    P = Principal amount
    r= rate of interest
    n = number of times interest applied per time period
    t = number of time periods elapsed'''
import math
P=float(input("Enter the pricipal amount:- "))
R=float(input("Enter the rate of interest: - "))/100
N=float(input("Number of times interest is compounded:- "))
T=float(input("The time for which money is invested:- "))
Total=P*((1+(R/N))**(N*T))
Total=float("{:.2f}".format(Total))
CI=Total-P
print(f"Compound Interest after {T} year/years at {R*100} per year is {CI} and the total amount accumulated is {Total}")