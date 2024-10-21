import sys
from tabulate import tabulate
from livePricesHandler import addPriceFunctionality



def readmode():
  with open('output.txt', 'r') as file:
    lines = []
    for line in file:
      lines.append(line)

    if len(lines) == 0:
      print(' NOTHING TO READ (Use the <write> arg to write to the file.) '.center(60, '_'), '\n')
      sys.exit()


    cleanedData = []

    for line in lines:
      splt = line.strip().split(',')
      asset, bidpoi, askpoi = splt
      
      cleanedLst = [asset, bidpoi, askpoi]
      cleanedData.append(cleanedLst)


    newData = addPriceFunctionality(cleanedData)

    headers = ['Asset', 'BidPoi', 'AskPoi', 'Live Price', 'Below BidPoi', 'Above AskPoi', 'Within 3% BidPoi', 'Within 3% AskPoi']

    print(tabulate(newData, headers=headers, tablefmt='grid'))

