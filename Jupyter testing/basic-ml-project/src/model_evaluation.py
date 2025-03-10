def evaluate_model(y_true, y_pred):
    from sklearn.metrics import accuracy_score, precision_score, recall_score

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')

    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall
    }

    return metrics