#! usr/local/bin/python
# -*- coding: utf-8 -*-
"""
These scripts implement the Correlation Techniques module of the Coursera
course `Strategic Business Analytics` in Python's Pandas package for data
analysis. The scripts were originally intended for the R programming language.
"""
from __future__ import unicode_literals
import pandas as pd

#import statsmodels.api as sm
import statsmodels.formula.api as smf

from analytics_scripts import plt
from analytics_scripts import SBA_FILE_LOADER


# first, we are asked to assess the truth value of multiple statements
# posed: the R-squared of the regression, as well as the directional impact
# of the education, balance, and gender variables on credit rating, as well
# as the directional impact of the student and income binaries on credit

# in order to do this, let's load the data into memory
credit_df = pd.read_csv(SBA_FILE_LOADER('correlation/DATA_3.01_CREDIT.csv'))

# in order for us to understand the orders of magnitude of our variables,
# we'll summarize our numerical variables set using the describe function
print credit_df.describe()

# since the credit rating variable is key to our analysis, let's plot a
# histogram graph of that variable to see its distribution
plt.hist(credit_df.Rating)  # set Rating as our variable to plot
plt.show()  # then let's show the plot

# let's then calculate the correlations between our variables, excluding the
# non-numerical variables from our dataset
num_vars = ['Income', 'Rating', 'Cards', 'Age', 'Education', 'Balance']
clean_credit_df = credit_df[num_vars]  # subset credit_df to be numerical vars
corr_credit_df = clean_credit_df.corr()  # then calculate the correlations
print corr_credit_df  # now print out the correlation matrix

# in order to answer question 1 we'll calculate a linear regression of our
# credit rating dataset; in this case, we'll use the statsmodels module

### THIS LINE FAILS - NEED TO FIGURE OUT WHY ###
x_vars = credit_df.columns.tolist()
x_vars.remove('Rating')
linreg_model = smf.OLS(credit_df.Rating, credit_df[x_vars]).fit()
print linreg_model.summary()  # print the linear regression model summary

### ALSO NEED TO FIGURE OUT A WAY TO PLOT THE FITTED VALUES VS THE ACTUALS ###
# we can also plot the fitted values versus the actuals
#fig, ax = plt.subplots()  # subplots returns a figure and the axes
#fig = sm.graphics.plot_fit(linreg_model, ax=ax)
#plt.show()
