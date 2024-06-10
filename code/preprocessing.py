import pandas as pd

def remove_floating_points_in_postcodes(df: pd.DataFrame, postcode_column: str = 'postcode') -> pd.DataFrame:
    """
    Removes trailing decimal points (".0") from postcode values in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the 'postcode' column.
        postcode_column (str, optional): The name of the column containing postcodes. Defaults to 'postcode'.

    Returns:
        pd.DataFrame: A new DataFrame with ".0" removed from postcode values.
    """

    # Check if data type is object
    if df[postcode_column].dtype != 'object':
        print(f"Postcode column '{postcode_column}' is not of object type, skipping formatting.")
        return df
    
    df_clean = df.copy()
    df_clean[postcode_column] = df_clean[postcode_column].apply(lambda x: x.strip('.0'))
    return df_clean

def check_postcodes(df: pd.DataFrame, postcode_column: str = 'postcode'):
    """
    This function checks if the 'postcode' column in a DataFrame contains non-numeric values or
    has only 5 digit values.

    Args:
        df (pandas.DataFrame): The DataFrame containing the 'postcode' column.
        postcode_column (str, optional): The name of the column containing postcodes. Defaults to 'postcode'.
    """

    # Check if data type is object
    if df[postcode_column].dtype != 'object':
        print(f"Postcode column '{postcode_column}' is not of object type, skipping check.")
        return df

    # Filter for non-numeric values
    non_numeric_postcodes = ~df[postcode_column].str.isnumeric()

    # Filter for invalid lengths (not 5 digits)
    invalid_length = df[postcode_column].str.len() != 5

    # Print informative messages
    if non_numeric_postcodes.any():
        print(f"Found {non_numeric_postcodes.sum()} postcodes with non-numeric values in column '{postcode_column}'.")
    else:
        print(f"All postcodes n column '{postcode_column}' are numeric.")
    if non_numeric_postcodes.sum() < 10:
        print(df.loc[non_numeric_postcodes, postcode_column])

    if invalid_length.any():
        print(f"Found {invalid_length.sum()} postcodes with invalid length (not 5 digits) in column '{postcode_column}'.")
    else:
        print(f"All postcodes in column '{postcode_column}' have valid length (5 digits).")


def convert_order_date_to_datetime(df: pd.DataFrame, order_date_column: str = 'order_date') -> pd.DataFrame:
    """
    Converts the 'order_date' column in a DataFrame to datetime format.

    This function assumes the 'order_date' column contains date strings in a format that can be parsed by pandas.to_datetime.

    Args:
        df (pd.DataFrame): The DataFrame containing the 'order_date' column.
        order_date_column (str, optional): The name of the column containing order dates. Defaults to 'order_date'.

    Returns:
        pd.DataFrame: A new DataFrame with the 'order_date' column converted to datetime format.
    """
    
    # Check if data type is object
    if df[order_date_column].dtype != 'object':
        print(f"Order date column '{order_date_column}' is not of object type, skipping conversion.")
        return df
    
    df_clean = df.copy()
    df_clean['order_date'] = pd.to_datetime(df_clean['order_date'])
    return df_clean