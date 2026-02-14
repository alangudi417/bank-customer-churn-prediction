import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, roc_auc_score, classification_report

def train_evaluate_model(
        model_class,
        model_params,
        X_train,
        y_train,
        X_test,
        y_test,
        use_class_weight=False
):
    """
    train_evaluate_model to help with the classification model.
    
    The Parameters are: 
    - model_class: is the model from sklearn.
    - model_params: are the hyperparameters per each model.
    - use_class_weight: as the class-balance is imbalanced, this is to use when TRUE (add class_weight='balanced')

    Returns:
    - model trained
    - F1 score
    - ROC - AUC score
    """

    # here is to add the class_weight if needed
    if use_class_weight:
        model_params = {**model_params, "class_weight": "balanced"}

    model = model_class(**model_params)    # Call the model
    model.fit(X_train, y_train)            # Training the model
    predictions = model.predict(X_test)    # Predict
    
    # Metrics
    f1 = f1_score(y_test, predictions)
    auc = roc_auc_score(y_test, predictions)

    print(classification_report(y_test, predictions))
    print()
    print(f"F1 Score: {f1:.4f}")
    print(f"AUC-ROC: {auc:.4f}")

    return model, f1, auc