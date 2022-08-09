# Running Notes:

# df.select_dtypes(include='number').columns
#    Pulls up all column names with int or float values. Nifty!

# pd.concat([df, dummy_df], axis=1)
#    Adds the data frames next to each other instead of creating new rows after the first dataframe's rows (and giving a bunch of null/nan)

import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data
from sklearn.model_selection import train_test_split

def prep_iris_data(df):
    '''
    For the Iris DB:
    Drops the Foreign Key Columns, renames 'species_name' to species, 
    then breaks the species into two dummy columns with int values.
    '''
    df = df.drop(columns=['species_id', 'measurement_id', 'Unnamed: 0']).rename(columns={'species_name' : 'species'})
    dummy_df = pd.get_dummies(df.species, drop_first=True)
    df = pd.concat([df,dummy_df], axis=1)
    return df

# def prep_titanic_data(df):
#    '''
#    The Ultimate Dishwasher
#    '''
#    df = clean_data(df)
#    train,validate,test