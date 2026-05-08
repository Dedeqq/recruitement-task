import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    roc_auc_score,
)


def evaluate_classification(*, y_test: np.ndarray, y_pred: np.ndarray) -> None:
    print("=== Classification Metrics ===\n")

    metrics: dict[str, float] = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "ROC AUC": roc_auc_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
    }

    for name, value in metrics.items():
        print(f"{name:10}: {value:.4f}")

    print("\n=== Confusion Matrix ===")
    print(confusion_matrix(y_test, y_pred))

    print("\n=== Classification Report ===")
    print(classification_report(y_test, y_pred))
