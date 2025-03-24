import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("final_dataset_BFP .csv")

# Encoding categorical variables
gender_encoder = LabelEncoder()
bfp_case_encoder = LabelEncoder()
bmi_case_encoder = LabelEncoder()

df['Gender'] = gender_encoder.fit_transform(df['Gender'])
df['BFPcase'] = bfp_case_encoder.fit_transform(df['BFPcase'])
df['BMIcase'] = bmi_case_encoder.fit_transform(df['BMIcase'])

# Selecting features & target (Removed 'Body Fat Percentage')
X = df[['Weight', 'Height', 'BMI', 'Age', 'Gender']]
y = df['Exercise Recommendation Plan']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Decision Tree Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
with open("fitness_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")
