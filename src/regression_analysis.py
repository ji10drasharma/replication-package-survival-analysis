import pandas as pd
from  matplotlib import pyplot as plt
import seaborn as sns
import os
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def regression():

    # Ensure the output directory exists
    output_dir = Path("output")
    os.makedirs(output_dir, exist_ok=True)

    # Load the data
    data = pd.read_csv(Path("data/processed/clean_data.csv"))

    # Drop the 'repo_name' as it's likely a unique identifier that's not useful for prediction
    data = data.drop(["repo_name", "lifeSpan"], axis=1)

    # Check for any missing values and fill or drop them
    # data.fillna(method='ffill', inplace=True)  # Forward fill for simplicity

    # Checking data types and unique values in each categorical column
    for col in ["repoType", "language", "status"]:
        print(f"Unique values in {col}: {data[col].unique()}")

    # If the data is confirmed to be categorical, proceed to encode and store mappings
    label_mappings = {}

    for col in ["repoType", "language", "status"]:
        le = LabelEncoder()
        original_data = data[col]  # Storing original data to view before transformation
        data[col] = le.fit_transform(data[col])
        label_mappings[col] = dict(
            zip(original_data, data[col])
        )  # Mapping from original labels to integers

    # Print out the mappings correctly
    for col, mapping in label_mappings.items():
        print(f"Mapping for {col}: {mapping}")

    print(f"Total dataset count: {data.shape[0]}")

    # Define the feature set and the target
    X = data.drop(
        ["status"], axis=1
    )  # Excluding 'lifeSpan' if it's not considered a feature
    y = data["status"]  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # Normalize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Initialize the Logistic Regression model
    logreg = LogisticRegression()

    # Fit the model to the training data
    logreg.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = logreg.predict(X_test)

    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

    # Print the confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Print the classification report with zero_division parameter set to 0
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # Generate the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Assuming label_mappings['status'] contains the mapping from labels to integers
    # We need to get the class labels in the correct order:
    class_labels = list(label_mappings["status"].keys())

    # Plotting using seaborn
    plt.figure(figsize=(10, 7))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=class_labels,
        yticklabels=class_labels,
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")

    plt.savefig(f"{output_dir}/confusion_matrix.eps", format="eps")
    plt.savefig(f"{output_dir}/confusion_matrix.pdf")
    # plt.show()

    print(f"Regression based analysis complete")