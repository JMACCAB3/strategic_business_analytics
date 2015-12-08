#! usr/local/bin/python
from os.path import abspath, dirname, join
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

# let's define a helper function that will build a shortcut for our filepaths
SBA_FILE = lambda *path: join(abspath('/Users/joshmaccabee/Projects/' \
    'strategic_business_analytics/fixtures'), *path)

###############################################
# now let's begin the analysis for the course #
# instead of R, we'll use Python's Pandas pkg #
# for our analysis and matplotlib for graphs  #
###############################################

# first, we are asked to calculate the correct mean and median of the
# coefficient of variations of the sales in the SKU dataset (DATA_2.01_SKU.csv)

# in order to do this, let's load the data into memory
sku_df = pd.read_csv(SBA_FILE('DATA_2.01_SKU.csv'))

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

# since we're implementing in Pandas rather than R, let's first define some
# helper functions to help us do some of the work built in to R
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

sku_df_scaled = scale(sku_df)
plt.scatter(sku_df_scaled['ADS'], sku_df_scaled['CV'])
plt.show()