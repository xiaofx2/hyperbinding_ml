#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("../..")


# In[2]:


from hyperbinding import single_peptide_convert as spc


# In[5]:


def test_peptide_converter():
    assert len(spc.peptide_converter('CCAACC')) == 12, "length of sequence is wrong"


# In[ ]:




