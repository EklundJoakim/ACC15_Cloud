import subprocess
p = subprocess.Popen('python3 test.py > result.txt', shell=True, stdout=subprocess.PIPE)
output = p.communicate()[0]

