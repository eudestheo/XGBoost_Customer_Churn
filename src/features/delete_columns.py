def delete_columns(df, columns_to_delete):
    """
    Delete specified columns from a DataFrame.

    Parameters:
    df (DataFrame): The input DataFrame from which columns will be deleted.
    columns_to_delete (list of str): A list of column names to be deleted from the DataFrame.

    Returns:
    DataFrame: A new DataFrame with the specified columns removed.
    """
    df = df.drop(columns=columns_to_delete)
    return df