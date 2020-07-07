def train_iris_model():
    """ trains iris model. """
    # load dataset
    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    
    # fit model
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(X, y)
    
    return model

