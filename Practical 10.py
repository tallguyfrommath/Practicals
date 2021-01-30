# Practical 10
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 21-01-2021

y = int(input('enter the number of terms you want of the fibonacci series '))
if y == 0:
    print('enter a number greater than 0')
a = [0,1]
if y>2:
    for i in range(2,y):
        a.append(a[i-2]+a[i-1])
for c in range(y):
    print(a[c],end=" ")
