from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Task Manager API is running"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify({"message": "Task added", "task": data})

@app.route('/tasks/<int:index>', methods=['PUT'])
def update_task(index):
    if index < len(tasks):
        data = request.get_json()
        tasks[index] = data
        return jsonify({"message": "Task updated"})
    return jsonify({"error": "Task not found"})

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
