# house_prices_linear_regression.py

"""
This script performs linear regression on a csv file to predict house prices.
It uses the scikit-learn library for the regression task and pandas for data manipulation.

Author: [Your Name]
Date: 27 March 2026
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from typing import Dict

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads the csv file into a pandas DataFrame.

    Args:
    - file_path (str): The path to the csv file.

    Returns:
    - pd.DataFrame: The loaded DataFrame.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        raise
    except pd.errors.EmptyDataError:
        print(f"File '{file_path}' is empty.")
        raise
    except pd.errors.ParserError:
        print(f"Error parsing file '{file_path}'.")
        raise


def prepare_data(data: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Prepares the data for the regression task.

    Args:
    - data (pd.DataFrame): The loaded DataFrame.

    Returns:
    - Dict[str, pd.DataFrame]: A dictionary with 'train_X', 'train_Y', 'test_X', and 'test_Y' DataFrames.
    """
    try:
        # Assuming 'price' is the target variable and other columns are features
        X = data.drop('price', axis=1)
        Y = data['price']

        # Split the data into train and test sets
        train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=42)

        return {
            'train_X': train_X,
            'train_Y': train_Y,
            'test_X': test_X,
            'test_Y': test_Y,
        }
    except KeyError:
        print("Target variable 'price' not found in the DataFrame.")
        raise


def perform_linear_regression(train_X: pd.DataFrame, train_Y: pd.Series, test_X: pd.DataFrame, test_Y: pd.Series) -> Dict[str, float]:
    """
    Performs linear regression on the prepared data.

    Args:
    - train_X (pd.DataFrame): The training feature data.
    - train_Y (pd.Series): The training target variable.
    - test_X (pd.DataFrame): The testing feature data.
    - test_Y (pd.Series): The testing target variable.

    Returns:
    - Dict[str, float]: A dictionary with 'MSE' and 'R2 Score' metrics.
    """
    try:
        model = LinearRegression()
        model.fit(train_X, train_Y)
        predictions = model.predict(test_X)

        mse = mean_squared_error(test_Y, predictions)
        r2 = r2_score(test_Y, predictions)

        return {
            'MSE': mse,
            'R2 Score': r2,
        }
    except Exception as e:
        print(f"Error performing linear regression: {e}")
        raise


def main():
    file_path = 'house_prices.csv'
    data = load_data(file_path)
    prepared_data = prepare_data(data)
    metrics = perform_linear_regression(prepared_data['train_X'], prepared_data['train_Y'], prepared_data['test_X'], prepared_data['test_Y'])

    print(f"Mean Squared Error (MSE): {metrics['MSE']}")
    print(f"R2 Score: {metrics['R2 Score']}")


if __name__ == "__main__":
    main()