import os

stream = os.popen('git --no-pager diff  --cached')
output = stream.read()
print(output)