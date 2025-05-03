import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, RobustScaler, QuantileTransformer

# === 1. Load dataset ===
url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv"
dataset = pd.read_csv(url)

model_df = dataset.copy()
model_df = model_df.drop(['EmployeeId'], axis=1)

# === 2. Label Encoding ===
le_dict = {}

for col in model_df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    model_df[col] = le.fit_transform(model_df[col].astype(str))
    le_dict[col] = le

# === 3. Pisahkan data ===
labeled_df = model_df[model_df['Attrition'].notna()]
unlabeled_df = model_df[model_df['Attrition'].isna()]

X = labeled_df.drop('Attrition', axis=1)
y = labeled_df['Attrition']

# === 4. Scaling dan Normalisasi ===
scaler = RobustScaler()
X_array = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_array, columns=X.columns)

quantile_transformer = QuantileTransformer(output_distribution='normal')
quantile_transformer.fit(X_scaled)
X_scaled_df = pd.DataFrame(quantile_transformer.transform(X_scaled), columns=X.columns)

# === 5. Preprocess unlabeled ===
for col in unlabeled_df.select_dtypes(include='object').columns:
    le = le_dict[col]
    unlabeled_df[col] = le.transform(unlabeled_df[col].astype(str))

X_unlabeled = unlabeled_df.drop('Attrition', axis=1)
X_unlabeled_scaled_df = pd.DataFrame(scaler.transform(X_unlabeled), columns=X_unlabeled.columns)
X_unlabeled_scaled_df = pd.DataFrame(quantile_transformer.transform(X_unlabeled_scaled_df), columns=X_unlabeled.columns)

# === 6. Load Model & Prediksi ===
model = joblib.load("best_randomForrest_model.pkl")

predicted_attrition_labeled = model.predict(X_scaled_df)
predicted_attrition_unlabeled = model.predict(X_unlabeled_scaled_df)

# === 7. Fungsi bantu konversi numerik ===
def convert_numeric_to_int(df, original_df):
    for col in df.columns:
        if np.issubdtype(original_df[col].dtype, np.integer):
            df[col] = df[col].round().astype(int)
    return df

# === UNLABELED ===
X_inverse_quantile_unlabeled = quantile_transformer.inverse_transform(X_unlabeled_scaled_df)
X_inverse_unlabeled = scaler.inverse_transform(X_inverse_quantile_unlabeled)
X_inverse_unlabeled_df = pd.DataFrame(X_inverse_unlabeled, columns=X_unlabeled.columns)

X_inverse_unlabeled_df = convert_numeric_to_int(X_inverse_unlabeled_df, dataset.loc[unlabeled_df.index])

for col in le_dict:
    if col in X_inverse_unlabeled_df.columns:
        le = le_dict[col]
        max_class = len(le.classes_) - 1
        X_inverse_unlabeled_df[col] = X_inverse_unlabeled_df[col].clip(0, max_class)
        X_inverse_unlabeled_df[col] = le.inverse_transform(X_inverse_unlabeled_df[col].astype(int))

X_inverse_unlabeled_df['Attrition'] = dataset.loc[unlabeled_df.index, 'Attrition'].values
X_inverse_unlabeled_df['Predicted_Attrition'] = predicted_attrition_unlabeled
X_inverse_unlabeled_df.index = dataset.loc[unlabeled_df.index].index

# === LABELED ===
X_inverse_quantile_labeled = quantile_transformer.inverse_transform(X_scaled_df)
X_inverse_labeled = scaler.inverse_transform(X_inverse_quantile_labeled)
X_inverse_labeled_df = pd.DataFrame(X_inverse_labeled, columns=X.columns)

X_inverse_labeled_df = convert_numeric_to_int(X_inverse_labeled_df, dataset.loc[labeled_df.index])

for col in le_dict:
    if col in X_inverse_labeled_df.columns:
        le = le_dict[col]
        max_class = len(le.classes_) - 1
        X_inverse_labeled_df[col] = X_inverse_labeled_df[col].clip(0, max_class)
        X_inverse_labeled_df[col] = le.inverse_transform(X_inverse_labeled_df[col].astype(int))

X_inverse_labeled_df['Attrition'] = dataset.loc[labeled_df.index, 'Attrition'].values
X_inverse_labeled_df['Predicted_Attrition'] = predicted_attrition_labeled
X_inverse_labeled_df.index = dataset.loc[labeled_df.index].index

# === Gabungkan & urutkan kembali ===
combined_df = pd.concat([X_inverse_labeled_df, X_inverse_unlabeled_df]).sort_index()
combined_df['EmployeeId'] = dataset['EmployeeId'].values
cols = combined_df.columns.tolist()
cols.insert(cols.index('Age'), cols.pop(cols.index('EmployeeId')))
combined_df = combined_df[cols]

# === Simpan atau tampilkan ===
print(combined_df.head())  # Tampilkan preview
combined_df.to_csv("combined_attrition_predictions.csv", index=False)

# === Selesai ===