import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import matplotlib.patches as mpatches

def file_reader(path):
    """
    This function  read csv file and returns two dataframe i.e. a normal 
    dataframe and a transposed dataframe 
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
    it generates a bar plot of countries in a period of time.

    Args: 
        data : The dataframe table 
        indicator (str) : The name of indicator from the indicator column
    
    Return: 
        Bar chart 
    
    """
    data1 = data[data['Indicator Name']== indicator_name]
    data2 = data1.groupby(['Country Name'])['2018', '2019', '2020'].mean()[-10:]
    data2.plot(kind = 'bar')
    plt.title('{} from 2018 till 2020'.format(indicator_name))


def line_plot(data, indicator_name, country1, country2):
    """
    it generate a line plot of two countries over a period of time 
    for a particular indicator.

    Args: 
        data : The dataframe table 
        indicator_name (str) : The name of te indicator from the indicator column.
        country1 : First country of interest
        country2 :  Second country of interest
    
    Return: 
        Line plot  
    """
    df_2 = data[data['Indicator Name']== indicator_name]
    df_2 = df_2.groupby(['Country Name']).sum()
    df_2_t = df_2.T
    df_2_t = df_2_t[[country1, country2]][-10:]
    plt.figure(figsize = (10, 10))
    df_2_t.plot()
    countrya = mpatches.Patch(color='blue', label='{}'.format(country1))
    countryb = mpatches.Patch(color='orange', label='{}'.format(country2))
    plt.xticks(rotation = 90)
    plt.title('{} trend between{} and {}'.format(indicator_name, country1, country2))
    plt.legend(handles=[country1, country2])
    plt.show()

def country_correlation(data, country_name, cmap="crest"): 
    """
    It generate an heatmap that shows the correlations of indicators 
    for a particular country.

    Args: 
        data : Table
        country_name (str): The country of interests.
        cmap (str, optional) :  The type of color pallete to match our visulaization. 

    Return : 
        Heatmap  
    
    """
    country = data[country_name]
    cols = []
    for x in data[country_name].columns:
        cols.append(x)
    tbl_1 = data[country_name]
    tbl = tbl_1[cols].iloc[:, :12]
    sns.heatmap(tbl.corr(), cmap)
    plt.title('{}'.format(country_name))
    plt.legend([], frameon=False)
    plt.show()