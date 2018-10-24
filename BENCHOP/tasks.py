import os

from celery import Celery
from oct2py import octave
from subprocess import call
from runfile import runfile

AppCelery = Celery('tasks', backend='rpc://', broker='amqp://ACC15:pwd@0.0.0.0:/myvhost')

@AppCelery.task
def runBench(prob, r):
    runfile(prob, r)
    f = open('result.txt','r')
    lines = f.read().splitlines()
    last_line1 = lines[-1]
    last_line2 = lines[-2]
    f.close()
    return ("COS: " + str(last_line1) + "\nUniform Grid: " + str(last_line2))

#paths
#Error
