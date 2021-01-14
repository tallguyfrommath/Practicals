# Practical 5
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 14-01-2021
y = int(input("enter a number: "))
if y ==1:
    print("this is not prime")
elif y ==2:
    print("the number is prime")
else:
    m = list()
    k = list()
    for n in range(2,y):
        k.append(n)
        if y % n != 0:
            m.append(n)
    if k == m:
        print(y,"is prime!")
    else:
        print(y,"is not prime")
if int(y)%2==0:
    print(y,"is even ")
else:
    print(y,"is odd")