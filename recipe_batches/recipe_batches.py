#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    amount_I_can_make = None
    for ingredient, amount in recipe.items():
        if ingredient in ingredients:
            if amount_I_can_make == None:
                # reset the amount I can make to the amount I have int divided by the amount I need
                amount_I_can_make = ingredients[ingredient] // amount
        else:  # set amount to 0 and end loop if ingredient is missing
            amount_I_can_make = 0
            break
    return amount_I_can_make


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
