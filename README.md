# What is Hyperbinding?

   Hyperbinding is a MHC ligand prediction python package using machine learning approach to generate high-confidence peptides by considering the presentation possibilities of peptides with MHC molecules. MHC-peptide binding prediction plays an important role in cancer immunoengineering, T cell therapy and vaccine design. A simplified immune recognition process invloves the binding of a short peptide with antigen presenting cells, where the peptide comes from cancer neoantigen or virus antigen. Higher binding affinity between MHC and the peptide will allow the MHC-peptide complex to be recognized by T cells and thus elicit immune cascade in eliminating the pathogen.
   The current release was trained using only data from HLA-A02:01, which is one of the most abundant alleles in Class I human MHC molecule. Currently, the training and testing support peptides ranging from 8 to 12 amino acids in length, but the model can be re-trained to support more alleles and wider ranges of peptide length.  The further application of Hyperbinding can be extended into different Class I MHC alleles, and broad categories of disease-related peptides.

   
   

# Download and installation

We recommond using Git to install the Hyperbinding.


## Git (All the dependencies should be properly installed)

### System
Linux

### Dependencies
perl    
python    

### Steps

Download the latest version of Hyperbinding from https://github.com/UWDIRECT/HyperBinding
    
    git clone https://github.com/UWDIRECT/HyperBinding.git
    
Unzip the source code and go into the directory by using the following command:

    tar xvzf deephlapan-*.tar.gz

    cd deephlapan

Invoke the setup script:

    sudo python setup.py install


# General usage

 
 
    
    
    
# Application usage example    

Following CDC updates for COVID-19:
https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/summary.html

Updated on Mar.15 2020, CDC is responding to an outbreak of respiratory disease caused by a novel coronavirus which has now been detected in more than 100 locations internationally, including in the United States. The virus has been named “SARS-CoV-2” and the disease it causes has been named “coronavirus disease 2019” (abbreviated “COVID-19”). 

The prediction of peptide-MHC binding affinity has rapidly accelerating the development of vaccines and adoptive T-cell therapies targeting virus. Rick is an Bioengineer working on T cell engineering and immunotherapy. His lab is supporting the research on COVID-19 by designing high-throughput capture reagents to select and isolate T cells with potent immunity in recognizing and eliminating the virus. Then the isolated T cells will be sequenced and amplified, and transfered back to patients to boost patient's immune system against the virus. 

To design the high-throughput capture reagents 

We can help you slice your protein sequence into fragments with desirable length and predicate their binding affinity to HLA-A-02.  

    cd HyperBinding/examples/prediction/
    jupyter notebook main_binding_predictor.ipynb 


## Input files

Hyperbinding takes **csv** files as input with head of **"Annotation,HLA,peptide"** (requisite).    
It supports to rank the HLA-peptide pairs if all the mutant peptides belong to one sample. 

For example (demo/1.csv):
    
      Annotation,HLA,peptide
      NCI-3784,HLA-A01:01,MKRFVQWL
      NCI-3784,HLA-A03:01,MKRFVQWL
      NCI-3784,HLA-B07:02,MKRFVQWL
      NCI-3784,HLA-B07:02,MKRFVQWL
      NCI-3784,HLA-C07:02,MKRFVQWL
      NCI-3784,HLA-C07:02,MKRFVQWL
      NCI-3784,HLA-A01:01,KRFVQWLK
      NCI-3784,HLA-A03:01,KRFVQWLK
      NCI-3784,HLA-B07:02,KRFVQWLK
      NCI-3784,HLA-B07:02,KRFVQWLK
      NCI-3784,HLA-C07:02,KRFVQWLK
      NCI-3784,HLA-C07:02,KRFVQWLK
 
 The content in Annotation can be changed as users wanted.
 
 
 # Update log
 ## 2019.12
 V1.1.1    
 Improve the prediction speed
 ## 2019.03
 V1.1    
 Add the function of immunogeneicity prediction
 
 ## 2018.07
 V1.0    
 Test the suitabilty of different RNN variants (GRU,LSTM,BGRU,BLSTM,att-BGRU and att-BLSTM) on the binding prediction and select the best (att-BGRU) one for model construction.
 
