print(classification_report(y_test, y_pred_xgb))

# Retorno console
#
#              precision    recall  f1-score   support
#
#           0       1.00      1.00      1.00     85307
#           1       0.94      0.85      0.89       136
#
#    accuracy                           1.00     85443
#   macro avg       0.97      0.93      0.95     85443
# weighted avg      1.00      1.00      1.00     85443
