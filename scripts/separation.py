### 
# This is the code within the EasyMicrobiome package for the separation visualization for either 16S data or more
###
from sklearn.decomposition import PCA
import pandas as pd
def EMcluster(df:pd.DataFrame,methodology:str):
    """
    df :: dataframe n x d
    method :: str, PCA/NMDS ( nonmetric multi-dimensional/TSNE/UMAP
scaling)
    
    """
    n, d  = df.shape
    pca = PCA(n_components=2)
