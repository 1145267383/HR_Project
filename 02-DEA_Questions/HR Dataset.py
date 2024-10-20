#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


employee = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\Employee.csv")
pd.set_option('display.max_columns', None)
employee


# In[5]:


employee['State']= employee['State'].replace('IL', 'Illinois', inplace=False)
employee['State']= employee['State'].replace('CA', 'California', inplace=False)
employee['State']= employee['State'].replace('NY', 'New York', inplace=False)
employee


# In[6]:


Educationlevel = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\EducationLevel.csv")
Educationlevel


# In[7]:


for index, row in employee.iterrows():
    if row['Education'] == 1:
        employee.at[index, 'EducationLevel'] = 'No Formal Qualifications'
    elif row['Education'] == 2:
        employee.at[index, 'EducationLevel'] = 'Highschool'
    elif row['Education'] == 3:
        employee.at[index, 'EducationLevel'] = 'Bachelors'
    elif row['Education'] == 4:
        employee.at[index, 'EducationLevel'] = 'Masters'
    elif row['Education'] == 5:
        employee.at[index, 'EducationLevel'] = 'Doctorate'

print(employee)


# In[8]:


PerformanceRating = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\PerformanceRating.csv")
PerformanceRating


# In[9]:


RatingLevel = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\RatingLevel.csv")
RatingLevel


# In[10]:


for index, row in PerformanceRating.iterrows():
    if row['SelfRating'] == 1:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Unacceptable'
    elif row['SelfRating'] == 2:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Needs Improvement'
    elif row['SelfRating'] == 3:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Meets Expectation'
    elif row['SelfRating'] == 4:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Exceeds Expectation'
    elif row['SelfRating'] == 5:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Above and Beyond'

print(PerformanceRating)


# In[11]:


for index, row in PerformanceRating.iterrows():
    if row['ManagerRating'] == 1:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Unacceptable'
    elif row['ManagerRating'] == 2:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Needs Improvement'
    elif row['ManagerRating'] == 3:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Meets Expectation'
    elif row['ManagerRating'] == 4:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Exceeds Expectation'
    elif row['ManagerRating'] == 5:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Above and Beyond'

print(PerformanceRating)


# In[12]:


SatisfiedLevel = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\SatisfiedLevel.csv")
SatisfiedLevel


# In[13]:


for index, row in PerformanceRating.iterrows():
    if row['EnvironmentSatisfaction'] == 1:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Very Dissatisfied'
    elif row['EnvironmentSatisfaction'] == 2:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Dissatisfied'
    elif row['EnvironmentSatisfaction'] == 3:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Neutral'
    elif row['EnvironmentSatisfaction'] == 4:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Satisfied'
    elif row['EnvironmentSatisfaction'] == 5:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Very Satisfied'

print(PerformanceRating)


# In[14]:


for index, row in PerformanceRating.iterrows():
    if row['JobSatisfaction'] == 1:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Very Dissatisfied'
    elif row['JobSatisfaction'] == 2:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Dissatisfied'
    elif row['JobSatisfaction'] == 3:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Neutral'
    elif row['JobSatisfaction'] == 4:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Satisfied'
    elif row['JobSatisfaction'] == 5:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Very Satisfied'

print(PerformanceRating)


# In[15]:


for index, row in PerformanceRating.iterrows():
    if row['RelationshipSatisfaction'] == 1:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Very Dissatisfied'
    elif row['RelationshipSatisfaction'] == 2:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Dissatisfied'
    elif row['RelationshipSatisfaction'] == 3:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Neutral'
    elif row['RelationshipSatisfaction'] == 4:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Satisfied'
    elif row['RelationshipSatisfaction'] == 5:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Very Satisfied'

print(PerformanceRating)


# In[16]:


Employee_Performance_Merged = pd.merge(employee, PerformanceRating, on='EmployeeID')
pd.set_option('display.max_columns', None)
Employee_Performance_Merged


# In[17]:


Employee_Performance_Merged.info()


# In[18]:


Employee_Performance_Merged.describe()


# In[19]:


sns.boxplot(x='Salary', data=employee)
plt.title('Salary Distribution')
plt.show()


# # Salary 

