import sys


def assetInputHandler():
  resp = input('What asset would you like to add? ("q" to quit) ')
  resp = resp.upper()

  if not resp.isalpha():
    return assetInputHandler()

  if resp == 'Q':
    print('\n', ' EXITING PROGRAM '.center(40, '_'), '\n')
    sys.exit()

  return resp


def bidAskInputHandler(BidorAsk: str):

  resp = input(f'Please input your POI for the {BidorAsk} ("x" to leave blank, "q" to quit the program) ')

  if resp.lower() in ['q', 'x']:
    return resp
  
  try:
    resp = float(resp)
  except ValueError:
    return bidAskInputHandler(BidorAsk=BidorAsk)
    
  return resp
    

def continuationInputHandler():
  continueAdding = input('Would you like to keep adding assets? (yes/no) ').lower()

  if continueAdding == '' or continueAdding not in ['yes', 'no']:
    return continuationInputHandler()
  
  return continueAdding

def inputHandler() -> list | None:
  assets = []

  while True:
    assetResp = assetInputHandler()
    bidResp = bidAskInputHandler('BID')
    if bidResp != 'q':
      askResp = bidAskInputHandler('ASK')

    if bidResp == 'q' or askResp == 'q':
      return None
    else:
      if bidResp != 'x':
        bidResp = float(bidResp)
      if askResp != 'x':
        askResp = float(askResp)
    
    assets.append([assetResp, bidResp, askResp])

    continueAdding = continuationInputHandler()
    if continueAdding != 'yes':
      break


  return assets


def writemode():
  print(' WARNING: QUITTING THE PROGRAM WILL NOT SAVE CHANGES! '.center(55, '*'), '\n')
  assetData = inputHandler()

  if assetData is None:
    print(' EXITING PROGRAM '.center(40, '_'), '\n')
    sys.exit()

  with open("output.txt", 'w') as file:
    for asset, bidPoi, askPoi in assetData:
      file.write(f'{asset},{bidPoi},{askPoi}\n')