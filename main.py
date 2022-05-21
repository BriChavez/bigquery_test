
import pandas as pd
from pandas import DataFrame

# import pandas and set pandas read_cvs to a variable
ufo_data = pd.read_csv('./data/nuforc_reports.csv', index_col = 'summary', header = 0)
df = pd.DataFrame(ufo_data)
# df.head()


"""start functions to clean data"""


def set_index(df,index = ['date_time']):
    """if our data doesnt already have one, this is a function to create an index"""
    df = df.set_index(index, inplace=False)
    

def fill_na(df):
    """check to see if there are any null values and changes them to NaN"""
    df.fillna(value="null", axis=1, inplace=True)


"""write the pandas df back to a csv"""
def write_csv(df):
    clean_UFO_data = './data/cleaned_UFO_data.csv'
    df.to_csv(clean_UFO_data)


"""write the run function and call it on out dataframe"""
def run(df):
    set_index(df)
    fill_na(df)
    write_csv(df)


run(ufo_data)

# print(df.head())
