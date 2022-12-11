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
    df = pd.read_csv(path, skiprows = 4)
    df.drop(['Indicator Code', 'Country Code', 'Unnamed: 66'], axis = 1, inplace = True)
    df_i = df.set_index(['Country Name', 'Indicator Name'])
    df_t = df_i.T
    return df, df_t


def bar_plot(data, indicator_name):
    """
    The goal of this function is to generate a bar plot of countries in a
    period of time.

    Args: 
        data : The dataframe table 
        indicator (str) : The column of intrest
    
    Return: 
        Bar chart 
    
    """
    data1 = data[data['Indicator Name']== indicator_name]
    data2 = data1.groupby(['Country Name'])['2018', '2019', '2020'].mean()[:10]
    data2.plot(kind = 'bar')
    plt.title('{} from 2018 till 2020'.format(indicator_name))