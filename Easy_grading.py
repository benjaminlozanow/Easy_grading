import pandas as pd
import sys

# The score dataframe (.csv) has to be passed as an argument while executing Easy_grading.py
second_argument = sys.argv[1]

# Load csv score dataframe
score_df = pd.read_csv(second_argument)

# Function for the user inputs
def user_input(colname):
    column_use = input("Do you want to calculate grades for " + colname + "? (y/n)")
    if column_use.lower() == 'y' or column_use.lower() == 'yes':
        max_score = int(input("What is the maximum score for this test?"))
        percentage = int(input("What is the minimum score percentage (just the number) for approval? (60% or 50% are commonly used)"))
    else:
        print("Let's skip the column then")
        max_score = 0
        percentage = 0
    return max_score, percentage


# Function that calculates the grade for each score
def grade_calculator(score, max_score, percentage):
    min_grade = 1.0
    max_grade = 7.0
    approval_grade = 4.0
    e = percentage/100
    if score < e * max_score:
        grade = (approval_grade - min_grade) * (score / (e * max_score)) + min_grade
    elif score >= e * max_score:
        grade = (max_grade - approval_grade) * ((score - e * max_score) / (max_score * (1 - e))) + approval_grade
    else:
        print("Something went wrong, try again")
    return (round(grade,2))

# Iterates through the desired columns with user_input() and apply grade_calculator()
for i in range(1,len(score_df.columns)):
    max_score, percentage = user_input(score_df.columns[i])
    if not (max_score == 0) and not (percentage == 0):
        score_df['Grade of ' + score_df.columns[i]] = score_df[score_df.columns[i]].apply(grade_calculator, args = (max_score, percentage))

# Saves grades to a csv file
score_df.to_csv("sample_grades_output_data.csv", index = False)
