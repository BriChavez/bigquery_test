
import pandas as pd
from pandas import DataFrame

# import pandas and set pandas read_cvs to a variable
ufo_data = pd.read_csv('./data/complete.csv')
df = pd.DataFrame(ufo_data)
# df.head()


"""start functions to clean data"""

# def set_header(df):
#     header_row = df.iloc[1]
#     df = df.values[1:]
    

def set_index(df):
    """if our data doesnt already have one, this is a function to create an index"""
    df = df.set_index('datetime')


def fill_na(df):
    """check to see if there are any null values and changes them to NaN"""
    df.fillna(value="null", inplace=True)


def write_csv(df):
    """write the pandas df back to a csv"""
    clean_UFO_data = './data/cleaned_UFO_data.csv'
    df.to_csv(clean_UFO_data)

def run(df):
    """write the run function and call it on out dataframe"""
    # set_header(df)
    set_index(df)
    fill_na(df)
    write_csv(df)


run(ufo_data)
"""call run function on our database"""