# ============================================
# Projeto de Machine Learning com Dados de Futebol
# ============================================

# 1. Importação e análise inicial
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_curve, roc_auc_score, precision_recall_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
import shap
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE

# Carregar dataset (exemplo fictício de futebol)
df = pd.read_csv("matches.csv")  # substitua pelo dataset real

print(df.head())
print(df["target"].value_counts())  # verificar desbalanceamento

# 2. Feature Engineering
df["goal_diff"] = df["home_goals"] - df["away_goals"]
df["is_home_win"] = (df["goal_diff"] > 0).astype(int)

# Definir X e y
X = df[["home_goals", "away_goals", "goal_diff"]]
y = df["is_home_win"]

# 3. Preparação dos dados
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Regressão Logística
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
print("=== Logistic Regression Report ===")
print(classification_report(y_test, y_pred))

# 5. Curvas de avaliação
y_probs = log_reg.predict_proba(x_test)[:,1]

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

# 6. Balanceamento
# Undersampling
fraudes = df[df["is_home_win"] == 1]
normais = df[df["is_home_win"] == 0].sample(len(fraudes), random_state=42)
df_under = pd.concat([fraudes, normais])

# Oversampling com SMOTE
smote = SMOTE()
x_res, y_res = smote.fit_resample(X, y)

# 7. Random Forest
rf = RandomForestClassifier(n_estimators=50, max_depth=10, class_weight="balanced", random_state=42)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)
print("=== Random Forest Report ===")
print(classification_report(y_test, y_pred_rf))

# 8. Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])
pipeline.fit(x_train, y_train)
y_pred_pipe = pipeline.predict(x_test)
print("=== Pipeline Logistic Regression Report ===")
print(classification_report(y_test, y_pred_pipe))

# 9. Threshold customizado
threshold = 0.3
y_pred_custom = (y_probs > threshold).astype(int)
print("=== Threshold 0.3 Report ===")
print(classification_report(y_test, y_pred_custom))

# 10. XGBoost
xgb = XGBClassifier(scale_pos_weight=10, eval_metric="logloss", random_state=42)
xgb.fit(x_train, y_train)
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

# 11. Ajuste de hiperparâmetros
param_grid = {
    "max_depth": [3, 5],
    "n_estimators": [50, 100]
}
grid = GridSearchCV(XGBClassifier(eval_metric="logloss"), param_grid, scoring="recall", cv=3)
grid.fit(x_train, y_train)
print("Melhores parâmetros:", grid.best_params_)

# 12. Explicabilidade com SHAP
explainer = shap.Explainer(xgb)
shap_values = explainer(x_test[:100])
shap.plots.bar(shap_values)
