def load_data(filepath):
    import pandas as pd
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    # Example preprocessing: drop missing values and encode categorical variables
    data = data.dropna()
    data = pd.get_dummies(data)
    return data