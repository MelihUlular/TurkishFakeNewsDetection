# -*- coding: utf-8 -*-
"""Data_ Preparation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/143izunPt6nW6JVEUjUiWDMYGB7HIYKXL

In this notebook,we try to combine 2 different fake.csv and real.csv files. This files consist fake and real news from Zaytung and Hurriyet.

Text files link: https://github.com/sfkcvk/TurkishFakeNewsDataset
"""

import pandas as pd
import numpy as np

data_path = 'Fake.csv'
fake = pd.read_csv(data_path, error_bad_lines=False)

data_path = 'Real.csv'
real = pd.read_csv(data_path, error_bad_lines=False)

fake.shape

real.shape

fake.head()

real.head()

"""Labelling fake and real dataframe before the concatination in one dataframe

Fake News -> "yalan" or 0

Real News -> "gerçek" or 1
"""

fake["Label"] = "yalan"   
real["Label"] = "gerçek"

news = pd.concat([fake,real])

news.head()

news = news.sample(frac = 1)  #shuffle the dataframe

news.head()

news.shape

"""Fake and Real News Distrubution comprassion using matplot library"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# making a bar plot to count the frequency of 
# fake and real news
sns.countplot(x='Label', 
              data=news,
              palette=['#0e2f44', '#800000'],
              saturation=2)
sns.despine()
plt.xticks([0,1], ['Real', 'Fake'])
plt.title('Fake and Real News Distribution');

"""This means that we have 2293 Real and 2162 Fake news data"""

label_counts = news['Label'].value_counts()

label_counts

"""Save the dataframe as a .csv file before the preprocessing steps"""

news.to_csv('news.csv', index=False, encoding='utf-8-sig')