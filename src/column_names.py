import pandas as pd
import re

def stardard_col_names(df):
    """
    This function helps to standardize the dataframe column names to snake_case.
    """
    new_col_name = []

    for old_name in df.columns:
        # Here we apply snake_case 
        
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', old_name.strip()).lower()
        name = name.replace(' ', '_')
        new_col_name.append(name)
   
    df.columns = new_col_name
    return df