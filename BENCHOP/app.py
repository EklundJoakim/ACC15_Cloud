import os
from flask import Flask
from tasks import runBench

app = Flask(__name__)

@app.route('/calculate/', methods = ['GET'])
def runbenchmark():
  results = runBench.delay()
  return results.get()

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True) 
