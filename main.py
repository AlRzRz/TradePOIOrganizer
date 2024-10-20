import sys
from readmode import readmode
from updatemode import updmode
from writemode import writemode


def initialize(args: list) -> str:
  if len(args) == 1:
    return 'read'
  
  arg = args[1].lower()

  if arg == 'read':
    return 'read'
  elif arg == 'update':
    return 'update'
  elif arg == 'write':
    return 'write'
  else:
    sys.exit()



def main(mode: str):
  
  if mode == 'read':
    readmode()
  elif mode == 'update':
    updmode()
  elif mode == 'write':
    writemode()



if __name__ == '__main__':
  mode = initialize(sys.argv)
  print('\n', ' PROGRAM HAS STARTED '.center(40, '_'), '\n')

  main(mode=mode)
