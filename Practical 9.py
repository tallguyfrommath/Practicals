# Practical 9
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 21-01-2021

y = int(input('enter your number '))
def fact(x):
    if x == 0:
       return 1
    y = x*fact(x-1)
    return y
print(f"factorial of number {y} is",fact(y))
