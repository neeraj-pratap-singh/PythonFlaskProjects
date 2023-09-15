import pandas as pd

# Create a sample CSV file content as a multi-line string
csv_content = """Name,Age,Gender,Salary
Alice,34,Female,52000
Bob,45,Male,72000
Charlie,23,Male,22000
David,31,Male,47000
Eve,29,Female,61000
"""

# Save the CSV content to a file
with open('sample_data.csv', 'w') as f:
    f.write(csv_content)

# Read the CSV file into a DataFrame
df = pd.read_csv('sample_data.csv')

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("="*50)

# Filter rows where Age > 30 and Salary > 50000
filtered_df = df[(df['Age'] > 30) & (df['Salary'] > 50000)]

# Display the filtered DataFrame
print("Filtered DataFrame (Age > 30 and Salary > 50000):")
print(filtered_df)
print("="*50)

# Calculate the average salary for each gender
avg_salary_by_gender = df.groupby('Gender')['Salary'].mean()

# Display the average salary by gender
print("Average Salary by Gender:")
print(avg_salary_by_gender)
print("="*50)

# Add a new column "Salary_Bucket" based on Salary
df['Salary_Bucket'] = pd.cut(df['Salary'], bins=[20000, 40000, 60000, 80000], labels=['Low', 'Medium', 'High'])

# Display the DataFrame with the new column
print("DataFrame with Salary Bucket:")
print(df)
