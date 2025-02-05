from flask import Flask, request, jsonify
import json
from collections import defaultdict

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)




@app.route('/')
def hello_world():
        return 'Hello, World!', 200, {'Content-Type': 'text/html'} # return with proper MIME type and status code

@app.errorhandler(404)
def not_found(e):
        return 'Page not found', 404, {'Content-Type': 'text/html'}

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: #select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied





# Route to get statistics about meal preferences and program enrollments
@app.route('/stats')
def get_stats():
    stats_data = defaultdict(int)

    for student in data:
        stats_data[student['pref']] += 1  # Count meal preferences
        stats_data[student['programme']] += 1  # Count program enrollments

    return jsonify(stats_data)  # Return the statistics as JSON




# Arithmetic routes: add, subtract, multiply, and divide
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({"result": a + b})

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return jsonify({"result": a - b})

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return jsonify({"result": a * b})

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    return jsonify({"result": a / b})



# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)