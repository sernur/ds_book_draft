#!/usr/bin/env python
# coding: utf-8

# sergazy.nurbavliyev@gmail.com © 2021

# ## Detecting Unfair Coin

# Question: Assume we have a fair coin (one side heads and the other side tails) also we have an unfair coin (both sides heads). You pick randomly one coin, and flip it 5 times. You get 5 heads in a row. What is the probability that you are indeed flipping the unfair coin?
# 

# ### Intuition

# Assume you flip a fair coin 5 times, what is the probability of getting 5 heads in a row. That is $\frac{1}{2^5}$. 
# If this is confusing, think this way, take 5 fair coin and flip once, and now the same question what is the probability of getting 5 heads? The same answer that is $\frac{1}{2^5}$. Which is around 0.03125. If you dont have a calculator, then rougly you can guess $3/96\approx 3/100=0.03$. That tells us probability of flipping an unfair coin is around 0.97. 
# 
# If you are flipping an unfair coin well then probability of getting 5 head is 1. Now correct answer should be close to these numbers.

# In[1]:


1/32


# In[ ]:





# ### Theoritical result

# As you can guess we will use Bayes theorem here. 
# We will denote with $U$ letter if we are flipping the unfair coin and $F$ letter if we are flipping a fair
# Since we are picking randomly one coin, $\mathbb{P}(U)=\mathbb{P}(F)=1/2$.
# 
# Let 5H represent the case where we get 5 heads in a row.  Then  we want to find the probability that we are flipping the unfair coin, given that we saw 5 heads in a row.
# i.e. $\mathbb{P}(U|5H)$. 
# If we are given an unfair coin and then the probability of getting 5 heads in a row would be 1. i.e. $\mathbb{P}(5H|U)=1$. With the same logic if we have fair coin and then the probability of getting 5 heads in a row would be 1/32. i.e. $\mathbb{P}(5H|F)=\frac{1}{2^5}.$ We actually collected all the information we want. Now using Bayes rule we get
# \begin{equation}
# \mathbb{P}(U|5H)=\dfrac{\mathbb{P}(5H|U)\mathbb{P}(U)}{\mathbb{P}(5H|U)\mathbb{P}(U)+\mathbb{P}(5H|F)\mathbb{P}(F)}=\frac{\frac{1}{2}*1}{\frac{1}{2}*1+\frac{1}{2}*\frac{1}{2^5}}=\frac{32}{33}= 0.9696969696969697
# \end{equation}

# In[2]:


32/33


# ## Python code for our intuition

# In[3]:


import scipy.stats as stats
def fair(n_trials):
    return stats.bernoulli.rvs(0.5, size=n_trials) # this returns an array of 0s and 1s
def unfair(n_trials):
    return stats.bernoulli.rvs(1, size=n_trials) ## this returns an array of 1s


# In[4]:


import numpy as np
count_f=0
count_unf=0
for j in range(100):
    data = fair(5)
    if np.sum(data)==5:
        count_f+=1
for j in range(100):
    data = unfair(5)
    if np.sum(data)==5:
        count_unf+=1
    


# In[5]:


count_f/100,count_unf/10000


# In[ ]:




