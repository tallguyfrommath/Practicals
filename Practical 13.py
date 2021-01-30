# Practical 13
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 28-01-2021

a = "12345"
for i in range(5):
    ans = ""
    for j in range(4-i,5):
        ans+=a[j]
    print("\n",ans.rjust(5))