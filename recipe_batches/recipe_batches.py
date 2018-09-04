#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  ratios = []

  for key in recipe:
    if key == key in ingredients:
      ratios.append(ingredients[key]/recipe[key])
      print('ratio: ', ratios)
      if min(ratios) < 1:
        return 0
      else:
        batches = min(ratios)
    else:
      return 0



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))