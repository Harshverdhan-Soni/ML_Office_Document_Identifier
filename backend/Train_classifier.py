import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# === Step 1: Load your dataset ===
# The CSV should have columns: 'text', 'label'
df = pd.read_csv("training_data.csv", encoding="ISO-8859-1")  # replace with your dataset file
df = df.dropna()
df= df.fillna("")
X = df['text'].astype(str)  # ensure all text is string
y = df['label']

# === Step 2: Split data (80/20) ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# === Step 3: Create a Pipeline (Vectorizer + Classifier) ===
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=300,    # small number for fast processing
        ngram_range=(1, 2),
        stop_words='english'
    )),
    ("clf", LogisticRegression(max_iter=100))  # increase iterations for convergence
])

# === Step 4: Train the model ===
pipeline.fit(X_train, y_train)

# === Step 5: Evaluate on test set ===
y_pred = pipeline.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# === Step 6: Save the trained pipeline ===
joblib.dump(pipeline, "model.pkl")
print("\nPipeline saved as 'model.pkl'. Ready to use in FastAPI!")