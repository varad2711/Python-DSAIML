from sklearn import tree
from sklearn.datasets import load_iris

def main():
    print("------ Iris Flower Classification Case Study -----")

    iris = load_iris()

    # print(type(data))

    print(iris)
    Features = iris.data 
    Labels = iris.target

    print("Features are: ")
    print(Features)

    print("Labels are: ")
    print(Labels)
if __name__ == "__main__":
    main()