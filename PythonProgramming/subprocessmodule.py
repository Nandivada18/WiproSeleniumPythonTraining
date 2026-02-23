#subprocess module
#execute external system commands
#iteract with OS processes
#capture outputs, error and return codes
#control the process execution
#run the OS level commands - linux, macos, windows

import subprocess
#subprocess.run() - run command and wait
#subprocess.papen() - run the process aynchronulsy
#subprocess.PIPE - capture the output
#subprocess.CompleteProcess - result
#subprocess.TimeoutExpired - Time out execution
#subprocess.CalledProcesserError - command failure

result = subprocess.run("dir", shell =True, capture_output = True,text = True)
print(result)

result = subprocess.run("ipconfig", shell =True, capture_output = True,text = True)
print(result)

result = subprocess.run("python --version", shell =True, capture_output = True,text = True)
print(result.stdout)
#print(result.stderr)
