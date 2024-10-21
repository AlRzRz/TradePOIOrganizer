import requests
from symbolMapping import symbol_to_id


def getCryptoPrice(tickerSymbol: str):
  tickerSymbol = tickerSymbol.upper()
  mappedTicker = symbol_to_id[tickerSymbol]

  url = f"https://api.coingecko.com/api/v3/simple/price?ids={mappedTicker}&vs_currencies=usd"
  resp = requests.get(url=url)

  if resp.status_code == 200:
    data = resp.json()
    return data.get(mappedTicker, {}).get('usd', None)
  else:
    print(f"Error fetching price for {tickerSymbol}.")
    return None


def comparisonHandler(liveAssetPrice, bidPoi, askPoi):
  priceBelowBid = liveAssetPrice < float(bidPoi)
  priceAboveAsk = liveAssetPrice > float(askPoi)

  within3Bid = abs((liveAssetPrice - float(bidPoi)) / float(bidPoi)) <= 0.03
  within3Ask = abs((liveAssetPrice - float(askPoi)) / float(askPoi)) <= 0.03

  return {
    "price_below_bidpoi": priceBelowBid,
    "price_above_askpoi": priceAboveAsk,
    "currentLiveAssetPrice": liveAssetPrice,
    "within_3_percent_bidpoi": within3Bid,
    "within_3_percent_askpoi": within3Ask
  }


def addPriceFunctionality(assetCargo: list) -> list:
  updatedAssetCargo = []

  for assetData in assetCargo:
    asset, bidPoi, askPoi = assetData

    liveAssetPrice = getCryptoPrice(asset.upper())

    if liveAssetPrice is not None:
      comparisonResult = comparisonHandler(liveAssetPrice=liveAssetPrice, bidPoi=bidPoi, askPoi=askPoi)

      updatedAssetData = assetData + [
        liveAssetPrice,
        comparisonResult['price_below_bidpoi'],
        comparisonResult['price_above_askpoi'],
        comparisonResult['within_3_percent_bidpoi'],
        comparisonResult['within_3_percent_askpoi']
      ]
      updatedAssetCargo.append(updatedAssetData)

    else:
      updatedAssetData = assetData + [None, None, None, None, None]
      updatedAssetCargo.append(updatedAssetData)
  
  return updatedAssetCargo