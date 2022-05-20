
import pandas as pd
from pandas import DataFrame

# import pandas and set pandas read_cvs to a variable

ufo_data = pd.read_csv('./data/nuforc_reports.csv', index_col = 'summary')
df = pd.DataFrame(ufo_data)
# df = ufo_data
# df.head()

# # create empty variables so we know what internal variablesneed to define later
# col_list = []
# col_check = []


"""start functions to clean data"""


"""if our data doesnt already have one, this is a function to create an index from a later specified column"""
# def set_index(df,index):

#     """create the index by concatting two columns"""
#     # df[index_name] = df[col_list]
#     # .apply(
#     # lambda row: "-".join(row.values.astype(str)), axis=1)
#     # index=df["date_time"]
#     df = df.set_index(index, inplace=True)
    


def fill_na(df):
    """check to see if there are any null values and changes them to NaN"""
    df.fillna(value="null", axis=1, inplace=True)


# def drop_dupes(df, col_check=None):
#     """drop duplicates among the specified col to ensure the data isnt repeated"""
#     df.drop_duplicates(subset=[col_check], inplace=True)


"""write the pandas df back to a csv"""


def write_csv(df):
    clean_UFO_data = './data/cleaned_UFO_data.csv'
    df.to_csv(clean_UFO_data)


"""run function to enact our functions on our ufo dataframe"""
# df = ufo_data
# col_check = df.summary

# df['date_time'] = pd.to_datetime(df['date_time'], format="%Y-%m-%d")
# col_list = [df.date_time]


def run(df):
    # set_index(df)
    fill_na(df)
    # drop_dupes(df)
    write_csv(df)


run(ufo_data)

# print(df.head())
