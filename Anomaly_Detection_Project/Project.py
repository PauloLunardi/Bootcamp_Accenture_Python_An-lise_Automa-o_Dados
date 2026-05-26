"""
Projeto de Machine Learning com dados de futebol.
Objetivo: prever vitória do time da casa usando variáveis pré-jogo.
Modelos: Logistic Regression, Random Forest, XGBoost.
Avaliação: métricas de classificação, curvas ROC/PR, SHAP.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_curve, roc_auc_score, precision_recall_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE


# Importação do dataset
url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
df = pd.read_csv(url)

print(df.head())

# Variável alvo (resultado do jogo)
df["is_home_win"] = (df["home_score"] > df["away_score"]).astype(int)

# Features pré-jogo
X = df[["neutral", "tournament", "home_team", "away_team"]]

# Converter booleano para inteiro
X["neutral"] = X["neutral"].astype(int)

# Transformar variáveis categóricas em dummies
X = pd.get_dummies(X, drop_first=True)

y = df["is_home_win"]

# Divisão treino/teste (70% treino, 30% teste)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Pipeline com Regressão Logística
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),  # trata NaN
    ("scaler", StandardScaler(with_mean=False)),           # padroniza
    ("model", LogisticRegression(max_iter=1000))
])

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)

print("=== Pipeline Logistic Regression Report ===")
print(classification_report(y_test, y_pred))

# Curvas de avaliação
y_probs = pipeline.predict_proba(x_test)[:,1]

fpr, tpr, _ = roc_curve(y_test, y_probs)
plt.plot(fpr, tpr)
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()
print("AUC:", roc_auc_score(y_test, y_probs))

precision, recall, _ = precision_recall_curve(y_test, y_probs)
plt.plot(recall, precision)
plt.title("Precision-Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()

# Balanceamento com SMOTE
smote = SMOTE(random_state=42)
x_train_res, y_train_res = smote.fit_resample(x_train, y_train)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
rf.fit(x_train_res, y_train_res)
y_pred_rf = rf.predict(x_test)
print("=== Random Forest Report ===")
print(classification_report(y_test, y_pred_rf))

# XGBoost
xgb = XGBClassifier(scale_pos_weight=10, eval_metric="logloss", random_state=42)
xgb.fit(x_train_res, y_train_res)
y_pred_xgb = xgb.predict(x_test)
print("=== XGBoost Report ===")
print(classification_report(y_test, y_pred_xgb))

# Importância das variáveis
importancias = xgb.feature_importances_
plt.bar(range(len(importancias)), importancias)
plt.title("Importância das Variáveis")
plt.xlabel("Índice da Variável")
plt.ylabel("Importância")
plt.show()

# Explicabilidade com SHAP
explainer = shap.Explainer(xgb)
shap_values = explainer(x_test[:100])
shap.plots.bar(shap_values)

