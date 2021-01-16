#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Practical 8
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 14-01-2021


while True:
    print("\t\t\t\tmenu\t\t\t\t")
    y = input("select an option\na. covert to ascii\nb. convert to character\nchoose:").lower()
    if y == "a":
        x = input("enter your character ")
        if len(x)>1:
            raise(Exception("ENTER ONLY ONE CHARACTER"))
        else:
            print("The ascii value of the character is ",ord(x))
        break
    elif y == "b":
        x = input("enter your character ")
        if len(x)>1:
            raise(Exception("ENTER ONLY ONE CHARACTER"))
        else:
            print("The character code of the numbr is ",chr(int(x)))
        break
    else:
        raise(Exception("Please enter a valid choice"))


# In[ ]:




