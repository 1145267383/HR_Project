# Project: Human Resources Dataset Analysis

## Overview
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

The first week of the Human Resources Dataset Analysis project successfully established a well-structured database and free of any illogical data or empty or repeated values, allowing for efficient data management and analysis. This setup serves as a strong foundation for further analytical tasks in the HR domain.