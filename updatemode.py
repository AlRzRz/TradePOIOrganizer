

def inputHandler():
  print('IP was here')


def updmode():
  assetsData = []

  with open('output.txt', 'r') as file:
    for line in file:
      assetInfo = line.strip().split(',')
      assetsData.append(assetInfo)

  print(assetsData)