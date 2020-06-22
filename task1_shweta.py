#!/usr/bin/env python
# coding: utf-8

# In[5]:


## Conditional Statements
a=20
if a%2==0:
    print('Even')
else:
    print('odd')    

if a<10:
    print('one digit number')
elif a<100:
    print('two digit number')
else:
    print('greater than two digits')
    


# In[8]:


## loops

# for loop
a=[12,17,13,1,44,61]
for item in a:
    if item%2==0:
        print('Even')
    else:
        print('odd')

# while loop
print('While loop:')
i=0
while(i<len(a)):
    if a[i]%2==0:
        print('Even')
    else:
        print('odd')
    i+=1


# In[5]:


## dicitionary
dict={'a':10,'b':11,'c':12}
# print keys
print(dict.keys())
# print values
print(dict.values())
# print value of specific key
print(dict.get('a'))


# adding an element
dict.update({'d':13})
print(dict)
# deleting an element
deleted_item=dict.pop('b')
print(dict)


# In[6]:


## set
b={1,2,3,1,3,2,5,21,4,1,1,2}
print(b)
# length of set
print(len(b))
# adding an element to set
b.add(8)
print(b)
# adding an set to set
x={1,4,9,2}
b.update(x)
print(b)
#deleting an item in set
deleted_item=b.remove(2)
print(b)


# In[20]:


## type casting
a="10.87"
a_float=float(a)
print(a_float)
a_int=int(a_float)
print(a_int)

## typecasting of data structure
a=(1,2,5,4,2,4,5)
a_list=list(a)
print(a_list)
a_set=set(a)
print(a_set)


# In[29]:


## function
def test(fname,lname):
    return fname+lname

a=test("Ram","Sharma")
print(a)


# function with default arguments
def test1(fname="",lname=""):
    return fname+lname

b=test1("john","Doe")
print(b)


# In[77]:


## file read
f=open('test.txt','r')
a=f.read()
print(a)
f.close()
   


# In[78]:


# file append
f=open('test.txt','a')
f.write(' this is newly added line 1')
f.close()
f=open('test.txt','r')
print(f.read())
f.close()


# In[79]:


# file write
f=open('test.txt','w')
f.write(' this is newly added line 1')
f.close()
f=open('test.txt','r')
print(f.read())
f.close()


# In[103]:


## classes and object
class abc: 
    
    def __init__ (self,fname,lname):
        self.fname=fname
        self.lname=lname
                
    def setAge(self,age):
        self.age=age
        
    def getAge(self):
        return self.age
    
    def fullName(self):
        return self.fname+self.lname
    
## object creation
obj=abc('john','doe')
print("First name:"+obj.fname)
print("Last name:"+obj.lname)
obj.setAge(20)
obj_age=obj.getAge()
print("Age: "+str(obj_age))
print("Full Name: "+obj.fullName())


# In[111]:


## implementing switch

def one():
    return "1 is enetered"
def two():
    return "2 is enetered"
def zero():
    return "0 is enetered"
def default():
    return "some key other than 0,1 and 2 is enetered"
switch_dict = {
    1: one,
    2: two,
    0: zero  
    }

def switch(a):
    return switch_dict.get(a,default)()

print(switch(1))
print(switch(3))


# In[ ]:




