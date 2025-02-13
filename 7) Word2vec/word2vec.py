# -*- coding: utf-8 -*-
"""Word2Vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Co4NlABnjB85X4NLF0X8Y7VGS-4bZbTi
"""

!pip install gensim

from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
import numpy as np

import pandas as pd
data_path = 'clean_news.csv'
df = pd.read_csv(data_path, error_bad_lines=False)

# Display the first 10 rows of the DataFrame
df.head(10)

from gensim.models import Word2Vec

# Set the length of the word vectors
vector_size = 100

# Create a Word2Vec model and train it on the text data
w2v_model = Word2Vec(df['Body'].apply(lambda x: x.split()), vector_size=vector_size, min_count=1)

# Display the w2v_model object
print(w2v_model)

"""LOGISTIC REGRESSION

"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#Split the data into X and y.
X = df['Body']
y = df['Label']

# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data using the previously trained Word2Vec model.
X_train_vec = []
for x in X_train:
    vecs = [w2v_model.wv[word] for word in x.split() if word in w2v_model.wv.key_to_index]
    if len(vecs) == 0:
        vecs = [np.zeros(w2v_model.vector_size)]
    elif len(vecs) < 100:
        padding = [(0, 100 - len(vecs)), (0, 0)]
        vecs = np.pad(vecs, padding, mode='constant')
    X_train_vec.append(np.mean(vecs, axis=0))

X_test_vec = []
for x in X_test:
    vecs = [w2v_model.wv[word] for word in x.split() if word in w2v_model.wv.key_to_index]
    if len(vecs) == 0:
        vecs = [np.zeros(w2v_model.vector_size)]
    elif len(vecs) < 100:
        padding = [(0, 100 - len(vecs)), (0, 0)]
        vecs = np.pad(vecs, padding, mode='constant')
    X_test_vec.append(np.mean(vecs, axis=0))

X_train_vec = np.vstack(X_train_vec)
X_test_vec = np.vstack(X_test_vec)


# Create a logistic regression model
lr = LogisticRegression(max_iter=10000)

# Train the model
lr.fit(X_train_vec, y_train)

# Make predictions on the test data
y_pred_lr = lr.predict(X_test_vec)



# Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Precision:", precision_score(y_test, y_pred_lr, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_lr, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_lr, average='weighted'))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred_lr)
print("Confusion Matrix:")
print(cm)

from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred_lr)
print("Classification Report:")
print(report)

# Display the contents of the X_train_vec variable
print(X_train_vec)

# Display the contents of the X_test_vec variable
print(X_test_vec)

# Get the number of items in the X_test_vec object
len(X_test_vec)

# Get the number of items in the X_train_vec object
len(X_train_vec)

"""DECISION TREE"""

from sklearn.tree import DecisionTreeClassifier

# Create a decision tree classifier
dt = DecisionTreeClassifier()

# Train the model on the vectorized training data
dt.fit(X_train_vec, y_train)

# Make predictions on the vectorized test data
y_pred_dt = dt.predict(X_test_vec)

# Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Precision:", precision_score(y_test, y_pred_dt, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_dt, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_dt, average='weighted'))

from sklearn.metrics import confusion_matrix, classification_report

# Confusion Matrix
cm_dt = confusion_matrix(y_test, y_pred_dt)
print("Confusion Matrix:")
print(cm_dt)

# Classification Report
report_dt = classification_report(y_test, y_pred_dt)
print("Classification Report:")
print(report_dt)

"""RANDOM FOREST"""

from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier with 100 trees
rf = RandomForestClassifier(n_estimators=100)

# Train the model on the vectorized training data
rf.fit(X_train_vec, y_train)

# Make predictions on the vectorized test data
y_pred_rf = rf.predict(X_test_vec)

# Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Precision:", precision_score(y_test, y_pred_rf, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_rf, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_rf, average='weighted'))

from sklearn.metrics import confusion_matrix, classification_report

# Confusion Matrix
cm_rf = confusion_matrix(y_test, y_pred_rf)
print("Confusion Matrix:")
print(cm_rf)

# Classification Report
report_rf = classification_report(y_test, y_pred_rf)
print("Classification Report:")
print(report_rf)

"""GRADIENT BOOSTING"""

from sklearn.ensemble import GradientBoostingClassifier

# Create a gradient boosting classifier
gb = GradientBoostingClassifier()

# Train the model on the vectorized training data
gb.fit(X_train_vec, y_train)

# Make predictions on the vectorized test data
y_pred_gb = gb.predict(X_test_vec)

# Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_gb))
print("Precision:", precision_score(y_test, y_pred_gb, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_gb, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_gb, average='weighted'))

# Confusion Matrix
cm_gb = confusion_matrix(y_test, y_pred_gb)
print("Confusion Matrix:")
print(cm_gb)

# Classification Report
report_gb = classification_report(y_test, y_pred_gb)
print("Classification Report:")
print(report_gb)

"""SUPPORT VECTOR MACHINE"""

from sklearn.svm import SVC

# Create a support vector machine classifier
svm = SVC()

# Train the model on the vectorized training data
svm.fit(X_train_vec, y_train)

# Make predictions on the vectorized test data
y_pred_svm = svm.predict(X_test_vec)

# Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print("Precision:", precision_score(y_test, y_pred_svm, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_svm, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_svm, average='weighted'))

cm_svm = confusion_matrix(y_test, y_pred_svm)
report_svm = classification_report(y_test, y_pred_svm)

print("Confusion Matrix:")
print(cm_svm)
print("Classification Report:")
print(report_svm)

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier

# Create a k-nearest neighbors classifier and train it on the vectorized training data
knn = KNeighborsClassifier()
knn.fit(X_train_vec, y_train)

# Make predictions on the vectorized test data
y_pred_knn = knn.predict(X_test_vec)

# Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Precision:", precision_score(y_test, y_pred_knn, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_knn, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_knn, average='weighted'))

cm_knn = confusion_matrix(y_test, y_pred_knn)
report_knn = classification_report(y_test, y_pred_knn)

print("Confusion Matrix:")
print(cm_knn)
print("Classification Report:")
print(report_knn)

"""NAIVE BAYES"""

from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB

# Perform min-max scaling on the training and test data
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train_vec)
X_test_scaled = scaler.transform(X_test_vec)

# Apply log transformation to the scaled data
X_train_log = np.log(X_train_scaled + 1)
X_test_log = np.log(X_test_scaled + 1)

# Create and train a Naive Bayes model
nb = MultinomialNB()
nb.fit(X_train_log, y_train)

# Make predictions on the test data
y_pred_nb = nb.predict(X_test_log)

# Calculate and print evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred_nb))
print("Precision:", precision_score(y_test, y_pred_nb, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_nb, average='weighted'))
print("F1 score:", f1_score(y_test, y_pred_nb, average='weighted'))

cm_nb = confusion_matrix(y_test, y_pred_nb)
report_nb = classification_report(y_test, y_pred_nb)

print("Confusion Matrix:")
print(cm_nb)
print("Classification Report:")
print(report_nb)