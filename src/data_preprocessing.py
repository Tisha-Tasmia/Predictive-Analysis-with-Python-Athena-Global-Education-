
def load_data(filename):
    """Loads data from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded data.
    """
    return pd.read_csv(filename)

def clean_data(df):
    """Cleans the data by handling missing values and outliers.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    # Handle missing values (example: impute with mean)
    df = df.fillna(df.mean()) 

    # Handle outliers (example: remove values beyond 3 standard deviations)
    df = df[np.abs(df - df.mean()) <= (3 * df.std())]

    return df

def feature_engineering(df):
    """Performs feature engineering to extract relevant information.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.DataFrame: The DataFrame with engineered features.
    """
    # Example: Create a new feature based on existing features
    df['new_feature'] = df['feature1'] + df['feature2'] 

    return df
