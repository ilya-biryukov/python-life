#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

def next_generation_std(cell_value, cell_neighbors):
  """Returns whether the cell with cell_value and cell_neighbors must be dead or alive in a next generation.
  Rules were taken from a wikipedia entry: http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

  :cell_value: a value of a cell in a current generation(True if alive, False if dead)
  :cell_neighbors: iterable with all neighbors of a cell
  :returns: True if a cell must be alive in a next generation, False otherwise
  """
  def count_alive_and_dead(current_res, next_value):
    alive, dead = current_res
    if next_value:
      # Increment alive count
      alive += 1
    else:
      # Increment dead count
      dead += 1
    return (alive, dead)

  alive, dead = reduce(count_alive_and_dead, cell_neighbors, (0, 0))

  if cell_value and (alive < 2 or alive > 3):
    # Overcrowding or under-population
    return False
  elif not cell_value and alive == 3:
    # Reproduction
    return True

  return cell_value



class IterativeStopRule(object):
  """Stop rule for a game, based on a fixed number of iterations."""

  def __init__(self, iterations):
    if iterations < 1:
      raise ValueError("`iterations` must be non-negative integer")

    self._iterations = iterations
    self._counter = 0


  @property
  def iterations(self):
    return self._iterations


  def __call__(self, field):
    self._counter += 1
    if (self._counter == self._iterations):
      return True
    else:
      return False