# #Which department has the highest average salary?

# In[20]:


highest_salary_department = employee.groupby('Department')['Salary'].mean().nlargest().reset_index()
print(highest_salary_department)


# #How does the salary distribution vary across different education levels or fields of study?

# In[21]:


education_salary_stats = employee.groupby('EducationLevel')['Salary'].mean().nlargest().reset_index()
print("Salary Distribution by Education Level:")
print(education_salary_stats)


# In[22]:


education_field_salary_stats = employee.groupby('EducationField')['Salary'].mean().nlargest().reset_index()
print("Salary Distribution by Field of Study:")
print(education_field_salary_stats)


# #Arrange the salaries in descending order according to their associated positions ?

# In[23]:


average_salary_by_JobRole = employee.groupby('JobRole')['Salary'].mean().sort_values(ascending=False).reset_index()
print(average_salary_by_JobRole)


# #What job roles have the highest percentage of employees working overtime?

# In[27]:


total_employees = employee.shape[0]

JobRole_Overtime = employee[employee['OverTime'] == 'Yes'].groupby('JobRole')['OverTime'].count()
JobRole_Total = employee.groupby('JobRole').size()

JobRole_Overtime_rate = (JobRole_Overtime / total_employees) * 100
JobRole_Overtime_rate = JobRole_Overtime_rate.fillna(0)  
JobRole_Overtime_rate = JobRole_Overtime_rate.nlargest().reset_index().rename(columns={'index': 'JobRole', 0: 'OvertTime Rate'})

print(JobRole_Overtime_rate)


# #Are there significant differences in salaries between genders?

# In[28]:


average_salary_by_Gender = employee.groupby('Gender')['Salary'].mean().nlargest().reset_index()
print(average_salary_by_Gender)


# #Is there an ethnic pay gap?

# In[29]:


average_salary_by_Ethnicity = employee.groupby('Ethnicity')['Salary'].mean().nlargest().reset_index()
print(average_salary_by_Ethnicity)


# # Turnover

# In[41]:


mean_turnover_rate = department_turnover_rate['Turnover Rate'].mean()
median_turnover_rate = department_turnover_rate['Turnover Rate'].median()
mode_turnover_rate = department_turnover_rate['Turnover Rate'].mode()
print("Mean turnover rate:", mean_turnover_rate)
print("Median turnover rate:", median_turnover_rate)
print("Mode turnover rate:", mode_turnover_rate)


# #Which department has the highest rate of employee turnover?

# In[31]:


department_turnover = employee[employee['Attrition'] == 'Yes'].groupby('Department')['Attrition'].count()
department_total_employees = employee.groupby('Department').size()

department_turnover_rate = (department_turnover / department_total_employees) * 100
department_turnover_rate = department_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Department', 0: 'Turnover Rate'})

print(department_turnover_rate)


# #which position has the highest employee turnover?

# In[32]:


JobRole_turnover = employee[employee['Attrition'] == 'Yes'].groupby('JobRole')['Attrition'].count()
total_employees = employee.groupby('JobRole').size()

JobRole_turnover_rate = (JobRole_turnover / total_employees) * 100
JobRole_turnover_rate = JobRole_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Department', 0: 'Turnover Rate'})

print(JobRole_turnover_rate)


# #Is there a significant difference in turnover rates among different ethnic groups?

# In[33]:


Ethnicity_turnover = employee[employee['Attrition'] == 'Yes'].groupby('Ethnicity')['Attrition'].count()
total_employees = employee.groupby('Ethnicity').size()

Ethnicity_turnover_rate = (Ethnicity_turnover / total_employees) * 100
Ethnicity_turnover_rate = Ethnicity_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Department', 0: 'Turnover Rate'})

print(Ethnicity_turnover_rate)


# #Does the distance from home have a significant impact on turnover rates?

# In[34]:


employee = pd.DataFrame(employee )

bins = [10, 20, 30, 40, 50 ,60] 
labels = ['1-10', '11-20', '21-30', '31-40','41-50']  
employee['Distance'] = pd.cut(employee['DistanceFromHome (KM)'], bins=bins, labels=labels)

attrition_by_Distance = employee.groupby(['Distance', 'Attrition']).size().unstack().fillna(0)

