from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd

def KNNWine():
    data = pd.read_csv('Winepredictor.csv')
    Features = data.drop('Class',axis=1)
    Labels = data['Class']

    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size=0.3)

    obj = KNeighborsClassifier(n_neighbors=3)
    obj = obj.fit(data_train,target_train)

    output = obj.predict(data_test)

    Accuracy = accuracy_score(output,target_test)
    print(Accuracy*100,"of 30% testing")
    return Features,Labels
    
def ChkAccuracy(Features,Labels):
    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size=0.5)
    obj = KNeighborsClassifier(n_neighbors=3)
    obj = obj.fit(data_train,target_train)
    output = obj.predict(data_test)
    Accuracy = accuracy_score(output,target_test)
    print(Accuracy*100,"of 50% testing")

def main():
    Features,Labels = KNNWine()
    ChkAccuracy(Features,Labels)

if __name__ == "__main__":
    main()