#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sys
sys.path.append("../..")


# In[23]:


from hyperbinding import multi_label_generator as mlg


# In[28]:


def test_multiple_lable_maker():
    import pandas as pd
    import os
    df = pd.read_csv('../../hyperbinding/data/Labeled-HLA-A-0201.csv')
    mlg.multiple_lable_maker(df)
    assert os.path.isfile('./multi-Labeled-HLA-A-0201.csv') == 1, 'File generation failed'


# In[29]:


test_multiple_lable_maker()


# In[ ]:




