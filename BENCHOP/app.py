import os, json
from flask import Flask
from init import init_instance
from tasks import runBench
from time import sleep
from flask import render_template, redirect, request, make_response, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return redirect('homepage')

@app.route('/homepage/')
def static_page():
    return render_template('homepage.html')

@app.route('/run-calculation/', methods = ['POST'])
def runCalculation():
  option_id = request.form['option_id']
  problem_id = request.form['problem_id']
  r = request.form['r']
  if option_id == '0':
    r = '0.03'
  result = ""
  if problem_id != '0':
    running = runBench.delay(int(problem_id), float(r))
    while not running.ready():
      sleep(0.5)
    f = open("result-" + str(problem_id) +".txt",'r')
    lines = f.read().splitlines()
    last_line1 = lines[-1]
    last_line2 = lines[-2]
    f.close()
    result = result + "Problem " + str(problem_id) + "; r = " + str(r) + "; COS: " + str(last_line1) + "; Uniform Grid: " + str(last_line2)
    return jsonify(status="success", result=result)
  else:
    running1 = runBench.delay(1, float(r))
    running2 = runBench.delay(2, float(r))
    running3 = runBench.delay(3, float(r))
    while not (running1.ready() and running2.ready() and running3.ready()):
      sleep(0.5)
    for i in range(1,4):
      f = open("result-" + str(i) + ".txt",'r')
      lines = f.read().splitlines()
      last_line1 = lines[-1]
      last_line2 = lines[-2]
      f.close()
      result = result + "Problem " + str(i) + "; r = " + str(r) + ";COS: " + str(last_line1) + "; Uniform Grid: " + str(last_line2) + "<hr>"
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

@app.route('/administrator/run-new-instance/', methods=['GET'])
def run_new_instance():
    result = init_instance()
    return result


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True) 

