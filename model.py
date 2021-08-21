import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

df = pd.read_csv("cloth_size_data.csv")
#use required features

df['age'].replace('', np.nan, inplace=True)
df['height'].replace('', np.nan, inplace=True)
df.dropna(subset=['height'], inplace=True)
df.dropna(subset=['age'], inplace=True)



v=df.replace(to_replace=["XXS","S","M","L","XL","XXL","XXXL"],value=["1","2","3","4","5","6","7"])


x = v[['weight','age','height']]
y = v['size']
#Training Data and Predictor Variable
# Use all data for training (tarin-test-split not used)
x = v.iloc[:, :3]
y = v.iloc[:, -1]
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(x, y)

# Saving model to current directory
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(regressor, open('cloth_size.pkl','wb'))

