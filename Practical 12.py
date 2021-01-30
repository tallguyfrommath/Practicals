# Practical 12
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 21-01-2021
a=[]
y = input("enter a string ")
for (i,j) in zip(y,y[::-1]):
    if i == j:
        a.append(1)
    else:
        a.append(0)
print('not a palindrome') if 0 in a else print('palindrome')
