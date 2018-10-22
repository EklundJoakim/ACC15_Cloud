import os
from flask import Flask
from tasks import runBench
from flask import render_template, redirect

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

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True) 
