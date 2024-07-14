import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def MultiLinearRegressionSales():
    data = pd.read_csv('Advertising.csv')
    Features = data.drop('sales',axis=1)
    Labels = data['sales']
    
    obj = LinearRegression()
    obj = obj.fit(Features,Labels)

    r2 = obj.score(Features,Labels)

    print(r2)

def main():
    MultiLinearRegressionSales()

if __name__ == "__main__":
    main()