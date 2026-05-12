from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the digits dataset (built-in, no download needed)
print("Loading Digits dataset...")
digits = load_digits()
X, y = digits.data, digits.target

# 2. Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize and Train the Model
print("Training the model...")
model = LogisticRegression(max_iter=10000) # Increased iterations for convergence
model.fit(X_train, y_train)

# 4. Make Predictions and check accuracy
print("Testing the model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"--- Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")