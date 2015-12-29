#! usr/local/bin/python
# -*- coding: utf-8 -*-
"""
These scripts implement the Correlation Techniques module of the Coursera
course `Strategic Business Analytics` in Python's Pandas package for data
analysis. The scripts were originally intended for the R programming language.
"""
from __future__ import unicode_literals
import pandas as pd

import statsmodels.api as sm
import statsmodels.formula.api as smf

from analytics_scripts import line_maker
from analytics_scripts import plt
from analytics_scripts import SBA_FILE_LOADER


end_of_question = line_maker()

# # for the first two questions, we are asked to assess the truth value
# # of multiple statements posed based on a regression analysis of credit_df

# # in order to do this, let's load the data into memory
# credit_df = pd.read_csv(SBA_FILE_LOADER('correlation/DATA_3.01_CREDIT.csv'))

# # in order for us to understand the orders of magnitude of our variables,
# # we'll summarize our numerical variables set using the describe function
# print "Summarized Credit Rating Data:\n"
# print credit_df.describe()
# print end_of_question

# # let's then calculate the correlations between our variables, excluding the
# # non-numerical variables from our dataset
# num_vars = ['Income', 'Rating', 'Cards', 'Age', 'Education', 'Balance']
# clean_credit_df = credit_df[num_vars]  # subset credit_df to be numerical vars
# corr_credit_df = clean_credit_df.corr()  # then calculate the correlations
# print "Credit Rating Data Correlation Matrix:\n"
# print corr_credit_df  # now print out the correlation matrix
# print end_of_question

# # in order to answer question 1 we'll calculate a linear regression of
# # credit_df; in this case, we'll use the statsmodels module
# # NOTE: if a variable is a categorical integer, use the C() operator
# formula = "Rating ~ Income + Cards + Age + Education + Gender + \
#     Student + Married + Ethnicity + Balance"
# linreg_model = smf.ols(formula=formula, data=credit_df).fit()
# print "Linear Regression Formula: {}".format(formula)
# print linreg_model.summary()  # print the linear regression model summary
# print end_of_question

# # then let's plot the fitted values against the actuals,
# plt.scatter(credit_df.Rating, linreg_model.fittedvalues, s=100)
# # add some axes for clarity,
# plt.xlabel('Actuals')
# plt.ylabel('Fitted Values')
# # and then show the plot
# plt.show()


# # for the third question, we are asked to assess the truth value
# # of multiple statements posed based on a regression of the
# # subsetted variables Income, Cards, and Married from credit_df
# subset_linreg_model = smf.ols(formula='Rating ~ Income + Cards + Married',
#     data=credit_df).fit()
# print subset_linreg_model.summary()  # print the model summary
# print end_of_question

# for questions four and five, we are asked to answer questions on the HR data

# in order to do this, let's load the data into memory
hr_df = pd.read_csv(SBA_FILE_LOADER('correlation/DATA_3.02_HR2.csv'))

# in order for us to understand the orders of magnitude of our variables,
# we'll again summarize our numerical variables set using describe()
print "Summarized HR Data:\n"
print hr_df.describe()

# since our fourth question involves the number of employees who've left,
# let's first count the number of employees who have and have not left
exit_data = hr_df.left.value_counts()
print "The number of employees who have stayed is: {}\nThe number of employees\
    who have left is: {}".format(exit_data[0], exit_data[1])
print end_of_question

# let's again calculate the correlations between our variables
corr_hr_df = hr_df.corr()
print "HR Data Correlation Matrix:\n"
print corr_hr_df  # and then print out the correlation matrix
print end_of_question

# you'll note in this case that the correlation matrix is not as useful. We
# are concerned with how the variables interact with one another, not their
# correlation in isolation; to compensate, we'll use a logistic regression
formula = "left ~ S + LPE + NP + ANH + TIC + C(Newborn)"
print "Linear Regression Formula: {}".format(formula)
logitreg_model = smf.glm(formula=formula,
    data=hr_df, family=sm.families.Binomial()).fit()
print logitreg_model.summary()  # print the model summary

# the output of a logistic regression model is a probability
# and we can plot a histogram of these fitted probabilities
plt.hist(logitreg_model.fittedvalues)
plt.xlabel('Probability of Employee Having Left The Company')
plt.ylabel('Number of Employees Projected')
plt.show()

# we can use this histogram to help set a cutoff value above which an employee
# is assumed likely to leave the company; let's set our cutoff value as 0.5
cutoff = 0.5
# and compute the percentage of correctly classified employees who stayed,
correct_stayed = sum((logitreg_model.fittedvalues <= cutoff) &  \
    (hr_df.left == 0)) / float(sum(hr_df.left == 0))
print "Percentage of correctly classed employees who stayed: {}".format(
    correct_stayed)
# the percentage of correctly classified employees who left,
correct_left = sum((logitreg_model.fittedvalues > cutoff) & \
    (hr_df.left == 1)) / float(sum(hr_df.left == 1))
print "Percentage of correctly classed employees who left: {}".format(
    correct_left)
# and the percentage of correctly classified employees overall
correct_tot = sum((logitreg_model.fittedvalues > cutoff) == (\
    hr_df.left == 1)) / float( \
    len((logitreg_model.fittedvalues > cutoff) == (hr_df.left == 1)))
print "Percentage of correctly classed employees: {}".format(
    correct_tot)
print end_of_question
