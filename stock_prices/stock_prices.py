#!/usr/bin/python
# Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices.

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?

import argparse


def find_max_profit(prices):
    # goal: find the maximum profit that can be made from a single buy and then sell of these stock prices.
    # 1. UNDERSTAND
    #                         buy        sell                            sell-buy=max profit
    #                          ⬇           ⬇                               ⬇   ⬇    ⬇
    # `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530 # 3800-270=3530,
    #                                          ⬆ not 2 b/c it comes after 3800
    # !! This means I CAN'T change the order in relation to each other.
    #
    # the current min price is automatically the first thing
    current_min_price_so_far = prices[0]
    max_profit_so_far = 0

    # I need to search, so I need to iterate or recurse, i can skip the first thing, since i stored it already
    for i in range(1, len(prices)):
        # check if this is the min price
        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
            print(current_min_price_so_far)
        # set the max profit


find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
