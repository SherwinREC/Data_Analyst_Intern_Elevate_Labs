import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

path = kagglehub.dataset_download("patelris/electric-vehicle-market-and-pricing-dataset-2026")
df = pd.read_csv(os.path.join(path, os.listdir(path)[0]))

print("Column Names:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

df = df.drop_duplicates()
df = df.dropna(subset=['Price'])

for col in df.select_dtypes(include='number').columns:
    if col != 'Price':
        df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

sns.histplot(df['Price'], kde=True, color='steelblue')
plt.title("EV Price Distribution")
plt.xlabel("Price (USD)")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

num_cols = df.select_dtypes(include='number').columns.tolist()
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

if 'Brand' in df.columns:
    df.groupby('Brand')['Price'].mean().sort_values(ascending=False).head(15).plot(
        kind='bar', color='mediumpurple', figsize=(12, 5))
    plt.title("Average Price by Brand")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("price_by_brand.png")
    plt.show()

if 'Range_km' in df.columns:
    sns.scatterplot(x='Range_km', y='Price', data=df, alpha=0.6)
    plt.title("Range vs Price")
    plt.xlabel("Range (km)")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.savefig("range_vs_price.png")
    plt.show()

if 'Battery_Capacity_kWh' in df.columns:
    sns.scatterplot(x='Battery_Capacity_kWh', y='Price', data=df, alpha=0.6, color='coral')
    plt.title("Battery Capacity vs Price")
    plt.xlabel("Battery Capacity (kWh)")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.savefig("battery_vs_price.png")
    plt.show()

df_model = df.copy()
le = LabelEncoder()
for col in df_model.select_dtypes(include='object').columns:
    df_model[col] = le.fit_transform(df_model[col].astype(str))

X = df_model.drop(columns=['Price'])
y = df_model['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
}

results = {}
trained_models = {}

for name, model in models.items():
    if name == 'Linear Regression':
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    results[name] = {
        'MAE': round(mean_absolute_error(y_test, y_pred), 2),
        'RMSE': round(np.sqrt(mean_squared_error(y_test, y_pred)), 2),
        'R2 Score': round(r2_score(y_test, y_pred), 4)
    }
    trained_models[name] = (model, y_pred)

results_df = pd.DataFrame(results).T
print(results_df)

best_name = results_df['R2 Score'].idxmax()
best_model, best_preds = trained_models[best_name]
print(f"Best Model: {best_name} with R2 Score: {results_df.loc[best_name, 'R2 Score']}")

plt.figure(figsize=(8, 5))
plt.scatter(y_test, best_preds, alpha=0.5, color='steelblue', edgecolors='k', linewidths=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=1.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(f"Actual vs Predicted — {best_name}")
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.show()

if hasattr(best_model, 'feature_importances_'):
    feat_imp = pd.Series(best_model.feature_importances_, index=X.columns)
    feat_imp.sort_values(ascending=False).head(10).plot(kind='bar', color='darkorange', figsize=(10, 5))
    plt.title("Top 10 Feature Importances")
    plt.ylabel("Importance Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("feature_importance.png")
    plt.show()

df.to_csv("ev_cleaned.csv", index=False)
results_df.to_csv("ev_model_results.csv")
print("Saved ev_cleaned.csv and ev_model_results.csv")
