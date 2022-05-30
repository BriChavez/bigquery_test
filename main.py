
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
    """drop columns"""
    # drop columns in the dataframe we dont want to play with to make the file size smaller
    df.drop(columns = ['report_link', 'posted', 'city_latitude', 'city_longitude', 'stats'], inplace = True)

def fill_na(df):
    """fill empty/na values"""
    # check to see if there are any null values and changes them to a string
    df.fillna(value='null', inplace=True)

def drop_na(df):
    """drop rows where information is missing"""
    # drop entire row where the feild date_time is missing
    df.dropna(subset=['date_time'], inplace=True)
    # drop entire rows where there is less than 4 columns with values
    df.dropna(thresh =4, inplace= True)

def clean_index(df):
    """drop rows where the index is set to  an n/a string"""
    # use  drop to delete the rows where the date_time feild shows as our missing data string
    df.drop(index = ['null'], inplace = True)

def set_index(df):
    """set the index"""
    # use set_index to use the column date_time to be our index
    df = df.set_index(['date_time'], inplace=True)

def write_csv(df):
    """write the pandas df back to a csv"""
    # function to create a new csv file and write the cleaned up data to it
    clean_UFO_data = './data/cleaned_UFO_data.csv'
    df.to_csv(clean_UFO_data)

def run(df):
    """write the run function and call it on out dataframe"""
    drop_cols(df)
    fill_na(df)
    drop_na(df)
    set_index(df)
    clean_index(df)
    write_csv(df)


run(ufo_data)
"""call run function on our database"""