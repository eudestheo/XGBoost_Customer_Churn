def replace_empty_cells_with_value(df, column_name, replacement_value):
    """
    Replace empty cells in a specific column of a DataFrame with a specified value.

    Parameters:
    - df: The DataFrame to be processed.
    - column_name (str): The name of the column in `df` where empty cells should be replaced.
    - replacement_value: The value to replace empty cells with.

    Returns:
    - pandas.DataFrame: A new DataFrame with empty cells replaced by the specified value in
      the specified column.
    """
    df[column_name] = np.where(df[column_name] == ' ', replacement_value, df[column_name])
    return df