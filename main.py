import sys
from readmode import readmode
from updimode import updimode
from updamode import updamode
from writemode import writemode


def initialize(args: list) -> str:
  if len(args) == 1:
    return 'read'
  
  arg = args[1].lower()

  if arg == 'read':
    return 'read'
  elif arg == 'updatei':
    return 'updi'
  elif arg == 'updatea':
    return 'upda'
  elif arg == 'write':
    return 'write'
  else:
    sys.exit()



def main(mode: str):
  
  if mode == 'read':
    readmode()
  elif mode == 'updi':
    updimode()
  elif mode == 'upda':
    updamode()
  elif mode == 'write':
    writemode()



if __name__ == '__main__':
  mode = initialize(sys.argv)
  print('\n', ' PROGRAM HAS STARTED '.center(40, '_'), '\n')

  main(mode=mode)
