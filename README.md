
# Project: Human Resources Dataset Analysis
________________________________________________

# Week 1:

## Overview the first week (A):
During this week (First) of the project, we built a robust data model, then created a DataBase, Inserted into it the dataset, and ensured that the DataBase was consistent and ready for analysis. 
The DB consists of employee information, education levels, satisfaction RatingLevels, Performance Rating, and other essential metrics necessary for HR analysis.

## Data Model and Creating DataBase.
The dataset tables were organized into relational DB to maintain consistency and enable efficient querying. The tables in relational 
 DB included:

### **A) Fact Tables:
- **Employees**: Contains essential employee details, including name, gender, department, salary, and employment history.
- **PerformanceRating**: Stores details about each employee's performance Rating, including satisfaction RatingLevels and self/manager RatingLevels.

### B) Dimension Tables:
- **EducationLevels**: Stores various education levels (e.g., Bachelors, Masters).
- **SatisfactionLevels**: Describes different satisfaction levels for the work environment, job, and relationships.
- **RatingLevels**: Contains rating levels such as "Meets Expectation" and "Above and Beyond."


The relationships between these tables are governed by foreign keys, ensuring data integrity across the system. For instance, employee satisfaction and rating data are linked to their respective levels via foreign key relationships to the `SatisfactionLevels` and `RatingLevels` tables.

### Tools Used:
- **SQL**: For Creating a Database, Insert the Dataset, data validation, relationship checks, and querying.
______________________________________________________________________________
______________________________________________________________________________________


## Overview the first week (B):

In the first week of this project a robust data model was developed, followed by the created of a relational database. The dataset was inserted into the database. The Data Validation and Relationship was Checks into the database for ensuring consistency and readiness. The ensure that the data is free of any illogical data or empty or repeated values for subsequent analysis. 

This database encompasses critical employee information, educational levels, satisfaction ratings, performance ratings, and other essential metrics necessary for Human Resources (HR) analysis.

_________________________________


## (1) Data Model and Creating DataBase :
The dataset tables were organized into a relational database to maintain consistency and enable efficient querying. The relational database comprises the following tables:

### A) Fact Tables
- **Employees**: Contains essential employee details, including name, gender, department, salary, and employment history.
- **PerformanceRating**: Stores details about each employee's performance rating, including satisfaction rating levels and self/manager rating levels.

### B) Dimension Tables
- **EducationLevels**: Stores various education levels (e.g., Bachelors, Masters).
- **SatisfactionLevels**: Describes different satisfaction levels related to the work environment, job satisfaction, and interpersonal relationships.
- **RatingLevels**: Contains rating levels such as "Meets Expectation" and "Above and Beyond."

The relationships between these tables are governed by foreign keys, ensuring data integrity across the system. For instance, employee satisfaction and rating data are linked to their respective levels via foreign key relationships to the **SatisfactionLevels** and **RatingLevels** tables.

## Data Validation and Relationship Checks
To ensure the accuracy and integrity of the database, several SQL queries were executed to validate data and verify relationships between tables. 

## Conclusion:
The process of creating and populating the database was executed flawlessly, ensuring that all necessary information was accurately represented. 
This was further validated through the execution of several test queries, which confirmed the correctness of the database structure and the reliability of the data.
Also, Create a View `FullEmployeePerformanceView` in one table for EDA and Visual Dashboard.


## Tools Used
- **SQL**: Utilized for creating the database, inserting the dataset, performing data validation, checking relationships, and executing queries.

_______________________________________

## (2) Data Cleaning:
After building the data model, we proceeded with data cleaning and preprocessing. Here’s a summary of the key observations:

- The data had no missing values or unusual entries across all tables. Each field, such as age, salary, and years of experience, showed values within expected ranges.
- Data entries for categorical variables like gender, marital status, and job roles were consistent without any spelling or formatting issues.
- Date fields, such as the employee `HireDate` and `ReviewDate` in the performance review table, were in the correct format and adhered to the expected chronological order.
- Numeric fields, including `Salary`, `YearsAtCompany`, and `DistanceFromHome`, were confirmed to contain only valid numbers without any outliers or inconsistent values.

