
import pandas as pd
from pandas import DataFrame


"""import pandas and set pandas read_cvs to a variable"""
ufo_data = pd.read_csv('./data/nuforc_reports.csv',
                    #    use the names paramater to assign header as the names of the columns
                       names=['summary', 'city', 'state', 'date_time', 
                            'shape', 'duration', 'stats', 'report_link', 
                            'text', 'posted', 'city_latitude', 'city_longitude'],
                    #    set header to 0 in order to override a header if it was included
                        header = 0,
                    #    help pandas read the datetime type files as date times by employing the paramater parse dates
                       parse_dates = ['date_time', 'posted']
                       )

"""turn the csv to a pandas dataframe"""
df = pd.DataFrame(ufo_data)

"""start functions to help clean the dataframe"""

def drop_cols(df):
    """drop columns that we dont want to play with to make the file size smaller"""
    df.drop(columns = ['report_link', 'posted', 'city_latitude', 'city_longitude', 'stats', 'text'], inplace = True)

def fill_na(df):
    """check to see if there are any null values and changes them to NaN"""
    df.fillna(value="N/A", inplace=True)

def drop_na(df):
    """drop rows where information is missing"""
    # drop entire row where the feild date_time is missing
    df.dropna(subset = ['date_time'], how = 'all', inplace = True)
    # drop entire rows where there is less than 4 columns with values
    df.dropna(thresh =4, inplace= True)


def set_index(df):
    """if our data doesnt already have one, this is a function to create an index"""
    df = df.set_index(['date_time'], inplace=True)

def write_csv(df):
    """write the pandas df back to a csv"""
    clean_UFO_data = './data/cleaned_UFO_data.csv'
    df.to_csv(clean_UFO_data)

def run(df):
    """write the run function and call it on out dataframe"""
    drop_cols(df)
    fill_na(df)
    drop_na(df)
    set_index(df)   
    write_csv(df)


run(ufo_data)
"""call run function on our database"""