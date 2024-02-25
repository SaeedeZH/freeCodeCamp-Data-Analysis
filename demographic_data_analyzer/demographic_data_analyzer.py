import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    dataset = pd.read_csv('./projects/demographic_data_analyzer/adult.csv', delimiter=',', header=None)
    # Set columns
    dataset.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital-status', 'occupatoin', 'relationship', 
                   'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-weak', 'native-country','salary' ]

    # How many people of each race are represented in this dataset?# This should be a Pandas series with race names as the index labels. (race column)
    race_series = dataset['race']  # return a series type!
    race_count = race_series.value_counts()

    # What is the average age of men?
    mask = (dataset['sex'] ==' Male')   
    average_age_men = round(dataset[mask]['age'].mean(),1)

    # What is the pceerntage of people who have a Bachelor's degree?
    mask = dataset['education'] == ' Bachelors'
    bach_count = len(dataset[mask])
    percentage = bach_count/ len(dataset) * 100
    percentage_bachelors = round(percentage,1)
    # or:
    # percentage_bachelors = round(dataset[dataset['education'] == ' Bachelors'].shape[0] / dataset.shape[0] * 100, 1)


    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # mask_1 = (dataset['education'] == ' Bachelors') | (dataset['education']==' Masters') | (dataset['education']== ' Doctorate')
    # or : optimal code

    mask_1 = dataset['education'].isin([' Bachelors', ' Masters', ' Doctorate' ])
    mask_2 = dataset['salary'] == ' >50K'

    higher_education_rich = round(((mask_1 & mask_2).sum() /mask_1.sum() ) *100,1)
    lower_education_rich = round(((~mask_1 & mask_2).sum() /(~mask_1).sum() ) *100,1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = dataset['hours-per-weak'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours = dataset['hours-per-weak'].min()
    
    # not optimal code
    
    # mask = dataset['hours-per-weak'] == min_hours
    # num_min_workers = len(dataset[mask])
    # temp_ds = dataset[mask]
    # mask_1 = temp_ds['salary'] == ' >50K'
    # high_salary_count = len(temp_ds[mask_1])
    # rich_percentage =int(high_salary_count/ num_min_workers * 100)

    # optimal code
    mask_1 = dataset['hours-per-weak'] == min_hours
    rich_percentage = round(((mask_1 & mask_2).sum() /mask_1.sum()) * 100, 1)

    # What country has the highest percentage of people that earn >50K?

    # not optimal code
    # count_w = dataset['native-country'].value_counts()
    # mask = dataset['salary'] == ' >50K'
    # new_df = dataset[mask]
    # count_salary = new_df['native-country'].value_counts()
    # count_res = count_salary / count_w * 100

    # optimal code
    count_res = (dataset[mask_2]['native-country'].value_counts() / dataset['native-country'].value_counts() * 100)

    highest_earning_country = count_res.idxmax()
    highest_earning_country_percentage = round(count_res.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask = (mask_2) & (dataset['native-country'] == ' India')
    new_ds = dataset[mask]
    top_IN_occupation = new_ds['occupatoin'].value_counts().idxmax()

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