## Conclusion:
The dataset was thoroughly examined and found to be clean, consistent, and aligned with the designed data model. 
There were no missing values, illogical entries, or repeated values, ensuring data integrity across all tables. 
Also, the datasets were saved in one CSV file `06-All_Data_Employees.csv` for EDA and Visual Dashboard.


- **Python (pandas, Matplotlib)**: For detailed data Cleaning and visual inspection.

_____________________________________

## Deliverables:
- A cleaned dataset, ready for analysis.
- Data preprocessing notebook, showcasing steps taken to validate and clean the data.

The first week of the Human Resources Dataset Analysis project successfully established a well-structured database and free of any illogical data or empty or repeated values, allowing for efficient data management and analysis. 
This setup serves as a strong foundation for further analytical tasks in the HR domain.

______________________________________________________
______________________________________________________
______________________________________________________
# Week 2:

## Overview the second weeK:
In the second week of this project, we focused on exploratory data analysis (EDA) to identify key questions related to employee retention. This phase aimed to determine how various factors, such as salary, job satisfaction, and overtime, impact the likelihood of employees leaving the company.

_________________________________

## Exploratory Data Analysis (EDA) And Data Analysis Questions:

Based on the company's interest in studying factors influencing employee retention, the following key questions were posed:

1. **Do employees who live more than 20 miles away `DistanceFromHome` have a higher tendency to leave the company `Attrition`?**
   
2. **Are employees with higher satisfaction levels at work `EnvironmentSatisfactionLevel` more likely to stay with the company `Attrition`?**

3. **Do more `TrainingOpportunitiesTaken` reduce the likelihood of an employee leaving the company `Attrition`?**

4. **Does an increase in salary `Salary` positively impact employee retention `Attrition`?**

5. **Does working `OverTime` negatively impact employee retention `Attrition`?**

6. **Is there a correlation between employee `Gender` and retention rate `Attrition`?**

7. **Are employees who frequently travel for business `BusinessTravel` more likely to leave the company `Attrition` than others?**

_________________________________

## Results:

1. `Distance From Home` exceeding 20 miles does not have a significant impact on employee turnover.
   
2. `Job Satisfaction` does not show a clear influence on whether employees stay with the company.

3. `Training Opportunities` provided to employees do not significantly affect their retention rates.

4. `Salary` increases positively influence employee retention, with higher salaries leading to longer tenures at the company.

5. `OverTime` has a negative impact on employee retention, with those working overtime more likely to leave.

6. There is a relationship between `Gender` and retention rates. Female employees are less likely to leave the company compared to male employees.

7. Employees who frequently engage in `Business Travel` are more likely to leave the company than those who travel less often.

_________________________________

## Summary

The analysis revealed that `Salary` increases and `Gender` are significant factors influencing employee retention. Higher salaries are associated with longer employee tenures, and female employees tend to have a lower attrition rate than male employees. Meanwhile, `OverTime` and frequent `Business Travel` were linked to higher turnover rates. 

However, other factors such as `Job Satisfaction`, `Distance From Home`, and `Training Opportunities` did not show a clear impact on employee retention. 

While these insights provide useful information, further detailed analysis and verification are needed to better understand the complex dynamics between these variables and employee retention.

______________________________________________________________
________________________________________________________________
_______________________________________________________________
# Week 3:

## Overview the third week:

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

- **Logistic Regression (LR)**: A baseline model for binary classification, used to predict whether an employee will leave (`Attrition`).
- **K-Nearest Neighbors (KNN)**: A simple model based on proximity, used for classifying data based on the closest neighbors.
- **Decision Tree (DT)**: A tree-based model used to determine decision paths, known for its interpretability and ease of use.
- **Support Vector Classifier (SVC)**: Utilized for its ability to handle both linear and non-linear relationships in the data.
- **Naive Bayes (NB)**: A probabilistic model used for classification, particularly effective for text data.
- **Random Forest (RF)**: An ensemble method known for handling large datasets and providing good accuracy while reducing overfitting.

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
