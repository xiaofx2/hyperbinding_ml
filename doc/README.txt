For First time user, Please read READM.md file to get fimilarization.
Run setup.py to build up required environment. Before use hyperbinding.

Hyperbinding takes peptide sequences from user and will convert it into 
one or three channel based matrix. For details on algorithm, please refer 
to individual .py files in hyperbinding folder. 
Matrix is then used as input to train convolution neural network(CNN). For
CNN architicture, please refer to eamples/model_fitting. 

For single peptide MHC binding affinity prediction, hyperbinding works for 
ones whose length is shorter than 12. User can go to examples/prediction/
main_binary_prediction.ipynb or main_multi_prediction.ipynb and follow 
guidance in the file.

To find out potential binding fragments in a protein sequence, use can go to 
examples/prediction/main_binding_predictor.ipynb and follow guidance in 
the file. 