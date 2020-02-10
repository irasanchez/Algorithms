#!/usr/bin/python
# Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices.

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?

import argparse


def find_max_profit(prices):
    current_min_price_so_far = prices[0]

    # ⬇ can't use a number cause what if the possible profit is actually a loss?
    max_profit_so_far = None

    for i in range(1, len(prices)):
        possible_max = prices[i] - current_min_price_so_far
        # handle smaller values
        if prices[i] < current_min_price_so_far:
            # if max is none reset it
            if max_profit_so_far is None:
                max_profit_so_far = prices[i] - current_min_price_so_far
            # if this is the new max, reset it
            if possible_max > max_profit_so_far:
                max_profit_so_far = prices[i] - current_min_price_so_far
            # set the min price if the index is smaller than the current min price
            current_min_price_so_far = prices[i]
        # handle larger values
        if prices[i] > current_min_price_so_far:
            # if max is none reset it
            if max_profit_so_far is None:
                max_profit_so_far = prices[i] - current_min_price_so_far
            # set the max profit if there's a new one
            elif possible_max > max_profit_so_far:
                max_profit_so_far = prices[i] - current_min_price_so_far

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
