from flask import Flask, jsonify, request
    
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
def index():
    data_json = request.get_json()
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        from sklearn.datasets import load_iris
        X, y = load_iris(return_X_y=True)
        new_samples = X[(0,50,70),:]
        preds = model.predict(new_samples) 
        return jsonify({'predictions': preds})

if __name__ == '__main__':
    app.run()



# from flask import Flask, jsonify, request

# app = Flask(__name__)

# app.run(debug=True)

# curl http://127.0.0.1:5000/
# curl http://127.0.0.1:5000/multi/10
# curl -H "Content-Type: application/json" -X POST -d "{\"name\":\"xyz\", \"address\":\"address xyz\"}" https://larsk-flask.herokuapp.com/json/
