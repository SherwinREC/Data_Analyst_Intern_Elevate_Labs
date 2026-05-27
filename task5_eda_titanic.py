import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import os

path = kagglehub.dataset_download("shuofxz/titanic-machine-learning-from-disaster")
train = pd.read_csv(os.path.join(path, "train.csv"))
test = pd.read_csv(os.path.join(path, "test.csv"))

print(f"Train Shape: {train.shape}")
print(f"Test Shape: {test.shape}")
print(train.info())
print(train.describe())
print(train.isnull().sum())
print(train['Survived'].value_counts())

sns.histplot(train['Age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.tight_layout()
plt.show()

sns.countplot(x='Survived', data=train)
plt.title("Survival Count")
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.tight_layout()
plt.show()

sns.countplot(x='Pclass', data=train)
plt.title("Passenger Class Distribution")
plt.xlabel("Pclass")
plt.tight_layout()
plt.show()

sns.boxplot(x="Pclass", y="Age", data=train)
plt.title("Age Distribution by Passenger Class")
plt.tight_layout()
plt.show()

sns.countplot(x="Sex", hue="Survived", data=train)
plt.title("Survival by Gender")
plt.tight_layout()
plt.show()

sns.countplot(x="Pclass", hue="Survived", data=train)
plt.title("Survival by Passenger Class")
plt.tight_layout()
plt.show()

sns.scatterplot(x="Age", y="Fare", hue="Survived", data=train)
plt.title("Age vs Fare by Survival")
plt.tight_layout()
plt.show()

sns.heatmap(train.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

sns.pairplot(train[["Survived", "Age", "Fare", "Pclass"]], hue="Survived")
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

train['Age'] = train['Age'].fillna(train['Age'].median())
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])

print("Key Insights:")
print("1. Females had much higher survival rates than males.")
print("2. First-class passengers survived more compared to third-class.")
print("3. Younger passengers and children had higher survival chances.")
print("4. Fare and survival were positively correlated.")
print("5. Missing values existed mainly in Age, Cabin, and Embarked.")
