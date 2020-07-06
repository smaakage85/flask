from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'heeeellloow world!'


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num * 10})
    
if __name__ == '__main__':
    app.run()



# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if (request.method == 'POST'):
#         some_json = request.get_json()
#         return jsonify({'you sent': some_json}), 201
#     else:
#         return jsonify({'about':'Hello World!'})


# app.run(debug=True)

# curl http://127.0.0.1:5000/
# curl http://127.0.0.1:5000/multi/10
# curl -H "Content-Type: application/json" -X POST -d "{\"name\":\"xyz\", \"address\":\"address xyz\"}" http://127.0.0.1:5000/

