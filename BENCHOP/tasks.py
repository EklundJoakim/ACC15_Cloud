import os

from celery import Celery
from oct2py import octave

AppCelery = Celery('tasks', backend='rpc://', broker='pyampq://')

@AppCelery.task
def runBench():
  timeToExecute, paths, Error = octave.Table()
  return (timeToExecute, paths, Error)
