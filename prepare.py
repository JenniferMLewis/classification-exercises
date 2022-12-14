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
    then breaks the species into dummy columns with int values.
    returns the Data Frame cleaned up
    '''
    df = df.drop(columns=['species_id', 'measurement_id', 'Unnamed: 0']).rename(columns={'species_name' : 'species'})
    dummy_df = pd.get_dummies(df.species, drop_first=True)
    df = pd.concat([df,dummy_df], axis=1)
    return df


def prep_titanic(df):
    '''
    For the Titanic DB:
    Drops the pasenger_id, embarked, class, age, and deck Columns, renames 'embark_town' to 'embarked' and 'pclass' to 'passenger_class', 
    Renames the index to passenger_id, since they are the same values, we don't need duplicates.
    Combines 'sibsp' and 'parch' into the column 'family' then dropos 'sibsp' and 'parch'
    then breaks 'sex' and 'embarked' into dummy columns with int values.
    Returns the Data Frame cleaned up
    '''
    df['family'] = df.sibsp + df.parch
    df = df.drop(columns=["parch", "sibsp"])
    dummy_df = pd.get_dummies(data=df[['sex','embark_town']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    df = df.drop(columns=['embarked', 'sex', 'embark_town','class', 'age','deck', 'Unnamed: 0', 'passenger_id'])
    df.index.names=["passenger_id"]

    return df


def prep_telco(df):
    '''
    For the Telco DB:
    Drops the Foreign Key Columns: 'internet_service_type_id', 'contract_type_id', and 'payment_type_id', 
    Maps 'gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', and 'churn' into columns with int values (Female and Yes mapped as 1, Male and No mapped to 0).
    Creates Dummy Columns for 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type',  'payment_type'
    Returns the Data Frame cleaned up
    '''
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(df[['multiple_lines',
                              'online_security',
                              'online_backup',
                              'device_protection',
                              'tech_support',
                              'streaming_tv',
                              'streaming_movies',
                              'contract_type',
                              'internet_service_type',
                              'payment_type'
                            ]],
                              drop_first=True)
    df = pd.concat( [df, dummy_df], axis=1 )
    df = df.drop(columns={'Unnamed: 0', 'customer_id', 'gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'payment_type', 'internet_service_type', 'churn_month'})

    return df

def data_split(df, target):
    '''
    take in a DataFrame and target.
    return train, validate, test DataFrames.
    '''
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    
    return train, validate, test

def prep_titanic_age(df):
    '''
    For the Titanic DB:
    Drops the pasenger_id, embarked, class, and deck Columns, renames 'embark_town' to 'embarked' and 'pclass' to 'passenger_class', 
    Renames the index to passenger_id, since they are the same values, we don't need duplicates.
    Combines 'sibsp' and 'parch' into the column 'family' then dropos 'sibsp' and 'parch'
    then breaks 'sex' and 'embarked' into dummy columns with int values. Lastly, fills in all NaN in 'age' with the rounded (because all ages are xx.0, may remove round() dependant upon how it affects data) mean of known ages.
    Returns the Data Frame cleaned up
    '''
    df['family'] = df.sibsp + df.parch
    df = df.drop(columns=["parch", "sibsp"])
    dummy_df = pd.get_dummies(data=df[['sex','embark_town']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    df = df.drop(columns=['embarked', 'sex', 'embark_town','class','deck', 'Unnamed: 0', 'passenger_id'])
    df.index.names=["passenger_id"]
    df.age.fillna(round(df.age.mean()), inplace=True) # rounded since all ages are xx.0

    return df