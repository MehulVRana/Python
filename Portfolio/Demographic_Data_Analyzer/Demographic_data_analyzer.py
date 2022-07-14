# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:55:27 2022

@author: jindo
"""

import pandas as pd


def calculate_demographic_data(print_data=True):
    ''' 
        Reads the adult.data.csv and calculates the race value counts, average 
        age of men, percentage of people with bachelors degree, percentage of
        people with a higher education that earn more than >50K, percentage of 
        people without a higher education that earn more than >50K, the lowest 
        amount of hours anyone works, percentage of people who earn >50K among 
        those who work fewest hours, the country with the highest percentage of
        people who earn >50K, the percentage associated with the country with 
        the highest percentage of people who earn >50K, and the most popular 
        occupation for those who earn >50K in India
      
        Args:
            print_data (bool): bool if True prints the results.

        Returns:
            dict : 'race_count': Number of each race,
            'average_age_men': Average age of men,
            'percentage_bachelors': Percentage with Bachelors degrees,
            'higher_education_rich': Percentage with higher education that earn >50K,
            'lower_education_rich': Percentage without higher education that earn >50K,
            'min_work_hours': min hours worked,
            'rich_percentage': Percentage of rich among those who work fewest hours,
            'highest_earning_country': Country with highest percentage of rich,
            'highest_earning_country_percentage': Country with highest percentage of rich
            'top_IN_occupation': Top occupations in India
    '''
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a 
    # Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_mask = df['sex']=='Male'
    average_age_men = df[male_mask]['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    entries = len(df.index)
    bach_mask = df['education'] == 'Bachelors'
    percentage_bachelors = 100 * bach_mask.sum()/entries

    # What percentage of people with advanced education (`Bachelors`, `Masters`
    #, or `Doctorate`) make more than 50K?
    high_edu_mask = (
        df['education'] == 'Bachelors')|(
            df['education'] == 'Masters')|(
                df['education'] == 'Doctorate')
    
    # What percentage of people without advanced education make more than 50K?
    low_edu_mask = high_edu_mask == False
    hi_earners_mask = df['salary'] == '>50K'
    low_edu_hi_earners = hi_earners_mask[low_edu_mask]
    hi_edu_hi_earners = hi_earners_mask[high_edu_mask]
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    higher_education_rich = 100 * hi_edu_hi_earners.sum()/high_edu_mask.sum()
    lower_education_rich = 100 * low_edu_hi_earners.sum()/low_edu_mask.sum()

    # What is the minimum number of hours a person works per week 
    # (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per 
    # week have a salary of >50K?
    min_hour_mask = df['hours-per-week']==df['hours-per-week'].min()
    hi_earn_min_hour_mask = df[min_hour_mask]['salary'] == '>50K'
    sum_min_hour_workers = min_hour_mask.sum()
    rich_percentage = 100 * hi_earn_min_hour_mask.sum()/sum_min_hour_workers

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].value_counts()
    hi_earners_by_country = df[hi_earners_mask]['native-country'].value_counts()
    percentages_of_high_earners_by_country = 100 * hi_earners_by_country / countries
    percentages_of_high_earners_by_country_sorted =  percentages_of_high_earners_by_country.sort_values(ascending = False)
    highest_earning_country = percentages_of_high_earners_by_country_sorted.index[0]
    highest_earning_country_percentage = percentages_of_high_earners_by_country_sorted.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_mask = df['native-country'] == 'India'
    high_earners_in_india = hi_earners_mask[india_mask]
    mode_of_high_paid_indian_jobs = df[india_mask][high_earners_in_india]['occupation'].mode()
    top_IN_occupation = mode_of_high_paid_indian_jobs[0]

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

calculate_demographic_data(print_data=True)

