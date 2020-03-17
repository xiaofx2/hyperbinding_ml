#!/usr/bin/env python
# coding: utf-8

# In[54]:


import sys
sys.path.append("../..")


# In[55]:


from hyperbinding import multiple_channel_matrix_generator as mcm


# In[56]:


def test_multiple_channel_generator():
    assert len(mcm.multiple_channel_generator('AACC')) == 3, "dimension of matrix is wrong"
    assert mcm.multiple_channel_generator('AACC').size == 756, 'size of matrix is wrong'


# In[57]:


def test_basic_matrix_generator():
    assert len(mcm.basic_matrix_generator('AACC')) == 21, 'length of basic matrix is wrong'


# In[58]:


def test_vol_channel_generator():
    assert mcm.vol_channel_generator('AACC').size == 252, 'size of vol channel is wrong'


# In[59]:


def test_polar_channel_generator():
    assert mcm.polar_channel_generator('AACC').size == 252, 'size of polar channel is wrong'


# In[60]:


def test_hydropathy_channel_generator():
    assert mcm.hydropathy_channel_generator('AACC').size == 252, 'size of hydropathy channel is wrong'


# In[ ]:




