for col in ['user_id', 'product_id_orders', 'order_id_orders', 'ts_orders', 'product_id_page_views', 'order_id_page_views', 'ts_page_views']:
    X_train[col] = X_train[col].astype('category')

# Create DMatrix with enable_categorical=True
dtrain = xgb.DMatrix(X_train, label=y_train, enable_categorical=True)

# Define the model parameters
params = {
    'objective': 'multi:softmax',
    'num_class': len(product_categories),
    'enable_categorical': True
}

# Train the model
xgb_model = xgb.train(params, dtrain)

# Predict on the training set
y_pred = xgb_model.predict(dtrain)

# Evaluate the model
accuracy = accuracy_score(y_train, y_pred)
print(f"Training Accuracy: {accuracy:.2f}")


xgb_model = xgb.XGBClassifier(objective='multi:softprob', num_class=len(np.unique(y_train)),
                              max_depth=6, learning_rate=0.1, n_estimators=100, n_jobs=-1)
xgb_model.fit(X_train, y_train)

# Make predictions
y_pred = xgb_model.predict(X_test)
y_pred_prob = xgb_model.predict_proba(X_test)