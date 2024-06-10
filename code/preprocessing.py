import pandas as pd

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
