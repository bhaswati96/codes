#!/usr/bin/env python
# coding: utf-8

# In[3]:


def prime(num):
    for n in range(2,num):
        if num%n == 0:
            print(num,'is not prime')
            break
        else:
            print(num,'Is prime')
            
        


# In[4]:


prime(4)


# In[9]:


print("William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]
William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]")


# In[10]:


print("William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]
      ")


# In[11]:


print("""William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]"""")


# In[12]:


print('''William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]
''')


# In[16]:


a="""William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]"""
print(a)


# In[17]:


a='''William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and the "Bard of Avon" (or simply "the Bard").[5][b] His extant works, including collaborations, consist of some 39 plays,[c] 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.[7]'''
print(a)


# In[18]:


cities='Manchester,Rome,Paris,London,Amerstredam'
print(cities)


# In[19]:


cities=['Manchester','Rome','Paris','London','Amerstredam']
print(cities)


# In[20]:


cities=['Manchester','Rome','Paris','London','Amerstredam']
print(cities[3])


# In[22]:


cities=['Manchester','Rome','Paris','London','Amerstredam']
cities.append("Tuscany")
print(cities)


# In[28]:


cities=['Manchester','Rome','Paris','London','Amerstredam']
len(cities)


# In[24]:


cities=('Manchester','Rome','Rome','Paris','London','Amerstredam')
print(cities)


# In[31]:


sports={"Virat Kohli":"cricket","saina nehrwal":"Badminton"}
print(sports)


# In[1]:


get_ipython().run_line_magic('pinfo', 'range')


# In[6]:


for i in range(0,10):
    print(i) 
    
    


# In[9]:


for i in range(0,10):
    print("I love this weather")
    


# In[12]:


for i in range(1,11):
    print(i**3)


# In[17]:


#cube f number betwwen 1 t0 10
i=1
while(i<11):
    print(i**3)
    i=i+1


# In[20]:


#step range
for i in range(1,11,2):
    print(i)
    


# In[26]:


import time
print("using while loop")
start_time=time.time()
i=1
while(i<11):
    print(i**3)
    i=i+1

end_time=time.time()
print("start time is",start_time)
print("end time is",end_time)
print(end_time-start_time)

print("using for loop")
start_time=time.time()
for i in range(1,11):
    print(i**3)
end_time=time.time()
print("start time is",start_time)
print("end time is",end_time)
print(end_time-start_time)



# In[27]:


def mycubicfn(a):
    result=a**3
    return result
a=int(input("Enter the number"))
result=mycubicfn(a)
print(result)


# In[32]:


import math as m
a=int(input("Enter the number"))
print ("Square root",m.sqrt(a))
print ("cube Power",m.pow(a,3))


# In[ ]:




