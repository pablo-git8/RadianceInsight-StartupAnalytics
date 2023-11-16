# Imports
import pandas as pd
from datetime import timedelta
import json

# Helper functions and variables created for the project
from helper_functions import create_bucket_df
import helper_variables


def process_unknowns(df:pd.DataFrame, cols:list) -> pd.DataFrame:
    '''
    '''
    for col in cols:
        df[col] = df[col].fillna('Unknown')
    
    return df


def process_last_funding(df: pd.DataFrame, col:str) -> pd.DataFrame:
    '''
    '''
    # Processing 'last_funding_at' variable
    df[col] = pd.to_datetime(df[col])
    condition = df[col] > '2023-01-01'
    df.loc[condition, col] = '2015-07-01'

    return df


def process_first_funding(df:pd.DataFrame, col:str) -> pd.DataFrame:
    '''
    '''
    # Processing 'first_funding_at' variable
    date_condition = df[col].isnull()
    days_to_substract = helper_variables.avg_day_per_round
    df.loc[date_condition, col] = df.loc[date_condition, 'last_funding_at'] - timedelta(days=days_to_substract) * df['funding_rounds']  

    return df


def process_founding(df:pd.DataFrame, col:str) -> pd.DataFrame:
    '''
    '''
    # Processing 'founded_at' variable
    df[col] = pd.to_datetime(df[col], errors='coerce')
    days_to_substract_founded = helper_variables.avg_days_first_founded
    date_condition = df[col].isnull()
    df.loc[date_condition, col] = df.loc[date_condition, 'first_funding_at'] - timedelta(days=days_to_substract_founded) 
    # Condition: Replace 'last_funding_at' where it's greater than '2023-01-01'
    condition_1 = df[col] == '2041-09-21'
    # Replace values that meet the condition
    df.loc[condition_1, col] = '2014-09-21'
    # Condition: Replace 'last_funding_at' where it's greater than '2023-01-01'
    condition_2 = df[col] == '2104-01-01'
    # Replace values that meet the condition
    df.loc[condition_2, col] = '2014-01-01'
    # Condition: Replace 'last_funding_at' where it's greater than '2023-01-01'
    condition_3 = df[col] == '2105-02-17'
    # Replace values that meet the condition
    df.loc[condition_3, col] = '2015-02-17'

    return df

def process_categories(df:pd.DataFrame, col:str) -> pd.DataFrame:
    '''
    '''
    # Processing 'category_list' variable
    df[col] = df[col].fillna('Not Specified')
    category_stack_series = df[col].str.split('|', expand=True).stack()
    category_one_hot_encoded = pd.get_dummies(category_stack_series, prefix=None).groupby(level=0).sum()
    cat_df = df.join(category_one_hot_encoded)
    categories = cat_df.columns[14:]
    file_path = "category_buckets.json"
    with open(file_path, "r") as file:
        categories_dictionary = json.load(file)
    bucket_df = create_bucket_df(cat_df, categories_dictionary)
    df = bucket_df.drop(columns=['category_list'])

    return df


if __name__ == '__main__':

    # Loading the dataset from source
    url = 'https://raw.githubusercontent.com/notpeter/crunchbase-data/master/companies.csv'
    df = pd.read_csv(url)

    # Creating the JSON file for bucketing and loading it to the directory
    filename = 'category_bucket_creation.py'
    with open(filename, 'r') as file:
        exec(file.read())

    # Processing 'Name' variable
    df['name'] = df['name'].fillna("TellItIn")

    # Processing 'funding_total_usd' variable
    df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'].replace('-', 0))

    # Processing 'homepage_url', 'country_code', 'state_code',  'region' and 'city' variables
    df = process_unknowns(df, ['homepage_url', 'country_code', 'state_code', 'region', 'city'])

    # Processing 'last_funding_at' variable
    df = process_last_funding(df, 'last_funding_at')

    # Processing 'first_funding_at' variable
    df = process_first_funding(df, 'first_funding_at')

    # Processing 'founded_at' variable
    df = process_founding(df, 'founded_at')

    # Processing 'category_list' variable
    df = process_categories(df, 'category_list')

    # Saving startups processed DataFrame to CSV file
    df.to_csv('start_up_processed_data.csv')

    # Saving startups processed DataFrame to JSON file
    df_json = df.to_json()
    with open('data/startup_processed_data.json', 'w') as file:
        json.dump(df_json, file)
