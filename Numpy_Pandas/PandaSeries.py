import pandas as pd
import numpy as np

def random_series(n = 10, seed = 42):
    rng  = np.random.default_rng(seed)
    values = rng.integers(low = 1, high = 100, size = n)
    return pd.Series(values)

def labeled_series(series):
    labels= [f"num_{i+1}" for i in range(len(series))]
    return pd.Series(series.values, index = labels)

def describe_series (s, title = "Series"):
    print (f"{title}")
    print (s)
    print (f"Shape      : {s.shape}")
    print (f"Dtype      : {s.dtype}")
    print (f"Size       : {s.size}")
    print (f"Index      : {list(s.index)}")

series = random_series()
print ("Series with default index   :")
describe_series(series)

labeled = labeled_series(series)
print ("Series with custom label    :")
describe_series(labeled, title = "Labeled Series")

#basic statistics
print ("Basic Statistics    :")
print ("Maximum     :", series.max())
print ("Minimum     :", series.min())
print ("Mean        :", series.mean())
print ("Sum         :", series.sum())

#sorted values
print ("Sorted Values   :")
print (series.sort_values().to_string())

#Indexing and filtering
print (f"First Value (series.iloc[0])   :   {series.iloc[0]}")
print ("Values greater than 50  :")
print (series[series > 50].to_string())