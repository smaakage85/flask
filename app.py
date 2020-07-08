from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

# instantiate and build model
from pkg.models import ModelIris
model = ModelIris()
model.build_model()

@app.route('/')
def home():
    return 'Welcome to this wonderful app!'

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    data_json = request.get_json()
    if (request.method == 'POST'):
        X = request.get_json()
        X = model.parse_input(X)
    else:
        from sklearn.datasets import load_iris
        X, y = load_iris(return_X_y=True)
         
    preds = model.predict(X)
    preds_json = model.parse_output(preds)
    return jsonify(preds_json)

if __name__ == '__main__':
    app.run()

# curl http://127.0.0.1:5000/
# curl http://127.0.0.1:5000/multi/10
# curl -H "Content-Type: application/json" -X POST -d "{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}" http://127.0.0.1:5000/json/
# curl -H "Content-Type: application/json" -X POST -d "[{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}]" http://127.0.0.1:5000/predict/
# curl -H "Content-Type: application/json" -X POST -d "[{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}, {\"x1\":6.2, \"x2\":3.4, \"x3\":5.4, \"x4\":2.3}]" http://127.0.0.1:5000/predict/
# curl -H "Content-Type: application/json" -X POST -d "[{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}]" https://larsk-flask.herokuapp.com/predict/
# curl -H "Content-Type: application/json" -X POST -d "[{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}, {\"x1\":6.2, \"x2\":3.4, \"x3\":5.4, \"x4\":2.3}]" https://larsk-flask.herokuapp.com/predict/
