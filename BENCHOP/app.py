import os
from flask import Flask
from tasks import runBench
from flask import render_template, redirect, request, make_response, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return redirect('homepage')

@app.route('/homepage/')
def static_page():
    return render_template('homepage.html')

@app.route('/calculate/', methods = ['GET'])
def runbenchmark():
  results = runBench.delay()
  return results.get()

@app.route('/run-calculation/', methods = ['POST'])
def runCalculation():
  option_id = request.form['option_id']
  problem_id = request.form['problem_id']
  r = request.form['r']
  result = runBench.delay(int(problem_id), float(r))
  return jsonify(status="success", result=result)


@app.route('/administrator/login/', methods=['POST', 'GET'])
def login():
    error = ''
    if request.method == 'POST':
        if request.form['username'] == "acc15" and request.form['password'] == "password":
            return redirect('homepage')
        else:
            error = 'Invalid username or password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True) 
