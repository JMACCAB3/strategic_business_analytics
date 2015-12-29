#! usr/local/bin/python
# -*- coding: utf-8 -*-
"""
These scripts implement the Clustering Techniques module of the Coursera
course `Strategic Business Analytics` in Python's Pandas package for data
analysis. The scripts were originally intended for the R programming language.
"""
from __future__ import unicode_literals
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

from analytics_scripts import plt
from analytics_scripts import SBA_FILE_LOADER


# first, we are asked to calculate the correct mean and median of the
# coefficient of variations of the sales in the SKU dataset (DATA_2.01_SKU.csv)

# in order to do this, let's load the data into memory
sku_df = pd.read_csv(SBA_FILE_LOADER('clustering/DATA_2.01_SKU.csv'))

# and then calculate the mean and median of the CV field of sku_df
cv_mean = sku_df['CV'].mean()
cv_med = sku_df['CV'].median()
print "Mean of CV: {}\nMedian of CV: {}".format(cv_mean, cv_med)


# second, we are asked to do a hierarchical clustering on scaled data using an
# Euclidian distance and Ward.D clustering on the SKU dataset. What are the
# resulting segments if we decide to take only 2 clusters instead of 3?
# NOTE: "Crickets" are low volatility, low value SKUs
# NOTE: "Wild Bulls" are high volatility, high value SKUs
# NOTE: "Horses" are low volatility, high value SKUs

# since we're implementing in Pandas rather than R, we'll define a
# helper function scale() below to help us do some of the work
def scale(df, center=True, scale=True):
    """
    A helper function to normalize data in a pandas DataFrame. Standard in R.
    PER THE R DOCUMENTATION:
    If 'scale' is True, then scaling is done by dividing the centered columns
    of 'x' by their standard deviations if 'center' is True, and the root mean
    square otherwise. If 'scale' is False, no scaling is done.
    """
    if not isinstance(df, pd.DataFrame):  # let's validate df before we start
        return TypeError("df passed to scale() must be a DataFrame")

    if not len(df) > 0:
        return ValueError("df passed to scale() must not be empty")

    x = df.copy()  # let's make a copy of the DataFrame so we don't modify df

    if center:  # if center is True,
        x -= x.mean()  # let's subtract the mean from each element of x
    if scale and center:  # if center is True and scale is True,
        x /= x.std()  # let's divide each element of x by the std dev of x
    elif scale:  # if only scale is True,
        # let's take the root mean square of x
        x /= np.sqrt(x.pow(2).sum().div(x.count() - 1))
    return x


sku_df_scaled = scale(sku_df)  # let's scale sku_df using our scale function

# the AgglomerativeClustering class from sklearn.cluster can perform
# hierarchical clustering using the ward method

n_clusters = 2  # let's set the number of clusters we want to show as 2
# and perform the clustering of the scaled dataset using the fit method
ward = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean',
    linkage='ward').fit(sku_df_scaled)
colors = ward.labels_  # let's set our plot colors to be the cluster labels

# then let's plot the data with CV on the x_axis and ADS on the y_axis
plt.scatter(sku_df['CV'], sku_df['ADS'], s=100, c=colors)
# add some axes for clarity
plt.xlabel('Average Daily Sales')
plt.ylabel('Coefficient of Variance')
# and then show the plot
plt.show()


# third, we are asked which graph reports the correct plot of the last project
# evaluation as a function of the number of projects done for the HR dataset

# in order to do this, let's load the data into memory
hr_df = pd.read_csv(SBA_FILE_LOADER('clustering/DATA_2.02_HR.csv'))

# then let's plot the data with CV on the x_axis and ADS on the y_axis
plt.scatter(hr_df['LPE'], hr_df['NP'], s=100)
# add some axes for clarity
plt.xlabel('Last Project Evaluation')
plt.ylabel('Number of Projects')
# and then show the plot
plt.show()


# fourth, we are asked to cluster the HR dataset on Satisfaction, Project
# Evaluation and Number of Projects Done and that we keep 2 segments using
# the same values for the other specifications

# to do this, we'll reduce our HR dataset to only have the required fields
required_columns = ['S', 'LPE', 'NP']
hr_sub_df = hr_df[required_columns]

# then we'll scale our data like we did with sku_df
hr_sub_df_scaled = scale(hr_sub_df)

n_clusters = 2  # let's set the number of clusters we want to show as 2
# and perform the clustering of the scaled dataset using the fit method
ward = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean',
    linkage='ward').fit(hr_sub_df_scaled)

# this time, let's add a segment field to hr_sub_df to categorize it
hr_df['segment'] = ward.labels_

# then we'll take the median Satisfaction for each segment
med = hr_df.groupby('segment').S.median()
print "The median of segment 0 is {}\nThe median of segment 1 is {}".format(
    med[0], med[1])
