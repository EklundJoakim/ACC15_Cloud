from oct2py import octave
import json
a = octave.Table()
dic = {'param1': str(a.flat[0]), 'param2': str(a.flat[1]), 'param3': str(a.flat[2])}

print (json.dumps(dic))

