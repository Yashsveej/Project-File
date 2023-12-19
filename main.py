# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the employee dataset
data= pd.read_csv('Employee.csv')
data = pd.get_dummies(data, columns = ['Education','City','Gender','EverBenched'] )
X = data.drop('LeaveOrNot',axis=1)
y = data['LeaveOrNot']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the Random Forest model
random_forest.fit(X_train, y_train)

# Make predictions on the test set
y_pred = random_forest.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save the trained model to a file
model_filename = 'random_forest_model.joblib'
joblib.dump(random_forest, model_filename)
print(f"Model saved to {model_filename}")