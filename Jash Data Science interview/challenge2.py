"""
Pandas programming task

1. Load the data into a Pandas dataframe
2. Remove records where scheme_code is NULL
3. Sort the data by nav_date
4. Fill Missing values in nav column by the last known value in the field after sorting by nav_date (Fill forward)
5. Save the output dataframe with the name pandas_challenge_output.csv
6. Send output file as well as the code in a zip file

Code evaluation criteria:
1. Correctness of the output file and code
2. Code should be clean and readable
3. optimal with respect to time and space complexity (e.g. avoid unnecessary extra variables and loops) 

"""

def process_df(input_csv):

    #TODO: implement your code here

    # loading pandas library
    import pandas as pd
    
    # 1. Load the data into a Pandas dataframe
    
    df = pd.read_csv(input_csv)

    # 2. Remove records where scheme_code is NULL
    
    df.dropna(subset=['scheme_code'], inplace=True)
    
    # 3. Sort the data by nav_date
    
    # first converting to datetime format 
    df['nav_date'] = pd.to_datetime(df['nav_date'])

    df.sort_values(by='nav_date', inplace=True)

    # 4. Fill Missing values in nav column by the last known value in the field after sorting by nav_date (Fill forward)
    
    df['nav'].ffill(axis=0, inplace=True)
    
    # 5. Save the output dataframe with the name pandas_challenge_output.csv

    df.to_csv('pandas_challenge_output.csv')
    
    
process_df('challenge2_input.csv')