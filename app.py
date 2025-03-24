import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("fitness_model.pkl", "rb") as file:
    model = pickle.load(file)

# Map numeric predictions to actual categories
category_mapping = {
    1: "sever thinness",
    2: "mild thinness",
    3: "moderate thinness",
    4: "normal",
    5: "over weight",
    6: "obese",
    7: "severe obese"
}

# Custom Fitness Recommendation Plans for Different Categories
fitness_recommendations = {
     "over weight": {
        "bmi_case": "Overweight",
        "diet": "🥗 Reduce processed carbs & sugar, eat more protein (chicken, fish, tofu, eggs), increase fiber intake (vegetables, fruits, whole grains), and drink plenty of water.",
        "exercise": "🏃‍♂️ 45 min of moderate-intensity cardio (brisk walking, jogging, cycling), strength training (3-4x per week), and HIIT workouts to burn fat efficiently."
    },
    "normal": {
        "bmi_case": "Normal Weight",
        "diet": "🍽️ Maintain a balanced diet with healthy carbs, proteins, and fats. Include plenty of fruits and vegetables while avoiding excess junk food.",
        "exercise": "💪 30 min of daily cardio (running, cycling, skipping), strength training (2-3x per week), and flexibility exercises like yoga and stretching."
    },
    "severe obese": {
        "bmi_case": "Severely Obese",
        "diet": "⚠️ Follow a high-protein, low-carb diet. Avoid sugary & processed foods, increase fiber intake, and maintain a calorie deficit.",
        "exercise": "🚶 Start with low-impact exercises (swimming, cycling), walk for 30-45 min daily, and slowly incorporate bodyweight exercises (chair squats, wall push-ups)."
    },
    "obese": {
        "bmi_case": "Obese",
        "diet": "🔥 Reduce carb intake and focus on high protein. Drink plenty of water, eat small frequent meals, and include healthy fats like nuts & avocado.",
        "exercise": "🏋️ 60 min of moderate-intensity cardio (brisk walking, elliptical), strength training (light weights, resistance bands), and a strict calorie deficit diet."
    },
    "mild thinness": {
        "bmi_case": "Mild Thinness",
        "diet": "🍞 Increase caloric intake with healthy fats & carbs (nuts, dairy, avocado). Eat protein-rich foods and focus on nutrient-dense meals.",
        "exercise": "🏋️ Strength training (weight lifting, resistance workouts), bodyweight exercises (push-ups, squats), and limited cardio to focus on muscle gain."
    },
    "sever thinness": {
        "bmi_case": "Severe Thinness",
        "diet": "🍛 Eat calorie-dense foods (whole grains, dairy, nuts), increase protein intake (chicken, fish, eggs, soy), and eat small frequent meals.",
        "exercise": "💪 Focus on muscle building with strength training (progressive overload), avoid excessive cardio, and perform weight-based exercises."
    },
    "moderate thinness": {
        "bmi_case": "Moderate Thinness",
        "diet": "🥑 Increase healthy calorie intake with protein & complex carbs. Include dairy, nuts, whole grains, and eat more frequently.",
        "exercise": "🏋️‍♂️ Resistance training (light to moderate weightlifting), bodyweight workouts (pull-ups, lunges), and limited cardio (light jogging, walking)."
    }
}


# Streamlit UI
st.title("🏋️‍♂️ Personal Fitness Tracker")

# User Inputs
weight = st.number_input("Enter your Weight (kg)", min_value=30.0, max_value=200.0, step=0.1)
height = st.number_input("Enter your Height (m)", min_value=1.0, max_value=2.5, step=0.01)
age = st.number_input("Enter your Age", min_value=10, max_value=100, step=1)
gender = st.selectbox("Select Gender", ["Male", "Female"])

# Encode Gender
gender_value = 0 if gender == "Male" else 1

# Calculate BMI
bmi = weight / (height ** 2) if height > 0 else 0

# Predict Fitness Category
if st.button("Get Fitness Recommendation"):
    input_data = np.array([[weight, height, bmi, age, gender_value]])  # Removed Body Fat Percentage
    predicted_numeric = model.predict(input_data)[0]  # Get numeric prediction

    # Convert numeric prediction to category
    predicted_category = category_mapping.get(predicted_numeric, "Unknown")

    # Get the mapped exercise plan
    recommendation = fitness_recommendations.get(predicted_category, {
        "bmi_case": "Unknown",
        "diet": "🤷 Unknown Plan - Please consult a nutritionist!",
        "exercise": "🤷 Unknown Plan - Please consult a trainer!"
    })

    st.subheader(f"📊 Your BMI: {bmi:.2f} ({recommendation['bmi_case']})")
    st.success(f"🏃 Recommended Exercise Plan: {recommendation['exercise']}")
    st.info(f"🍽️ Diet Plan: {recommendation['diet']}")