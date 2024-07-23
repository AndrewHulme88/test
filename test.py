import pandas as pd  # Importing pandas for data manipulation
from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data
from sklearn.preprocessing import StandardScaler, LabelEncoder  # Importing StandardScaler for feature scaling and LabelEncoder for encoding categorical features
from sklearn.svm import SVC  # Importing SVM classifier
from sklearn.metrics import confusion_matrix, roc_curve, precision_recall_curve, classification_report  # Importing various metrics for model evaluation
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import seaborn as sns  # Importing seaborn for enhanced visualizations
import numpy as np  # Importing numpy for numerical operations

# Load the cleaned data from CSV
df = pd.read_csv('cwdata_cleaned.csv')

# Separate features and target variable
X = df.drop(columns=['Stolen'])
y = df['Stolen']

# Encode categorical features
label_encoder = LabelEncoder()
X_encoded = X.copy()
for column in X.columns:
    if X[column].dtype == 'object':
        X_encoded[column] = label_encoder.fit_transform(X[column])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Scale numeric features
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()
X_train_scaled[numeric_features] = scaler.fit_transform(X_train[numeric_features])
X_test_scaled[numeric_features] = scaler.transform(X_test[numeric_features])

# Initialize SVM with a linear kernel
svm_model = SVC(kernel='linear', random_state=42, probability=True)

# Fit the model to the training data
svm_model.fit(X_train_scaled, y_train)

# Predict the outcomes on test data
y_pred = svm_model.predict(X_test_scaled)

# Evaluate the model
# Generate a classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# ROC Curve
y_prob = svm_model.decision_function(X_test_scaled)
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, linestyle='--', label='SVM')
plt.plot([0, 1], [0, 1], color='orange', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Precision-Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_prob)
plt.figure(figsize=(8, 6))
plt.plot(recall, precision, marker='.', label='SVM')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()
