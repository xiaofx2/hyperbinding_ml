#!/usr/bin/env python
# coding: utf-8

# In[22]:


import sys
sys.path.append("../..")


# In[29]:


from hyperbinding import Input_matrix_generation as img


# In[68]:


def test_create_input_matrix():
    import pandas as pd
    df = pd.read_csv('../../hyperbinding/data/Labeled-HLA-A-0201.csv')
    assert len(img.create_input_matrix(df.head(5))) == 5, "size of input matrix in wrong"


# In[49]:


def test_sequence_to_matrix():
    assert img.sequence_to_matrix('AAXAXAAAXXAA').shape == (5,12), "size of input matrix in wrong"


# In[37]:


def test_hydropathy():
    assert img.hydropathy('D') == -3.5, "Hygropathy of amino acid D is wrong"


# In[38]:


def test_sequence_to_num():
    assert img.sequence_to_num('K') == 9, "Index number of amino acid K is wrong"


# In[39]:


def test_volume():
    assert img.volume('T') == 116.1, "Volume of amino acid T is wrong"


# In[40]:


def test_polarity():
    assert img.polarity('A') == 1, "Polarity of amino acid A is wrong"


# In[41]:


def test_length():
    assert img.length('AAXAXAAAXXAA') == 8, "length of sequence is wrong"


# In[ ]:




