# Basic import set

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This will help me figure out the encording I need to use
import chardet
chardet.detect(rawdata)

# Alternatively in UNIX I can run:
# file xxx.tsx

# After you read in the columns.

df.columns
# Output will be columns name

df.describe()
# Will give basic statistics.

df.info()
# Will tell me the types of items are in the df

# Be careful with different types because Python cant import null integers

# Converting Types
df.column = df.column.astype(int)

# Kind of nothing

pd.read_csv(..., na_values=["N/A", "Unknown"])
# or
df.replace("N/A", None)

# Dropping nulls
df.dropna(axis=1, how="all")

# You can take the True/False series and stick it back into the dataframe to see only the matching information.
expensive_stuff = df.X > 100000
df[expensive_stuff]


df.<column name>.value_counts()

# Pivoting
df.pivot(index="date", columns='variables', values='')

# Merging

#import fuzzywuzzy and jellyfish
fuzz.ratio("this is a test", "this is a test1")
# Will return how close the match is

data = json

json_normalize(df, <The nested part>)
json_normalize(df, <the nested part>, [the additional data])