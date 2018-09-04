#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = 0
  buyPrice = 0
  sellPrice = 0

  for i in range(len(prices)-1):
    if prices[i] < prices[i+1] and buyPrice == 0:
      buyPrice = prices[i]
    if prices[i] > prices[i+1] and buyPrice != 0:
      sellPrice = prices[i]
    if buyPrice !=0 and sellPrice !=0 and sellPrice - buyPrice > profit:
      profit = sellPrice - buyPrice
      buyPrice = 0
      sellPrice = 0
  if profit == 0:
    return -10
  else:
    return profit




if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))