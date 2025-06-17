#!/usr/bin/env python
# coding: utf-8

# In[59]:


gross_pay = 37771200
tax_rate = 0.173
expenses = 1000000

def savings(gross_pay, tax_rate, expenses):
    import math
    tax_amount = gross_pay * tax_rate
    net_savings = math.floor(gross_pay - tax_amount - expenses)
    return net_savings
print(savings(gross_pay, tax_rate, expenses))


# In[51]:


total_material = 100
material_units = "kg"
num_jobs = 4
job_consumption = 15

def material_waste(total_material, material_units, num_jobs, job_consumption):
    con = num_jobs * job_consumption
    ans = total_material - con 
    return str(ans) + material_units 
print (material_waste(total_material, material_units, num_jobs, job_consumption))


# In[54]:


principal = 10000
rate = 0.2
periods = 3

def interest(principal, rate, periods):
    import math
    ins = principal * rate * periods
    final = math.floor(principal + ins)
    return final
print(interest(principal, rate, periods))


# In[ ]:




