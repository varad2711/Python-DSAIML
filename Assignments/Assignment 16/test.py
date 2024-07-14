import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 


def LinearRegressionSales():
    data = pd.read_csv('Advertising.csv')
    print("Dataset:\n", data.head())

    Features = data.drop('sales', axis=1)
    Labels = data['sales']
    
    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, test_size=0.3, random_state=42)
    
    data_train = np.hstack((np.ones((data_train.shape[0], 1)), data_train))
    data_test = np.hstack((np.ones((data_test.shape[0], 1)), data_test))
    
    X_transpose = data_train.T
    coefficients = np.linalg.inv(X_transpose.dot(data_train)).dot(X_transpose).dot(target_train)
    
    intercept = coefficients[0]
    slopes = coefficients[1:]
    
    print("Intercept (b_0):", intercept)
    print("Slopes (b_1, b_2, ...):", slopes)
    
    predictions = data_test.dot(coefficients)
    
    ss_total = sum((target_test - np.mean(target_test)) ** 2)
    ss_residual = sum((target_test - predictions) ** 2)
    r2_test = 1 - (ss_residual / ss_total)
    print(f"R-squared value on the test set: {r2_test:.2f}")

    X = np.hstack((np.ones((Features.shape[0], 1)), Features))
    overall_predictions = X.dot(coefficients)
    ss_total_overall = sum((Labels - np.mean(Labels)) ** 2)
    ss_residual_overall = sum((Labels - overall_predictions) ** 2)
    r2_overall = 1 - (ss_residual_overall / ss_total_overall)
    print(f"R-squared value for the entire dataset: {r2_overall:.2f}")

def main():
    LinearRegressionSales()

if __name__ == "__main__":
    main()
