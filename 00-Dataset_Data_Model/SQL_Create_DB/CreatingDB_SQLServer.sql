-- SELECT name FROM sys.databases;

-- DROP DATABASE HR_system;

-- CREATE DATABASE HR_system;
-- USE HR_system;
-- SELECT * FROM sys.tables;

-- Create table for storing education levels
CREATE TABLE EducationLevels (
    EducationLevelID INT PRIMARY KEY, -- Unique identifier for each education level
    EducationLevel VARCHAR(50) NOT NULL -- Description of the education level (e.g., Bachelors, Masters)
);

-- Create table for storing satisfaction levels
CREATE TABLE SatisfactionLevels (
    SatisfactionID INT PRIMARY KEY, -- Unique identifier for each satisfaction level
    SatisfactionLevel VARCHAR(50) NOT NULL -- Description of satisfaction level (e.g., Satisfied, Dissatisfied)
);

-- Create table for storing rating levels
CREATE TABLE RatingLevels (
    RatingID INT PRIMARY KEY, -- Unique identifier for each rating level
    RatingLevel VARCHAR(50) NOT NULL -- Description of performance rating (e.g., Meets Expectation, Above and Beyond)
);

-- Create table for storing employee details
CREATE TABLE Employees (
    EmployeeID VARCHAR(20) PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL, -- Employee's first name
    LastName VARCHAR(50) NOT NULL, -- Employee's last name
    Gender VARCHAR(30), -- Employee's gender
    Age INT, -- Employee's age
    BusinessTravel VARCHAR(50), -- Frequency of business travel
    Department VARCHAR(50), -- Department where the employee works
    DistanceFromHome INT, -- Distance from home to office in kilometers
    State VARCHAR(50), -- State where the employee resides
    Ethnicity VARCHAR(50), -- Employee's ethnicity
    Education INT, -- Foreign key referencing EducationLevels
    EducationField VARCHAR(50), -- Field of education or study
    JobRole VARCHAR(50), -- Job role of the employee
    MaritalStatus VARCHAR(20), -- Marital status of the employee
    Salary FLOAT, -- Employee's salary
    StockOptionLevel INT, -- Employee's stock option level
    OverTime NVARCHAR(3), -- Whether the employee works overtime or not (0 = No, 1 = Yes)
    HireDate DATETIME, -- Date the employee was hired
    Attrition NVARCHAR(3), -- Whether the employee has left the company or not (0 = No, 1 = Yes)
    YearsAtCompany INT, -- Total number of years the employee has worked at the company
    YearsInMostRecentRole INT, -- Number of years in the employee's most recent role
    YearsSinceLastPromotion INT, -- Number of years since the employee's last promotion
    YearsWithCurrManager INT, -- Number of years the employee has worked with the current manager
    FOREIGN KEY (Education) REFERENCES EducationLevels(EducationLevelID) -- Establish a foreign key relationship to the EducationLevels table
);

-- Create table for storing performance review details
CREATE TABLE PerformanceRating (
    PerformanceID VARCHAR(20) PRIMARY KEY, -- Unique identifier for each performance review
    EmployeeID VARCHAR(20), -- Foreign key referencing Employees table
    ReviewDate DATETIME, -- Date the performance review took place
    EnvironmentSatisfaction INT, -- Satisfaction with work environment (references SatisfactionLevels)
    JobSatisfaction INT, -- Satisfaction with the job (references SatisfactionLevels)
    RelationshipSatisfaction INT, -- Satisfaction with relationships at work (references SatisfactionLevels)
    TrainingOpportunitiesWithinYear INT, -- Number of training opportunities offered within the year
    TrainingOpportunitiesTaken INT, -- Number of training opportunities taken by the employee
    WorkLifeBalance INT, -- Work-life balance rating (references SatisfactionLevels)
    SelfRating INT, -- Self-rating by the employee (references RatingLevels)
    ManagerRating INT, -- Rating given by the manager (references RatingLevels),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID), -- Establish a foreign key relationship to the Employees table
    FOREIGN KEY (EnvironmentSatisfaction) REFERENCES SatisfactionLevels(SatisfactionID), -- Establish foreign key relationship to SatisfactionLevels table
    FOREIGN KEY (JobSatisfaction) REFERENCES SatisfactionLevels(SatisfactionID), -- Job satisfaction foreign key
    FOREIGN KEY (RelationshipSatisfaction) REFERENCES SatisfactionLevels(SatisfactionID), -- Relationship satisfaction foreign key
    FOREIGN KEY (WorkLifeBalance) REFERENCES SatisfactionLevels(SatisfactionID), -- Work-life balance foreign key
    FOREIGN KEY (SelfRating) REFERENCES RatingLevels(RatingID), -- Foreign key for self-rating referencing RatingLevels
    FOREIGN KEY (ManagerRating) REFERENCES RatingLevels(RatingID) -- Foreign key for manager rating referencing RatingLevels
);
