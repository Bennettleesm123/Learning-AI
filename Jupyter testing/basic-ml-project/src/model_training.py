def train_model(X_train, y_train):
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor

    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

    # Initialize the model (you can choose either Linear Regression or Decision Tree)
    model = LinearRegression()  # or DecisionTreeRegressor()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    return model, X_val, y_val