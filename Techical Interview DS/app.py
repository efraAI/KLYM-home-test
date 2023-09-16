# %% [markdown]
# # Importing libraries
# 

# %%
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.stats import f_oneway
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.ensemble import RandomForestRegressor
# import xgboost as xgb
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# from sklearn.preprocessing import StandardScaler
# import random
# import joblib


print("""
The purpose of this app.py is to demonstrate how we can easily deploy our best machine learning model using a Docker container. This deployment allows us to:

Host the model on various platforms, including cloud services like AWS, Google Cloud, or Azure.
Expose the model through a designated port using HTTP requests.
To achieve this, we create a Flask application that transforms each new entry.

Within this Flask app, we load the saved model in the .pkl format. This architecture facilitates seamless deployment and accessibility of our model.

""")
print ("Efrain Galvis")

# %%



