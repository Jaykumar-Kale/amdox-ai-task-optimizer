import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
df = pd.read_csv("data/employee_emotions.csv")

X = df["text"]
y = df["emotion"]

# Vectorization
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model
pickle.dump((model, vectorizer), open("model/emotion_model.pkl", "wb"))

print("Model trained successfully")
