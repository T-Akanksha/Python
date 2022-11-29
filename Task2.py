#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1) Write a program to accept two numbers from the user and calculate multiplication, division


x=int(input("enter a number "))
y=int(input("enter a number "))
print("multiplication={}".format(x*y))
print("Division={}".format(x/y))


# In[5]:


#2) Write a python program to print the characters from a string that are present at an even index


a=input("Enter your string : ")
l=len(a)
for i in range(l):
    if i%2==0:
        s=a[i]
        print(s)
    


# In[6]:


#3) Write a python program to print the characters from a string that are present at an odd index


a=input("Enter your string : ")
l=len(a)
for i in range(l):
    if i%2!=0:
        s=a[i]
        print(s)
    


# In[9]:


#4) Write a python program which will print the sum of the two numbers if the two numbers are even or it will print the
#difference of two numbers


x=int(input("enter a number : "))
y=int(input("enter a number : "))
if x%2==0 and y%2==0:
    print("sum : {}".format(x+y))
else:
    print("difference : {}".format(x-y))


# In[13]:


#5) Write a python program to convert all even indexed alphabets to upper and odd indexed char


x=input("enter the alphabets : ")
a=len(x)
s=" "
for i in range(a):
    if i%2==0:
        p=x[i].upper()
        s=s+p
    else:
        k=x[i].lower()
        s=s+k
print(s)
        


# In[15]:


#6) Write a python program which will print True if the input number is divisible by 5 or else False


x=int(input("Enter a number : "))
if x%5==0:
    print("True")
else:
    print("False")


# In[17]:


#7) Given two integer numbers return their product only if the product is greater than 1000, else return their sum


x=int(input("Enter number : "))
y=int(input("Enter number : "))
z=x*y
if z>1000:
    print("{}".format(x*y))
else:
    print("{}".format(x+y))
    


# In[21]:


#8) Given two strings x, y writes a program to return a new string made of x and y’s first, middle, and last characters


x=input("Enter a string : ")
y=input("Enter a string : ")
z=x[0]+y[0]+x[len(x)//2]+y[len(x)//2]+x[-1]+y[-1]
print(z)


# In[30]:


#9) Write a python program to take three names as input from a user in the single input () function call


def names(a):
    a=input("enter three names")
    s=a.split()
    print("Name1 :" ,s[0])
    print("Name2 :" ,s[1])
    print("Name3 :" ,s[2])


# In[31]:


names("Akanksha klyani Rama")


# In[3]:


#10) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '@',
#except the first char itself.


x=input("enter a string : ")
s=x[0]
x=x.replace(s,"@")
x=s+x[1:]
print(x)
    


# In[5]:


#11) Write a Python program to add 'ing' at the end of a given string (string length should be equal to or more than 3). If
#the given string already ends with 'ing' then add 'ly' instead.If the string length of the given string is less than 3, leave
#it unchanged


x=input("enter a string : ")
l=len(x)
if l>=4:
    if x.endswith("ing"):
        w=x[:-3]+"ly"
        print(w)
    else:
        r=x[0:]+"ing"
        print(r)
elif l<3:
    print(x)
    
    


# In[9]:


#12) Write a python program that accepts two inputs num1 and num2 print True if one of them is 10 or if their sum is 10
#otherwise print False


num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=num1+num2
if num1==10 or num2==10 or num3==10:
    print("True")
else:
    print("False")


# In[11]:


#13) Write a python program that accepts three inputs x, y and z print True if x*y>z otherwise False


x=int(input("enter a num : "))
y=int(input("enter a num : "))
z=int(input("enter a num : "))
a=x*y
if a>z:
    print("True")
else:
    print("False")


# In[13]:


#14) Write a python program that accepts two strings inputs return True depending on whether the total number of characters in
#the first string is equal to the total number of characters in the second string


x=input("enter a string : ")
y=input("enter a string : ")
a=len(x)
b=len(y)
if a==b:
    print("True")
else:
    print("False")


# In[17]:


#15) Write a python program that takes a string input, we'll say that the front is the first three characters of the string.
#If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies
#of the front


x=input("enter a new string")
y=len(x)
if y<3:
    z=x*3
    print(z)
else:
    print(x[0:3])


# In[20]:


#16) Write a python program that takes in a word and determines whether or not it is plural. A plural word is one that ends in
#"s".

x=input("enter a word: ")
if x.endswith("s"):
    print("plural")
else:
    print("not a plural")


# In[24]:


#17) A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves drinks to
#people 18 and older and when he's not on break (True means break and False means not a break time). Given the person's age,
#and whether break time is in session, create a python program which prints whether he should serve drinks or not.

person_age=int(input("Enter your age : "))
break_time=input("Enter break is true or false")
if person_age>=18 and break_time==("false"):
    print("Bartender will serve the drink")
else:
    print("Bartender will never serve the drink")


# In[25]:


#18) Manoj Kumar has family and friends. Help him remind them who is who. Given a string with a name, return the relation of 
#that person to Manoj Kumar.
#Person Relation
#Shiva father
#Letha mother
#Tarun brother

relative=input("Enter the name : ")
if relative=="Shiva":
    print("Father")
elif relative=="Letha":
    print("Mother")
elif relative=="Tarun":
    print("Brother")
else:
    print("not related to manoj")


# In[29]:


#19) Write a python program that takes a string, breaks it up and returns it with vowels first, consonants second. For any
#character that's not a vowel (like special characters or spaces), treat them like consonants

a=input("enter a string: ")
b=""
c=""
for s in a:
    if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
        b=b+s
    else:
        c=c+s
print(b+c)


# In[31]:


#20) Create a dynamic calculator which asks for numbers and operator and return the answers

x=int(input("Enter first num: "))
y=int(input("Enter second num: "))
z=input("Enter the operator: ")
if z=="+":
    print("{}+{}={}".format(x,y,x+y))
elif z=="-":
    print("{}-{}={}".format(x,y,x-y))
elif z=="*":
    print("{}*{}={}".format(x,y,x*y))
elif z=="**":
    print("{}**{}={}".format(x,y,x**y))
elif z=="//":
    print("{}//{}={}".format(x,y,x//y))
else:
    print("wrong operator")


# In[ ]:




