# Practical 12
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 21-01-2021
a = 0
g = int(input("enter a number "))
while a ==0:
    n = int(input('enter a number, -1 to stop '))
    if n == -1:
        print('the greatest of entered numbers is',g)
        break
    else:
        if n>g:
            g = n
