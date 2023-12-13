# To made an predictions using Random Forest Algorithm

  # Import Requried Package as Object
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

# Load diabetes dataset (replace with your dataset)
    data = pd.read_csv('diabetes_dataset.csv')

# Split data into features (X) and target (y)
    X = data.drop('label_column', axis=1)
    y = data['label_column']

# Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

# Make predictions on the test set
    y_pred = model.predict(X_test)

# Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy}')

# In First face of the project SVM has been Implemented for the project
    
    SVM: SVM is a supervised learning algorithm used for classification and regression tasks. It
    aims to find a hyperplane that best separates different classes in the feature space.
    Random Forests: Random Forests is an ensemble learning method that builds a multitude of decision
    trees during training and merges them together to get a more accurate and stable prediction.
