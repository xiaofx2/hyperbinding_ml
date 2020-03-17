#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("../..")


# In[7]:


from hyperbinding import peptide_cutter as pc


# In[15]:


def test_cutter():
    assert pc.cutter('AABBCC', 3) == ['AAB', 'ABB', 'BBC', 'BCC'], "Cutter function is wrong"


# In[ ]:




