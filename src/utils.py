import os
import sys
import dill
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save a Python object to the given file path using dill.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Train and evaluate multiple models using R² score.
    Returns a report dictionary mapping model names to their test scores.
    """
    try:
        report = {}

        for name, model in models.items():
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[name] = test_score  # Or include train_score if needed

        return report

    except Exception as e:
        raise CustomException(e, sys)
