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
        This function return an original dataframe(df) and 
        a transposed dataframe(df_t).
    """
    df = pd.read_csv(path, skiprows = 4)
    df.drop(['Indicator Code', 'Country Code', 'Unnamed: 66'], axis = 1, 
            inplace = True)
    df_i = df.set_index(['Country Name', 'Indicator Name'])
    df_t = df_i.T
    return df, df_t


def bar_plot(data, indicator_name_1, indicator_name_2):
    """
    it generates a bar plot of countries in a period of time.

    Args: 
        data : The dataframe table 
        indicator (str) : The name of indicator from the indicator column
    
    Return: 
        Bar chart 
    
    """
    indicators = [indicator_name_1, indicator_name_2]
    for indicator in indicators: 
        data1 = data[data['Indicator Name']== indicator]
        data1.loc[(data1['Country Name']=="Nigeria"), 'Africa'] = "Nigeria"
        data1.loc[(data1['Country Name']=="Zambia"), 'Africa'] = "Zambia"
        data1.loc[(data1['Country Name']=="Zimbabwe"), 'Africa'] = "Zimbabwe"
        data2 = data1.groupby(['Africa'])['2018', '2019', '2020'].mean()
        data2.plot(kind = 'bar')
        plt.title('{} from 2018 till 2020'.format(indicator))


def line_plot(data, indicator_name_1, indicator_name_2, country1, 
              country2, country3):
    """
    it generate a line plot of three countries over a period of time 
    for a particular indicator.

    Args: 
        data : The dataframe table 
        indicator_name_1 (str) : The name of the frst indicator from the 
                                indicator column.
        indicator_name_2 (str) : The name of the second indicator from the 
                                indicator column.
        country1 : First country of interest
        country2 :  Second country of interest
        country3 :  Third country of interest
    
    Return: 
        Line plot  
    """
    indicators = [indicator_name_1, indicator_name_2]
    for indicator in indicators: 
        df_2 = data[data['Indicator Name']== indicator]
        df_2 = df_2.groupby(['Country Name']).sum()
        df_2_t = df_2.T
        df_2_t = df_2_t[[country1, country2,  country3]][-10:]
        plt.figure(figsize = (10, 10))
        df_2_t.plot()
        countrya = mpatches.Patch(color='blue', label='{}'.format(country1))
        countryb = mpatches.Patch(color='orange', label='{}'.format(country2))
        countryc = mpatches.Patch(color = 'green', label = '{}'.format(country3))
        plt.xticks(rotation = 90)
        plt.title('{} trend between {}, {} and {}'.format(indicator, country1, 
                                                     country2, country3))
        plt.legend(handles=[countrya, countryb, countryc])
        plt.show()

def country_correlation(data, country_1, country_2, country_3): 
    """
    It generate an heatmap that shows the correlations of indicators 
    for three countries.

    Args: 
        data : Table
        country_1 (str): The first country of interests.
        country_2 (str): The second country of interests.
        country_3 (str): The third country of interests.
        

    Return : 
        Heatmap  
    
    """
    countries = [country_1, country_2, country_3]
    #cmaps = ["coolwarm", "PiYG", "BuPu"]
    for country in countries: 
        place = data[country]
        cols = []
        for x in place.columns:
            cols.append(x)
        tbl = place[cols].iloc[:, :7]
        for cmap in ["coolwarm", "PiYG", "BuPu"]: 
            sns.heatmap(tbl.corr(), cmap = cmap, annot = True)
            plt.title('{}'.format(country))
            plt.legend([], frameon=False)
            plt.show()