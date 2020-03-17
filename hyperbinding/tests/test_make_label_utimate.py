#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sys
sys.path.append("../..")


# In[37]:


from hyperbinding import make_label_utimate as mlu


# In[38]:


def test_label_marker():
    import os
    mlu.label_marker('multi-Labeled-HLA-A-0201.csv')
    assert os.path.isfile('./Labeled-HLA-A-0201.csv') == 1, 'File generation failed'


# In[ ]:




