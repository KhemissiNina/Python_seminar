#!/usr/bin/env python
# coding: utf-8

# # f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10*x - 30
# Определить корни
# 
# Найти интервалы, на которых функция возрастает
# 
# Найти интервалы, на которых функция убывает
# 
# Построить график
# 
# Вычислить вершину
# 
# Определить промежутки, на котором f > 0
# 
# Определить промежутки, на котором f < 0
# 
# *math.sin(math.cos(x)
# 

# In[118]:


import numpy as np
import matplotlib.pyplot as plt


# In[119]:


a=-12
b=-18
c=5
d=10
e=-30


# In[120]:


def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3+c*x**2 + d*x + e


# In[121]:


limit=10
step=0.01
step_acr=0.0000001
line_style='-'
color='b'
direct_up=True


# In[122]:


def line_swith():
    global line_style
    if line_style=="-":
        line_style='--'
    else:
        line_style='-'
    return line_style


# In[123]:


def color_swith():
    global color
    if color=="b":
        color='r'
    else:
        color='b'
    return color


# In[124]:


x=np.arange(-limit,limit+step,step)


# In[103]:


'''
def take_root(a,b,c,d,e):
    roots=[]
    while True:
        a*x**4*np.sin(np.cos(x)) + b*x**3+c*x**2 + d*x + e=0
        roots.append(x)
        print(roots)
'''    


# In[125]:


x_change=[(-limit,'limit')]
for i in range(len(x)-1):
    if func(x[i])>0 and func(x[i+1])<0 or func(x[i])<0 and func(x[i+1])>0:
        x_acr=np.arange(x[i],x[i+1]+step_acr,step_acr)
        for j in range(len(x_acr)-1):
            if func(x_acr[j])>0 and func(x_acr[j+1])<0 or func(x_acr[j])<0 and func(x_acr[j+1])>0:
                x_change.append((x_acr[j],'zero'))
        
        
        x_change.append((x[i],'zero'))
    if direct_up:
        if func(x[i])>func(x[i+1]):
            direct_up=False
            x_change.append((x[i],'dir'))
    else:
        if func(x[i])<func(x[i+1]):
            direct_up=True
            x_change.append((x[i],'dir'))
            
x_change.append((limit,"limit"))


# In[126]:


for i in range(len(x_change)-1):
    cur_x=np.arange(x_change[i][0],x_change[i+1][0]+step, step)
    if x_change[i][1]=='zero':
        plt.plot(x_change[i][0],func(x_change[i][0]), 'go')
        plt.rcParams['lines.linestyle']=line_swith()
        plt.plot(cur_x,func(cur_x), color)
    else:
        plt.plot(cur_x,func(cur_x), color_swith())
    
plt.grid()
plt.show
