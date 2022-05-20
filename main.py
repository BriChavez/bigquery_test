
import pandas as pd

# import pandas and set pandas read_cvs to a variable
ufo_data =pd.read_csv('./data/nuforc_reports.csv')
# ufo_data.head()
df = ufo_data
df.shape

"""start functions to clean data"""
def fill_na(df):
    """check to see if there are any null values and changes them to NaN"""
    df.fillna(value = "null", axis = 1, inplace = True)


def drop_dupes(dataframe, col_check=None):
    """drop duplicates among the summaries to ensure the data isnt repeated"""
    df.drop_duplicates(subset=[col_check], inplace=True)


# if our data doesnt already have one, this is a function to create an index from a later specified column
"""create the index"""

def add_index(self, col_list, index_name="index"):
    df = self.df
    """create the index by concatting two columns"""
    df[index_name] = df[col_list].apply(lambda row: "-".join(row.values.astype(str)), axis=1)
    df = df.set_index(index_name, inplace=True)
    self.df = df


"""write the pandas df back to a csv"""
def write_csv(df):
    clean_UFO_data = (f'./data/cleaned_UFO_data.csv')
    df.to_csv(clean_UFO_data)