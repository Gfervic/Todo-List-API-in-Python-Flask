from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    print(todos)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True) # get the request body content in a real python data structure
    if request_body is None:
        return "The request body is null", 400
    if request_body["label"] is None:
        return "You have to send the label", 400
    if request_body["done"] is None:
        return "You have to send the done", 400
    
    # print("Incoming request with the following body", request_body)
    todos.append(request_body)
    print(todos)
    return jsonify(todos), 200
    # return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.remove(todos[position])
    print(todos)
    return jsonify(todos), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
