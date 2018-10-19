import os

from celery import Celery
from oct2py import octave
from subprocess import call

AppCelery = Celery('tasks', backend='rpc://', broker='pyamqp://')

@AppCelery.task
def runBench():
    call(["python3", "a.py"])
    with open('result.txt','r') as f:
      lines = f.read().splitlines()
      last_line = lines[-1]
      return (str(last_line))
#paths
#Error
