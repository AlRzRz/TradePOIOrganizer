import sys

def assetInputHandler():
  resp = input('Which asset would you like to update/add? ("q" to quit) ')
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
  continueAdding = input('Would you like to keep updating/adding to your assets? (yes/no) ').lower()

  if continueAdding == '' or continueAdding not in ['yes', 'no']:
    return continuationInputHandler()
  
  return continueAdding



def inputHandler() -> list:
  assets = []

  while True:
    assetResp = assetInputHandler()
    bidResp = bidAskInputHandler('BID')
    if bidResp != 'q':
      askResp = bidAskInputHandler('ASK')

    if bidResp == 'q' or askResp == 'q':
      return None
    
    assets.append([assetResp, bidResp, askResp])

    continueAdding = continuationInputHandler()
    if continueAdding != 'yes':
      break


  return assets


def updmode():
  assetCargoData = inputHandler()
  if assetCargoData is None:
    print(' PROGRAM HAS QUIT VIA USER INPUT '.center(50, '_'))
    sys.exit()

  updatedAssetData = {}

  try:
    with open('output.txt', 'r') as file:
      for line in file:
        assetInfo = line.strip().split(',')
        updatedAssetData[assetInfo[0]] = assetInfo[1:]
  except FileNotFoundError:
    print(" No existing data found. Creating new file. ".center(55, '*'))

  for asset, bidPoi, askPoi in assetCargoData:
    updatedAssetData[asset] = [str(bidPoi), str(askPoi)]

  with open('output.txt', 'w') as file:
    for asset, poi in updatedAssetData.items():
      file.write(f'{asset},{poi[0]},{poi[1]}\n')
      print(f"Updated/Added asset: {asset}, BID POI: {poi[0]}, ASK POI: {poi[1]}")