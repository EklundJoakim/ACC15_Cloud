import os
from flask import Flask
from tasks import runBench
from subprocess import call

call("celery -A tasks worker --loglevel=INFO --concurrency=10 -n worker1.%h &", shell=True)

app = Flask(__name__)

@app.route('/calculate/', methods = ['GET'])
def runbenchmark():
  results = runBench.delay()
  resultat = results.get()

if __name__ == '__main__'
  app.run(host='0.0.0.0', debug=True)
  
