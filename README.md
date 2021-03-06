# Easy_grading

Easy grading provides the code required for calculating chilean grades from a score dataframe. It also provides an automatic graphical representation of them with the minimum summary statistics required for test analysis.

## Why Easy_grading?

Chilean grades calculation is not as straight forward as one might think. Easy_grading helps solving the task with an user-friendly code that helps educators obtain grades and the respective analysis in a rapid manner.

## Files

The [sample_data_generator.py](https://github.com/benjaminlozanow/Easy_grading/blob/master/sample_data_generator.py) generates a sample dataframe ([sample_score_data.csv](https://github.com/benjaminlozanow/Easy_grading/blob/master/sample_score_data.csv)) that can be used for grade calculation and representation. Contains four columns 1) Student, represents 100 course students; 2) Score Random, represents the score obtained by each student from pseudo-random number between 0 and 100 points; 3) Score Normal, represents the score obtained by each student from a Normal distribution of mean 60 and standard deviation 10; 4) Score Gamma, represents the score obtained by each student from a Gamma distribution of alpha 2 and beta 2 with a maximum score of 20.

The [Easy_grading.py](https://github.com/benjaminlozanow/Easy_grading/blob/master/Easy_grading.py) takes a score csv dataframe as input and asks for the maximum score of a test and the score percentage for approval. Then it calculates the grades for the desired columns and outputs the original dataframe with the grades' columns appended.

## Usage  

In the terminal run:  

```
python3 Easy_grading.py <score_csv_dataframe.csv>

```

Then follow the instructions for the different inputs asked.

## Contribution

Feel free to optimize/modify the code to have better or different results.

## License

MIT
