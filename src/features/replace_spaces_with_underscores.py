def replace_spaces_with_underscores(df, column_name=None):
    """
    Replace spaces with underscores in a specific column of a DataFrame or in
    column names.

    This function can be used in two ways:
    1. If `column_name` is provided, it replaces all spaces in the specified
       column with underscores using regular expressions.
    2. If `column_name` is not provided, it replaces all spaces in column names
       with underscores.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to be processed.
    - column_name (str, optional): The name of the column in `df` where spaces
      should be replaced. If not provided, spaces in column names will be replaced.

    Returns:
    - DataFrame: A new DataFrame with spaces replaced by underscores in
      the specified column or in column names.
    """
    if column_name is not None:
        df[column_name] = df[column_name].replace(' ', '_', regex=True)
    else:
        df.columns = df.columns.str.replace(' ', '_')
    return df