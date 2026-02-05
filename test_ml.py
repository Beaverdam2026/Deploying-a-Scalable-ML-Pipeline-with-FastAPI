import pytest
import numpy as np
import pandas as pd
import os
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model
from train_model import cat_features

def test_model_type():
    """
    # asserts that the model is a random forest classifier
    """
    
    X_train, y_train = make_classification(random_state=67)
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)


def test_data_shape():
    """
    # asserts that the census.csv file the model is trained on is the correct shape
    """
    correct_shape = (32561, 15)
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    assert data.shape == correct_shape

def test_cat_features():
    """
    # asserts that the cat_features variable from the train_model.py file has not been modified
    """
    cat_features_check = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
    ]
    assert cat_features_check == cat_features
