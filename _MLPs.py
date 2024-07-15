import numpy as np
import pandas as pd
#from keras.utils import to_categorical
# Load data
def MLPclassifier(c):
    data=pd.read_csv('dataaaaaaaaaa.csv')


    # Tên cột
    columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']

    # Tạo DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Loại bỏ các hàng trùng lặp
    df_cleaned = df.drop_duplicates()

    # Spliting data into Feature and
    X=df_cleaned[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']]
    y=df_cleaned['33']


    # Import train_test_split function
    from sklearn.model_selection import train_test_split

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)  # 70% training and 30% test

    '''num_unique_labels = np.unique(y).shape[0]
    y_train_test =  to_categorical(y_train, num_classes = num_unique_labels)
    y_test_test = to_categorical(y_test, num_classes = num_unique_labels)
    '''
    # Import MLPClassifer 
    from sklearn.neural_network import MLPClassifier

    # Create model object
    clf = MLPClassifier(hidden_layer_sizes=(5, 3, 5),
                        random_state=4,
                        verbose=True,
                        activation='logistic',
                        solver='sgd',
                        alpha=0.0001,
                        learning_rate_init=1)

    # Fit data onto the model
    clf.fit(X,y)

    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']
    sample = [a, c]
    # Tạo DataFrame
    df = pd.DataFrame(sample[1:], columns=sample[0])

    # Make prediction on test dataset
    ypred=clf.predict(df)
    y_in = np.unique(ypred)
    print(y_in)
    return y_in
'''
# Import accuracy score 
from sklearn.metrics import accuracy_score

# Calcuate accuracy
accuracy = accuracy_score(y_test, ypred)
print("Với 5 3 5 ")
print("Accuracy:", accuracy)
'''
