#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a python program to convert a string to lower case
x=input("enter your name")
x.lower()


# In[1]:


#2.Write a python program to convert only odd indexed characters to lower case
x=input("enter the string")
y=""
for i in range(len(x)):
    if i%2==0:
        y=y+x[i].upper()
    else:
        y=y+x[i].lower()
print(y)


# In[2]:


#3.Write a python program to convert only even indexed characters to lower case
x=input("enter the string")
y=""
for i in range(len(x)):
    if i%2==0:
        y=y+x[i].lower()
    else:
        y=y+x[i].upper()
print(y)


# In[6]:


#4.Write a python program to convert only odd indexed characters to upper case
x=input("enter the string")
y=""
for i in range(len(x)):
    if i%2!=0:
        y=y+x[i].upper()
    else:
        y=y+x[i].lower()
print(y)


# In[7]:


#5.Write a python program to convert only even indexed characters to upper case
x=input("enter the string")
y=""
for i in range(len(x)):
    if i%2!=0:
        y=y+x[i].lower()
    else:
        y=y+x[i].upper()
print(y)


# In[11]:


#6.Write a python program where you have different variable which contains your name,sex,age, phone no ,fathers name and 
#mothersname.And by using this variable create a variable named bio-data where you will use all 
this variable
name=input("Enter your name")
gender=input("Enter your sex")
age=int(input("Enter your age"))
phone_number=int(input("Enter your number"))
father_name=input("Enter your father name")
mother_name=input("Enter your mother name")
bio_data="my name is {0} I am {1} and my age is {2} , my number is {3} and my father name is {4} and mother name is {5}"
bio_data.format(name,gender,age,phone_number,father_name,mother_name)


# In[19]:


#7.Write a python program to count how many times “@” occurred
var1=input("enter your string")
var2=var1.count("@")
print(type(var1))
print(var2)


# In[18]:


#8.Write a python program to get only names from the string  “name1.@gmail.com,name2.@gmail.com,name3.@gmail.com”
var1="name1.@gmail.com,name2.@gmail.com,name3.@gmail.com"
var2=var1.split(".@gmail.com")
var3=" ".join(var2)
var3


# In[28]:


#9.Given a string of odd length greater that 9,return a new string made of the middle three characters of a given String
var1="mynameissan"
print(var1[len(var1)//2-1]+var1[len(var1)//2:len(var1)//2+2])


# In[29]:


#10. Write a python program to insert a 2 string in the middle of 1 string
s1="myn"
s2="sa"
print(s1[0:1]+s2[0:3]+s1[1:])


# In[32]:


#11.11. Write a program to remove vowels from the entire alphabets
var1="abcdefghijklmnopqrstuvwxyz"
var2=["a","e","i","o","u"]
x=[]
for i in var1:
    if i not in var2:
        x.append(i)
y=" ".join(x)
y


# In[ ]:




