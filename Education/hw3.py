"""
Avery Lee
CSE 163 AB
This program implements the functions for HW Education.
File: 'nces-ed-attainment.csv'; this file contains info about education
Performs analyses comparing type and percentage of education
throughout the years of different sexes and races.
Examples include comparing percentage of sexes that earned a bachelors,
most commonly awarded degrees for a certain demographic,
and plotting line plots and bar charts comparing degrees
to different demograhics.
"""


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

sns.set()


# Define your functions here
def compare_bachelors_1980(data):
    """
    parameter: dataframe
    returns: a 2x2 dataframe with Sex and Total as columns,
    of the percentage for women vs men
    having earned a Bachelor's degree in 1980.
    """
    # PICK ROWS
    # remove Sex 'A' (only keep 'M' and 'F'), only Year 1980, only bachelor's
    data = data[(data['Sex'] != 'A') &
                (data['Year'] == 1980) &
                (data['Min degree'] == 'bachelor\'s')]
    # PICK COLS
    # just Sex and Total
    data = data[['Sex', 'Total']]

    return pd.DataFrame(data)


def top_2_2000s(data, sex='A'):
    """
    parameter: dataframe, sex with default 'A'
    returns: a 2-element Series of the most commonly-awarded education levels
    between 2000-2010 inclusive for a given sex, and its means.
    """
    # only Sex indicated, only Year 2000-2010 inclusive
    data = data[(data['Sex'] == sex) &
                (data['Year'] >= 2000) &
                (data['Year'] <= 2010)]
    degrees_series = data.groupby('Min degree')['Total'].mean()
    degrees_series = degrees_series.nlargest(2)  # the 2 largest values
    return degrees_series


def line_plot_bachelors(data):
    """
    parameter: dataframe
    plots: a line chart of the total percentages of all people Sex 'A'
    with bachelor's 'Min degree' over time.
    """
    # only Sex A and Min degree bachelors
    df = data[(data['Sex'] == 'A') & (data['Min degree'] == 'bachelor\'s')]

    # make plot
    sns.relplot(x='Year', y='Total', data=df, kind='line')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title('Percentage Earning Bachelor\'s over Time')

    # save plot
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    """
    parameter: dataframe
    plots: a bar chart of total percentages of Sex (F, M, A) with
    Min degree high school in Year 2009.
    """
    # only Year 2009, only Min degree high school
    df = data[(data['Year'] == 2009) &
              (data['Min degree'] == 'high school')]

    # make plot
    sns.catplot(x='Sex', y='Total', data=df, kind='bar')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.title('Percentage Completed High School by Sex')

    # save plot
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    parameter: dataframe
    plots: a line plot of percentage of Hispanics with degrees
    1990-2010 inclusive for high school and barchelors.
    """
    # only Year 1990-2010 inclusive, only Min degree high school or bachelors
    print(data)
    df = data[(data['Year'] >= 1990) &
              (data['Year'] <= 2010) &
              ((data['Min degree'] == 'high school') |
              (data['Min degree'] == 'bachelor\'s'))]

    # make plot
    # separate color of line based on degree
    sns.relplot(x='Year', y='Hispanic', data=df, hue='Min degree', kind='line')
    plt.xlabel('Year')
    plt.xticks(rotation=45)
    plt.ylabel('Percentage')
    plt.title('Hispanic Percentage of Degrees from 1990 to 2010')

    # save plot
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    parameter: dataframe
    returns: the test mean squared error (float), after
    predicting the percentage of Sex to achieve the Min degree in a given Year.
    """
    # PREPROCESSING
    # filter to only include Year, Min degree, Sex, and total
    data = data[['Year', 'Min degree', 'Sex', 'Total']]
    # drop rows with missing data
    data = data.dropna()

    # MODEL TRAINING
    # features and labels
    features = data.loc[:, data.columns != 'Total']
    features = pd.get_dummies(features)  # dealing with categorical data
    labels = data['Total']

    # split into 80% training, 20% testing
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)

    # modeling
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    test_predictions = model.predict(features_test)
    test_mean_squared_error = mean_squared_error(labels_test, test_predictions)

    return test_mean_squared_error


def main():
    """
    main method of the Education Assessment.
    """
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    sns.set()
    # Call your functions here
    compare_bachelors_1980(data)
    top_2_2000s(data, 'A')  # 'A', 'F', or 'M'
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
