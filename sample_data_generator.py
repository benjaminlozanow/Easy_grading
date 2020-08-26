import pandas as pd
import random

## Generate columns for score dataframe

# Sample students
sample_students = []
for i in range(1,101):
    sample_students.append("Student " + str(i))

# Sample score 1 based on random selection
random_score = []
for i in range(1,101):
    random_score.append(random.randint(0,100))

# Sample score 2 based on a Normal distribution
normal_score = []
while len(normal_score) < 100:
    temporal_score = 0
    temporal_score = random.normalvariate(60,10)
    if temporal_score >= 0 and temporal_score <= 100:
        normal_score.append(round(temporal_score,2))

# Sample score 3 based on a Gamma distribution
gamma_score = []
while len(gamma_score) < 100:
    temporal_score = 0
    temporal_score = random.gammavariate(2,2)
    if temporal_score >= 0 and temporal_score <= 10:
        gamma_score.append(round(temporal_score,2))

## Buid dataframe

# Dictionary as a base for the dataframe
score_dictionary = {
"Student": sample_students,
"Score Random": random_score,
"Score Normal": normal_score,
"Score Gamma": gamma_score
}

# Dataframe with Pandas
score_dataframe = pd.DataFrame(score_dictionary)
cols = ['Student', 'Score Random', 'Score Normal', 'Score Gamma']
score_dataframe = score_dataframe[cols]

# Export dataframe as a csv file
score_dataframe.to_csv("sample_score_data.csv", index = False)
