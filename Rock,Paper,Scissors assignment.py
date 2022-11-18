#!/usr/bin/env python
# coding: utf-8

# In[10]:


p1=input("enter your choice ")
p2=input("enter your choice ")
if p1=="rock" and p2=="rock" or p1=="paper" and p2=="paper" or p1=="scissors" and p2=="scissors":
    print("play again same")
elif p1=="rock" and p2=="paper" or p1=="paper" and p2=="scissors" or p1=="scissors" and p2=="rock":
    print("p2 wins")
elif p1=="rock" and p2=="scissors" or p1=="paper" and p2=="rock" or p1=="scissors" and p2=="paper":
    print("p1 wins")
else:
    print("written mistake")


# In[ ]:





# In[ ]:




