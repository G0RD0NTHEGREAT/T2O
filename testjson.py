import os.path
import time
import base64
import subprocess
import json

with open("media/"+'aW5wdXQu.json', 'r') as f:
	distros_dict = json.load(f)

operations = distros_dict[0]['operations']

print(operations[2][1])
arg =   "{:.7f}".format(operations[2][1][0]) 

print(arg)
