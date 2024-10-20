# Week 1: Data Model, Cleaning, and Preprocessing

## Overview
During this week (First) of the project, we will build a robust data model, clean the dataset, and ensure that the data is consistent and ready for analysis. The dataset consists of employee information, education levels, satisfaction RatingLevels, performance reviews, and other essential metrics necessary for HR analysis.

## Data Model
The dataset was organized into several relational tables to maintain consistency and enable efficient querying. The core tables included:

- **Employees**: Contains essential employee details, including name, gender, department, salary, and employment history.
- **EducationLevels**: Stores various education levels (e.g., Bachelors, Masters).
- **SatisfactionLevels**: Describes different satisfaction levels for the work environment, job, and relationships.
- **RatingLevels**: Contains rating levels such as "Meets Expectation" and "Above and Beyond."
- **PerformanceReviews**: Stores details about each employee's performance reviews, including satisfaction RatingLevels and self/manager RatingLevels.

The relationships between these tables are governed by foreign keys, ensuring data integrity across the system. For instance, employee satisfaction and rating data are linked to their respective levels via foreign key relationships to the `SatisfactionLevels` and `RatingLevels` tables.

### Tools Used:
- **SQL**: For Creating a Database, Insert the Dataset, data validation, relationship checks, and querying.


________________________________

## Data Cleaning and Preprocessing
After building the data model, we proceeded with data cleaning and preprocessing. Here’s a summary of the key observations:

- The data had no missing values or unusual entries across all tables. Each field, such as age, salary, and years of experience, showed values within expected ranges.
- Data entries for categorical variables like gender, marital status, and job roles were consistent without any spelling or formatting issues.
- Date fields, such as the employee `HireDate` and `ReviewDate` in the performance review table, were in the correct format and adhered to the expected chronological order.
- Numeric fields, including `Salary`, `YearsAtCompany`, and `DistanceFromHome`, were confirmed to contain only valid numbers without any outliers or inconsistent values.

## Conclusion
The dataset was found to be clean, free of errors, and consistent with the designed data model. The foreign key relationships worked as expected, linking employee details to education levels, satisfaction levels, and performance RatingLevels. With this well-prepared and consistent dataset, we are ready to move forward to the next phase of analysis, ensuring that our data pipeline is reliable and efficient.

- **Python (pandas, Matplotlib)**: For detailed data preprocessing and visual inspection.

_______________________

### Deliverables:
- A cleaned dataset, ready for analysis.
- Data preprocessing notebook, showcasing steps taken to validate and clean the data.

