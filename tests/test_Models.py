from pkg.models import Model
import numpy

model = Model()

def test_Model_type():
    assert isinstance(model, Model)

model.build_model()

X, y = model.get_training_data()
preds = model.predict(X)

def test_predict_type():
    assert isinstance(preds, numpy.ndarray)

def test_predict_length():
    assert len(preds)==len(X)
    

    

