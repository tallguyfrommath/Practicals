# Practical 7
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 14-01-2021


y = input("enter an integer: ")
k = []
for i in y:
    k.append(i)
x=len(k)
a=[]
for i in range(len(k)):
    a.append(int(k[i])**x)
if sum(a)==int(y):
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")