print(attrition_by_Distance)


# In[35]:


attrition_by_Distance.plot(kind='bar', stacked=True)
plt.title('Attrition by Distance')
plt.ylabel('Employees Count')
plt.xlabel('Distance')
plt.show()


# #Are there notable differences in employee retention among different age groups?

# In[36]:


employee = pd.DataFrame(employee )

bins = [20, 30, 40, 50, 60] 
labels = ['20-29', '30-39', '40-49', '50-59']  
employee['AgeGroup'] = pd.cut(employee['Age'], bins=bins, labels=labels, right=False)

Turnover_by_age = employee.groupby(['AgeGroup', 'Attrition']).size().unstack().fillna(0)

print(Turnover_by_age)


# In[42]:


Turnover_by_age.plot(kind='bar', stacked=True)
plt.title('Turnover by age')
plt.ylabel('Employees Count')
plt.xlabel('Age Group')
plt.show()


# #Is there an interaction between gender in predicting turnover?

# In[43]:


Gender_turnover = employee[employee['Attrition'] == 'Yes'].groupby('Gender')['Attrition'].count()
total_employees = employee.groupby('Gender').size()

Gender_turnover_rate = (Gender_turnover / total_employees) * 100
Gender_turnover_rate = Gender_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Department', 0: 'Turnover Rate'})

print(Gender_turnover_rate)


# #Are employees who work long hours more likely to leave the organization?

# In[44]:


OverTime_turnover = employee[employee['Attrition'] == 'Yes'].groupby('OverTime')['Attrition'].count()
total_employees = employee.groupby('OverTime').size()

OverTime_turnover_rate = (OverTime_turnover / total_employees) * 100
OverTime_turnover_rate = OverTime_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Department', 0: 'Turnover Rate'})

print(OverTime_turnover_rate)


# # Employees satisfaction 

# #Is there a significant relation between salary levels and Relationship-satisfaction?

# In[45]:


salary_RelationshipSatisfaction = Employee_Performance_Merged.groupby('RelationshipSatisfactionLevel')['Salary'].mean().nlargest().reset_index()
print(salary_RelationshipSatisfaction)


# #How do the overall levels of EnvironmentSatisfaction, JobSatisfaction, and RelationshipSatisfaction differ between employees who turned over and those who stayed?

# In[46]:


attrition_satisfaction = Employee_Performance_Merged.groupby('Attrition')[['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']].mean()
print(attrition_satisfaction)


# #How satisfied are the employees with their job?

# In[47]:


JobRole_Satisfaction = Employee_Performance_Merged.groupby('JobRole')['JobSatisfaction'].mean()
print(JobRole_Satisfaction)


# #Does employee training positively impact job satisfaction?

# In[49]:


training_satisfaction = Employee_Performance_Merged.groupby('TrainingOpportunitiesTaken')['JobSatisfaction'].mean()
print(training_satisfaction)


# # Ratings

# #Are employees with higher self-ratings generally rewarded with higher salaries?

# In[53]:


average_salary_by_SelfRatingLevel = Employee_Performance_Merged.groupby('SelfRatingLevel')['Salary'].mean().nlargest().reset_index()
print(average_salary_by_SelfRatingLevel)


# #Are employees who report to high-performing managers more likely to receive higher salaries?

# In[54]:


average_salary_by_ManagerRatingLevel = Employee_Performance_Merged.groupby('ManagerRatingLevel')['Salary'].mean().nlargest().reset_index()
print(average_salary_by_ManagerRatingLevel)


# #Do self-ratings align with manager's ratings ?

# In[55]:


ratings_comparison = Employee_Performance_Merged[['SelfRating', 'ManagerRating']].mean()
print(ratings_comparison)


# # Work-life Balance

# #Does working overtime impact work-life balance?

# In[56]:


overtime_worklife = Employee_Performance_Merged.groupby('OverTime')['WorkLifeBalance'].mean()
print(overtime_worklife)


# #What is the work-life balance within each department?

# In[57]:


Department_worklife = Employee_Performance_Merged.groupby('Department')['WorkLifeBalance'].mean()
print(Department_worklife)


# In[ ]:




