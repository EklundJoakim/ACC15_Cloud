import subprocess
def runfile(prob, r):
  str_to_write = "from oct2py import octave\nimport json\na,b = octave.Table("+ str(prob) + "," + str(r) + ")\nprint (a)\nprint (b)"
  text_file = open("write_and_run.py","w")
  text_file.write(str_to_write)
  text_file.close()
  p = subprocess.Popen('python3 write_and_run.py > result.txt', shell=True, stdout=subprocess.PIPE)
  output = p.communicate()[0]

