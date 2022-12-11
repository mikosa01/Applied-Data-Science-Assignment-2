import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import matplotlib.patches as mpatches

def file_reader(path):
    """
    This goal of this function is to read csv file and returns two dataframe. 
    Args: 
        path (str) : This is csv file path
        
    Return : 
        This function return an original dataframe(df) and a transposed dataframe(df_t).
    """
    df = pd.read_csv(path, skiprows = 4, index_col = [])
    df.drop(['Indicator Code', 'Country Code', 'Unnamed: 66'], axis = 1, inplace = True)
    df_i = df.set_index(['Country Name', 'Indicator Name'])
    df_t = df_i.T
    return df, df_t