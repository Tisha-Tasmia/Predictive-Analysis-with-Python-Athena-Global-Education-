def train_model(X_train, y_train, model_name='linear_regression'):
    """Trains a machine learning model.

    Args:
        X_train (pandas.DataFrame): Training features.
        y_train (pandas.Series): Training target.
        model_name (str): Name of the model to train ('linear_regression', 'decision_tree', etc.).

    Returns:
        object: Trained model object.
    """
    if model_name == 'linear_regression':
        model = LinearRegression()
    elif model_name == 'decision_tree':
        model = DecisionTreeRegressor()
    else:
        raise ValueError("Invalid model name.")

    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluates the performance of the trained model.

    Args:
        model: Trained model object.
        X_test (pandas.DataFrame): Test features.
        y_test (pandas.Series): Test target.

    Returns:
        float: Mean Squared Error (MSE).
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse
