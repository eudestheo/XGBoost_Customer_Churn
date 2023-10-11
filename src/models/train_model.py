def train_model(X, y):
    """
    Train the machine learning model using cross-validation and grid search.

    Parameters:
    X (DataFrame): Features (input variables) for training.
    y (Series): Target variable for training.

    Returns:
    XGBoostClassifier: The best-trained XGBoost model found by grid search.
    """
    # Define the machine learning model
    model = xgb.XGBClassifier(objective='binary:logistic',
                                 eval_metric="logloss",
                                 seed=42,
                                 subsample=0.9,
                                 colsample_bytree=0.5,
                                 early_stopping_rounds=10)

    # Define hyperparameters for grid search
    param_grid = {'max_depth': [4],
              'learning_rate': [0.1, 0.5, 1],
              'gamma': [0.25],
              'reg_lambda': [10, 20, 100],
              'scale_pos_weight': [3]
        # Add other hyperparameters to tune
    }

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(estimator=model, 
                               param_grid=param_grid,
                                 scoring='roc_auc',
                                 verbose=1,
                                 n_jobs = 10,
                                 cv = 3)
    grid_search.fit(X,
                    y,
                    eval_set=[(X_test, y_test)],
                    verbose=True)

    # Print the best hyperparameters
    print("Best Hyperparameters:", grid_search.best_params_)
    

    return grid_search.best_estimator_