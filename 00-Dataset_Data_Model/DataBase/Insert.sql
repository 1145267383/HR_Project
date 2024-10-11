BULK INSERT Employees FROM '.\01-Dataset\01-Employee.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

