import sys
from tabulate import tabulate


def getCurrentPrices(assetLst: list) -> list:
  pass


def readmode():
  with open('output.txt', 'r') as file:
    lines = []
    for line in file:
      lines.append(line)

    if len(lines) == 0:
      print(' NOTHING TO READ (Use the <write> arg to write to the file.) '.center(60, '_'), '\n')
      sys.exit()

    print(lines)
    cleanedData = []

    for line in lines:
      splt = line.strip().split(',')
      asset, bidpoi, askpoi = splt
      
      cleanedLst = [asset, bidpoi, askpoi]
      cleanedData.append(cleanedLst)

    headers = ['Asset', 'BidPoi', 'AskPoi']

    print(tabulate(cleanedData, headers=headers, tablefmt='grid'))

