from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd

def KNNWeather(weather,temperature):
    data = pd.read_csv('PlayPredictor.csv')
    label_enc = LabelEncoder()

    data['Whether']=label_enc.fit_transform(data['Whether'])
    data['Temperature']=label_enc.fit_transform(data['Temperature'])
    data['Play']=label_enc.fit_transform(data['Play'])

    Features = data[['Whether','Temperature']]
    Labels = data['Play']

    obj = KNeighborsClassifier(n_neighbors=3)

    obj = obj.fit(Features,Labels)

    input_data = pd.DataFrame([[weather, temperature]], columns=['Whether', 'Temperature'])
    
    output = obj.predict(input_data)

    if output[0]==1:
        print("Yes")
    else:
        print("No")

    return Features,Labels

def CheckAccuracy(Features, Labels):
    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, test_size=0.5)
    
    obj = KNeighborsClassifier(n_neighbors=3)
    obj.fit(data_train, target_train)
    
    predictions = obj.predict(data_test)
    
    accuracy = accuracy_score(target_test, predictions)
    print("Accuracy: {:.2f}%".format(accuracy * 100))

def main():
    print("------Play Predictor classification case study------")
    print("Please enter the information about the environment that you want to test")

    print("Enter the Weather-")
    weather=input()
    if weather.lower() == "sunny":
        weather = 2
    elif weather.lower() == "overcast":
        weather = 1
    elif weather.lower() == "rainy":
        weather = 0
    else:
        print("Invalid type of weather")
        exit()

    print("Enter the Temperature-")
    temperature=input()
    if temperature.lower() == "hot":
        temperature = 2
    elif temperature.lower() == "mild":
        temperature = 1
    elif temperature.lower() == "cool":
        temperature = 0
    else:
        print("Invalid type of temperature")
        exit()

    Features,Labels = KNNWeather(weather,temperature)
    CheckAccuracy(Features,Labels)

if __name__ == "__main__":
    main()