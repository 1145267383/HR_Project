-- Insert the data from CSV files into the tables.

-- Employees
BULK INSERT Employees FROM '.\01-Dataset\01-Employee.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- PerformanceRating 
BULK INSERT PerformanceRating FROM '.\01-Dataset\02-PerformanceRating.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- EducationLevels
BULK INSERT EducationLevels FROM '.\01-Dataset\03-EducationLevels.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- SatisfactionLevels
BULK INSERT SatisfactionLevels FROM '.\01-Dataset\04-SatisfactionLevels.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- RatingLevels
BULK INSERT RatingLevels FROM '.\01-Dataset\05-RatingLevels.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

