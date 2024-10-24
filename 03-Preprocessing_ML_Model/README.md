# Project: Human Resources Dataset Analysis

## Overview
In the third week of this project, the focus shifts to **Data Preprocessing**, **Machine Learning Model Selection**, and **Model Training, Validation, and Testing**. This phase is crucial for building predictive models that can help understand and forecast employee retention.

_________________________________

## (1) Data Preprocessing

Before applying machine learning models, the data needs to be cleaned, transformed, and prepared for analysis. Here’s a summary of the key steps:

- **Encoding Categorical Variables**: Categorical variables such as `Gender`, `BusinessTravel`, and `JobRole` were encoded using methods like **One-Hot Encoding** or **Label Encoding** to make them usable for machine learning algorithms.
- **Feature Scaling**: Continuous variables such as `Salary`, `YearsAtCompany`, and `Age` were normalized using standardization techniques to ensure they contribute equally to the model.
- **Train-Test Split**: The dataset was divided into training and testing sets, ensuring that a separate portion of the data would be used to validate the model performance.

_________________________________

| **Column Name**                      | **Description**                                                                                                              | **Correlation with Attrition_Yes** |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| **Age**                              | The age of the employee. Younger employees may have different job expectations compared to older employees.                 | -0.347087                           |
| **Salary**                           | The annual salary of the employee. Higher salaries might correlate with lower attrition rates due to financial satisfaction.  | -0.205315                           |
| **StockOptionLevel**                 | The level of stock options granted to the employee, which may influence their loyalty to the company.                        | -0.165969                           |
| **YearsAtCompany**                  | The total number of years the employee has worked at the company. Longer tenure often correlates with lower attrition rates. | -0.630678                           |
| **YearsInMostRecentRole**           | The number of years the employee has been in their current role. More years in a role might indicate satisfaction or burnout. | -0.434773                           |
| **YearsSinceLastPromotion**         | The number of years since the employee was last promoted. Longer durations may lead to dissatisfaction and higher attrition.  | -0.577255                           |
| **YearsWithCurrManager**            | The total years spent under the current manager. A good relationship with management may reduce attrition.                   | -0.431820                           |
| **ReviewDate**                      | The date of the most recent performance review. Recent reviews may correlate with employee satisfaction and retention.         | 0.101915                            |
| **Department_Sales**                | A binary indicator (True/False) if the employee works in the Sales department. This department may have different turnover rates. | 0.102166                            |
| **Department_Technology**           | A binary indicator if the employee works in the Technology department. This can indicate a different culture and job satisfaction. | -0.106946                           |
| **JobRole_Data Scientist**           | A binary indicator if the employee's job role is Data Scientist. Different roles may have different job satisfaction levels. | 0.109752                            |
| **JobRole_Engineering Manager**     | A binary indicator if the employee's job role is Engineering Manager. The nature of managerial roles may affect attrition.   | -0.123720                           |
| **JobRole_Machine Learning Engineer**| A binary indicator if the employee's job role is Machine Learning Engineer. Role satisfaction may vary by job type.          | -0.106375                           |
| **JobRole_Sales Representative**    | A binary indicator if the employee is a Sales Representative. Sales roles may have unique pressures affecting turnover.       | 0.182392                            |
| **MaritalStatus_Married**           | A binary indicator if the employee is married. Personal life can influence job satisfaction and retention rates.             | -0.127256                           |
| **MaritalStatus_Single**            | A binary indicator if the employee is single. Single employees may have different job priorities and satisfaction levels.    | 0.221311                            |
| **OverTime_Yes**                    | A binary indicator if the employee works overtime. Increased overtime may correlate with job dissatisfaction and attrition.  | 0.304218                            |
| **Attrition_Yes**                   | Target variable indicating if the employee has left the company (Yes/No). This variable is the main focus of the analysis.  | -                                   |

_________________________________

## (2) Model Selection and Training

After preparing the data, the next step was to choose a suitable machine learning model. Several models were considered:

- **Logistic Regression**: A baseline model for binary classification, predicting whether an employee will leave (`Attrition`).
- **Random Forest Classifier**: An ensemble method known for handling large datasets and providing good accuracy with less overfitting.
- **Support Vector Machines (SVM)**: Applied for its ability to handle both linear and non-linear relationships in the data.
- **Gradient Boosting Machines (GBM)**: Considered for its performance in structured/tabular data like HR datasets.

We used cross-validation techniques to evaluate the models and select the best performing one based on accuracy, precision, recall, and F1-score metrics.

_________________________________

## (3) Model Validation and Testing

After training the selected models, we validated their performance using a validation set. The following steps were taken:

- **Model Evaluation**: The performance of the models was evaluated on the validation set using metrics like **Accuracy** for classification.
- **Testing**: The final selected model was tested on an unseen test dataset to ensure that it generalizes well and performs accurately in predicting employee attrition.

_________________________________

## Tools Used

- **Python (pandas, scikit-learn, Matplotlib, seaborn)**: For data preprocessing, model training, evaluation, and testing.
- **Jupyter Notebook**: For documenting the entire process and results.

_________________________________

## Deliverables:
- A fully processed dataset ready for modeling.
- A trained and tested machine learning model capable of predicting employee attrition.
- A detailed notebook documenting the preprocessing, model selection, and testing process.
- Creating App

The third week of the Human Resources Dataset Analysis project successfully established a robust machine learning pipeline, ensuring that the data was properly prepared, and the best model was selected to predict employee retention with high accuracy. This phase sets the foundation for deploying the model in real-world scenarios.
