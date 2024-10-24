'''
In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |
You must use Pandas to answer the following questions:

How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
What is the average age of men?
What is the percentage of people who have a Bachelor's degree?
What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
What percentage of people without advanced education make more than 50K?
What is the minimum number of hours a person works per week?
What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
What country has the highest percentage of people that earn >50K and what is that percentage?
Identify the most popular occupation for those who earn >50K in India.
Use the starter code in the file demographic_data_analyzer.py. Update the code so all variables set to None are set to the appropriate calculation or code. Round all decimals to the nearest tenth.
'''


import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()


    # What is the average age of men?
    males=df[df['sex']=='Male']
    average_age_men=males['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_deg= df[df['education']=='Bachelors']
    percentage_bachelors = (bachelors_deg.count.shape[0]/df.shape[0])*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['Bachelors','Masters','Doctorate']]
    lower_education = df[!df['Bachelors','Masters','Doctorate']]

    # percentage with salary >50K
    higher_education_sal= higher_education['salary'=='>50K'].shape[0]
    higher_education_rich = (higher_education_sal/higher_education.shape[0])*100

    lower_education_sal=lower_education['salary'=='>50K'].shape[0]
    lower_education_rich = (lower_education_sal/lower_education.shape[0])*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = min_work_hours.shape[0]

    rich_percentage = num_min_workers[num_min_workers['salary']=='>50K'].shape[0]
    percent= (rich_percentage/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?

    #Calculate the total number of people in each country
    total_people_by_country = df['native-country'].value_counts()

    # Calculate the number of people earning more than $50K in each country
    highest_earning_country = df[df['salary'] > 50000]['native-country'].value_counts()

    # Calculate the percentage of people earning more than $50K in each country
    percentage_high_income_by_country = (high_income_by_country / total_people_by_country) * 100

    # Find the country with the highest percentage
    highest_earning_country_percentage = percentage_high_income_by_country.idxmax()



    # Identify the most popular occupation for those who earn >50K in India.
    

    # Filter the DataFrame to include only rows where the income is greater than $50K and the country is India
    high_income_india_df = df[(df['salary'] > 50000) & (df['native-country'] == 'India')]

    # Identify the most popular occupation for those who earn more than $50K in India
    top_IN_occupation = high_income_india_df['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

