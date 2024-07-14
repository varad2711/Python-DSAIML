import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousMultiLinearPredictor():
    data = pd.read_csv('Advertising.csv')
    X = data.drop('sales',axis=1)
    y = data['sales']


    X = np.hstack((np.ones((X.shape[0], 1)), X))
    
    #  (X^T * X)^-1 * X^T * y
    X_transpose = X.T
    coefficients = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
    
    intercept = coefficients[0]
    slopes = coefficients[1:]
    
    print("Intercept:", intercept)
    print("Slopes:", slopes)
    
    y_pred = X.dot(coefficients)
    
    ss_total = sum((y - np.mean(y)) ** 2)
    ss_residual = sum((y - y_pred) ** 2)
    r2 = 1 - (ss_residual / ss_total)
    
    print("Goodness of fit using R-squared method is:", r2)
    
    plt.scatter(y, y_pred, color='#ef5423')
    plt.plot([min(y), max(y)], [min(y), max(y)], color='#58b970', label='Regression Line')
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.legend()
    plt.show()
    

def main():
    print("Multi-linear Regression")
    
    MarvellousMultiLinearPredictor()

if __name__ == "__main__":
    main()
