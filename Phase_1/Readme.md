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
