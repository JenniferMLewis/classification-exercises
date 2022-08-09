import os
import pandas as pd
from env import user, password, host

def get_url(db, user=user, password=password, host=host):
    '''
    take database name for input,
    returns url, using user, password, and host pulled from your env file.
    PLEASE save it as a variable, and do NOT just print your credientials to your document.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''
    Returns the titanic dataset, checks local disk for titanic.csv, if present loads it, 
    otherwise it pulls the data from SQL and then saves it to local disk as 'titanic.csv'
    (This is set up for Codeup's SQL server, with database title 'titanic_db'.)
    '''
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('SELECT * FROM passengers', get_url('titanic_db'))
        df.to_csv(filename)
        return df 

def get_iris_data():
    '''
    Returns the iris dataset, checks local disk for iris.csv, if present loads it, 
    otherwise it pulls the data from SQL, joins species and measurements tables and then saves it to local disk as 'iris.csv'
    (This is set up for Codeup's SQL server, with database title 'iris_db'.)
    '''
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('''SELECT * FROM species
        LEFT JOIN measurements
        USING(species_id);''', get_url('iris_db'))
        df.to_csv(filename)
        return df 

def get_telco_data():
    '''
    Returns the telco dataset, checks local dist for telco.csv, if present loads it,
    otherwise it pulls the data from SQL, joins customer, contract_types, payment_types, internet_service_types, and customer_churn tables,
    the customer_churn has date of customer churn, as not all customers have churned, there WILL be Null Values that require tidying up, Please be aware.
    '''
    filename = 'telco_churn.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('''SELECT * FROM customers
        JOIN contract_types
        USING(contract_type_id)
        JOIN payment_types
        USING(payment_type_id)
        JOIN internet_service_types
        USING(internet_service_type_id)
        LEFT JOIN customer_churn
        USING(customer_id);''', get_url('telco_churn'))
        df.to_csv(filename)
        return df