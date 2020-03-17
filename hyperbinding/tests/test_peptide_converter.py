#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sys
sys.path.append("../..")


# In[30]:


from hyperbinding import peptide_converter as pc


# In[35]:


def test_peptide_converter():
    import os
    pc.peptide_converter('multi-Labeled-HLA-A-0201.csv')
    assert os.path.isfile('./Filled-multi-Labeled-HLA-A-0201.csv') == 1, 'File generation failed'


# In[ ]:




