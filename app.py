from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

from pkg.models import train_iris_model

# train model
model = train_iris_model()

@app.route('/')
def home():
    return 'heeeellloow world!'

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num * 10})

@app.route('/json/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()

        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({'about':'Hello World!'})

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    data_json = request.get_json()
    if (request.method == 'POST'):
        samples = request.get_json()
        samples = [np.array(list(obs.values()), ndmin = 2) for obs in samples]
        samples = np.concatenate(samples, axis = 0)
    else:
        from sklearn.datasets import load_iris
        X, y = load_iris(return_X_y=True)
        samples = X[(0,50,70),:]
         
    preds = model.predict(samples)
    preds = preds.tolist()
    return jsonify({'predictions': preds})

if __name__ == '__main__':
    app.run()



# from flask import Flask, jsonify, request

# app = Flask(__name__)

# app.run(debug=True)

# curl http://127.0.0.1:5000/
# curl http://127.0.0.1:5000/multi/10
# curl -H "Content-Type: application/json" -X POST -d "{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}" http://127.0.0.1:5000/json/
# curl -H "Content-Type: application/json" -X POST -d "[{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}]" http://127.0.0.1:5000/predict/
# curl -H "Content-Type: application/json" -X POST -d "[{\"x1\":5.1, \"x2\":3.5, \"x3\":1.4, \"x4\":0.2}, {\"x1\":6.2, \"x2\":3.4, \"x3\":5.4, \"x4\":2.3}]" http://127.0.0.1:5000/predict/


# data_json = """[{ 
#     \"x1\" : 5.1,
#     \"x2\" : 3.5,
#     \"x3\" : 1.4,
#     \"x4\" : 0.2
# },
# { 
#     \"x1\" : 6.2,
#     \"x2\" : 3.4,
#     \"x3\" : 5.4,
#     \"x4\" : 2.3
# }]"""

# data_json = json.loads(data_json)
# arr = [np.array(list(obs.values()), ndmin = 2) for obs in data_json]
# arr = np.concatenate(arr, axis = 0)

