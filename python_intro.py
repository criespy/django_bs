def callname():
  import subprocess
  proc = subprocess.Popen('whoami', stdout=subprocess.PIPE, universal_newlines=True)
  nama =  str(proc.stdout.read())
  print('Helo ' + nama)

callname()