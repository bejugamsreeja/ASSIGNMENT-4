#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Write a Python program to square the elements of a list using map() function
nums = [4,5,2,9] 
squared_list=[]
for num in nums:
    square_num=num*num
    squared_list.append(square_num)


# In[2]:


squared_list


# In[3]:


def square(num):
    return num*num


# In[4]:


map(square,nums)


# In[5]:


list(map(square,nums))


# In[6]:


##Write a Python program to triple all numbers of a given list of integers. Use Python map

nums = [1, 2, 3, 4, 5, 6, 7]
print("sample list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of  list numbers:")
print(list(result))


# In[7]:


#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
result = lambda x: x + 25
answer=result(10)
print(answer)

