from sklearn import tree

# Rough 1
# Smooth 0

# Tennis 1
# Cricket 2
def MarvellousClassifier():
    print("Ball Classification Case Study")

    # Feature Encoding
    Features = [[35,1], [47,1], [90,0], [48,1], [90,0], [35,1], [92,0], [35,1], [35,1], [35,1]]

    # Label Encoding
    Labels = [1,1,2,1,2,1,2,1,1,1]

    # decide the algorithm
    obj = tree.DecisionTreeClassifier()

    # Train the model
    obj = obj.fit(Features,Labels)

    # Test the model
    ret=obj.predict([[96,0]])
    if ret == 1:
        print("Your object looks like Tennis ball")
    else:
        print("Your object looks like Cricket ball")

def main():
    print("------Ball type classification case study------")

    MarvellousClassifier()
    
if __name__ == "__main__":
    main()

