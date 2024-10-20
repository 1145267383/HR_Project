# Week 1: Data Model and Creating DataBase.

## Overview
During this week (First) of the project, we built a robust data model, then created a DataBase, Inserted into it the dataset, and ensured that the DataBase was consistent and ready for analysis. 
The DB consists of employee information, education levels, satisfaction RatingLevels, Performance Rating, and other essential metrics necessary for HR analysis.

## Data Model
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
