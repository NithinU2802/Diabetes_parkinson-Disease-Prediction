# Diabetes and Parkinson's Disease Prediction System

Role: Developer || Researcher

# Stages to Develop the System
    Phase-1 : To learn the requirement of build the project.
    Phase-2 : To develop an Model trained with dataset.
    Phase-3 : Integrated with Web Application.
    Pahse-4 : To Deploy the model as a result

# Requirements attach with a file 
    cmd: pip install -r requirements.txt
    
# Steps Implemented to train the model
    1. Make an x and y label to classify the data for prediction.
    2. Using classifier objects to enhance the service of SVM, which provides
    a prediction for the model.
    3. Before classifiers, the labels need to be standardized, which makes
    mode to be trained with a scalar object.

# To find the accuracy of the given data
    # Execute to find the accuracy of model
    X_train_prediction = classifier.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Following package need to be access
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn import svm
    from sklearn.metrics import accuracy_score

# Model Architecture 
![SVM](https://github.com/NithinU2802/Diabetes_parkinson-Disease-Prediction/assets/106614289/86f50ead-ee9a-477d-846b-563a1aa2b310)


# Architecture of the Project
     1. The model has been trained with the required algorithm and standardized.
    make an analysis with label values.
    2. Deploy the project using streamlet and spider web applications to 
    enhance the dataset with easy access to output.

![Architecture](https://github.com/NithinU2802/Diabetes_parkinson-Disease-Prediction/assets/106614289/baf5c046-edd3-4fa0-8251-4752ce17a478)
