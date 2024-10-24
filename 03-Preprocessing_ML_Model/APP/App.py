import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd
import numpy as np
import os

# Get the current directory
parent_directory = os.path.dirname(os.getcwd())

# Load the model, features, and scaler
model = joblib.load(os.path.join(parent_directory, 'best_model.h5'))
features = joblib.load(os.path.join(parent_directory, 'features.h5'))
scaler = joblib.load(os.path.join(parent_directory, 'scaler.h5'))

# Create a function to handle predictions
def predict_attrition():
    try:
        # Collect the input values from the user
        age = float(age_entry.get())
        salary = float(salary_entry.get())
        stock_option_level = float(stock_option_level_entry.get())
        years_at_company = float(years_at_company_entry.get())
        years_in_most_recent_role = float(years_in_most_recent_role_entry.get())
        years_since_last_promotion = float(years_since_last_promotion_entry.get())
        years_with_curr_manager = float(years_with_curr_manager_entry.get())
        department_sales = int(department_sales_entry.get())
        department_technology = int(department_technology_entry.get())
        jobrole_data_scientist = int(jobrole_data_scientist_entry.get())
        jobrole_engineering_manager = int(jobrole_engineering_manager_entry.get())
        jobrole_machine_learning_engineer = int(jobrole_machine_learning_engineer_entry.get())
        jobrole_sales_representative = int(jobrole_sales_representative_entry.get())
        marital_status_married = int(marital_status_married_entry.get())
        marital_status_single = int(marital_status_single_entry.get())
        overtime_yes = int(overtime_yes_entry.get())

        # Create a DataFrame for the input data
        input_df = pd.DataFrame({
            'Age': [age],
            'Salary': [salary],
            'StockOptionLevel': [stock_option_level],
            'YearsAtCompany': [years_at_company],
            'YearsInMostRecentRole': [years_in_most_recent_role],
            'YearsSinceLastPromotion': [years_since_last_promotion],
            'YearsWithCurrManager': [years_with_curr_manager],
            'Department_Sales': [department_sales],
            'Department_Technology': [department_technology],
            'JobRole_Data Scientist': [jobrole_data_scientist],
            'JobRole_Engineering Manager': [jobrole_engineering_manager],
            'JobRole_Machine Learning Engineer': [jobrole_machine_learning_engineer],
            'JobRole_Sales Representative': [jobrole_sales_representative],
            'MaritalStatus_Married': [marital_status_married],
            'MaritalStatus_Single': [marital_status_single],
            'OverTime_Yes': [overtime_yes]
        })

        # Scale the age and salary
        input_df[['Age', 'Salary']] = scaler.transform(input_df[['Age', 'Salary']])

        # Predict using the loaded model
        prediction = model.predict(input_df)

        # Display the result
        result = "Yes" if prediction[0] == 1 else "No"
        messagebox.showinfo("Prediction Result", f"Attrition Prediction: {result}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main application window
app = tk.Tk()
app.title("Attrition Prediction")

# Create and place input fields and labels
tk.Label(app, text="Age").grid(row=0, column=0)
age_entry = tk.Entry(app)
age_entry.grid(row=0, column=1)

tk.Label(app, text="Salary").grid(row=1, column=0)
salary_entry = tk.Entry(app)
salary_entry.grid(row=1, column=1)

tk.Label(app, text="Stock Option Level (1 or 2 or 3)").grid(row=2, column=0)
stock_option_level_entry = tk.Entry(app)
stock_option_level_entry.grid(row=2, column=1)

tk.Label(app, text="Years at Company").grid(row=3, column=0)
years_at_company_entry = tk.Entry(app)
years_at_company_entry.grid(row=3, column=1)

tk.Label(app, text="Years in Most Recent Role").grid(row=4, column=0)
years_in_most_recent_role_entry = tk.Entry(app)
years_in_most_recent_role_entry.grid(row=4, column=1)

tk.Label(app, text="Years Since Last Promotion").grid(row=5, column=0)
years_since_last_promotion_entry = tk.Entry(app)
years_since_last_promotion_entry.grid(row=5, column=1)

tk.Label(app, text="Years With Current Manager").grid(row=6, column=0)
years_with_curr_manager_entry = tk.Entry(app)
years_with_curr_manager_entry.grid(row=6, column=1)

tk.Label(app, text="Department Sales (0 or 1)").grid(row=7, column=0)
department_sales_entry = tk.Entry(app)
department_sales_entry.grid(row=7, column=1)

tk.Label(app, text="Department Technology (0 or 1)").grid(row=8, column=0)
department_technology_entry = tk.Entry(app)
department_technology_entry.grid(row=8, column=1)

tk.Label(app, text="Job Role Data Scientist (0 or 1)").grid(row=9, column=0)
jobrole_data_scientist_entry = tk.Entry(app)
jobrole_data_scientist_entry.grid(row=9, column=1)

tk.Label(app, text="Job Role Engineering Manager (0 or 1)").grid(row=10, column=0)
jobrole_engineering_manager_entry = tk.Entry(app)
jobrole_engineering_manager_entry.grid(row=10, column=1)

tk.Label(app, text="Job Role ML Engineer (0 or 1)").grid(row=11, column=0)
jobrole_machine_learning_engineer_entry = tk.Entry(app)
jobrole_machine_learning_engineer_entry.grid(row=11, column=1)

tk.Label(app, text="Job Role Sales Rep (0 or 1)").grid(row=12, column=0)
jobrole_sales_representative_entry = tk.Entry(app)
jobrole_sales_representative_entry.grid(row=12, column=1)

tk.Label(app, text="Marital Status Married (0 or 1)").grid(row=13, column=0)
marital_status_married_entry = tk.Entry(app)
marital_status_married_entry.grid(row=13, column=1)

tk.Label(app, text="Marital Status Single (0 or 1)").grid(row=14, column=0)
marital_status_single_entry = tk.Entry(app)
marital_status_single_entry.grid(row=14, column=1)

tk.Label(app, text="OverTime Yes (0 or 1)").grid(row=15, column=0)
overtime_yes_entry = tk.Entry(app)
overtime_yes_entry.grid(row=15, column=1)

# Create and place the Predict button
predict_button = tk.Button(app, text="Predict Attrition", command=predict_attrition)
predict_button.grid(row=16, columnspan=2)

# Run the application
try:
    app.mainloop()
except Exception as e:
    messagebox.showerror("Application Error", f"An error occurred: {str(e)}")
