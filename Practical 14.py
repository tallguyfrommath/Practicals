# Practical 14
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 28-01-2021
b=[]
c,d="",""
def sin(x,n):
    global d
    d=n
    a=["-",""]
    for (i,j) in zip(range(1,(n*2),2),range(n)):
        b.append(f"{a[(j+1)%2]}x^{str(i)}/{str(i)}! + ")
    global c
    for k in b:
        c+=k
    print(f'The expansion for sin x till {d} terms is \nsin(x)= {c[0:-2]}')
sin("x",9)
