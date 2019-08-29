## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 19 to the power of 4?**

# In[1]:


19 ** 4


# ** Split this string:**
# 
#     s = "Hi there Pratibha!"
#     
# **into a list. **

# In[10]:


s = 'Hi there Pratibha!'


# In[15]:


s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[8]:


planet = "Earth"
diameter = 12742


# In[16]:


print("The diameter of {} is {} kilometers.".format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "pratibha" **

# In[21]:


lst = [1,2,[3,4],[5,[100,200,['pratibha']],23,11],1,7]


# In[22]:


lst[3][1][2][0]


# ** Given this nested dictionary grab the word "rana". Be prepared, this will be annoying/tricky **

# In[23]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'rana']}]}]}


# In[25]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     info@pratibha.com
#     
# **So for example, passing "info@pratibha.com" would return: pratibha.com**

# In[30]:


def domainGet(email):
    return email.split('@')[1]
    


# In[48]:


domainGet('info@pratibha.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[70]:


def findDog(str):
    return 'dog' in str.lower()
    


# In[71]:


findDog('Is there a dogs here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[91]:


def countDog(str):
    count = 0
    for word in str.lower().split():
        if word == 'dog':
            count += 1
    return count


# In[92]:


countDog('This dog runs faster than the other dog dude!')



caught_speeding(81,False)


# # You Did It
