#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from engine import GameEngine
from field import StandardField
from rules import next_generation_std, IterativeStopRule

def main():
  """ Main entry function.
  Tries to run some tests for now.
  :returns: None.
  """

  def print_field(field):
    """ Prints the field to console window.
    :field: a field to be printed.
    :returns: None.
    """
    sys.stdout.write("== State ==\n")
    last_row = 0
    for coord in field.cells_coords():
      row = coord[0]
      if row > last_row:
        sys.stdout.write("\n")
        last_row = row
      if field.get_cell(coord):
        sys.stdout.write("*")
      else:
        sys.stdout.write(" ")
    sys.stdout.write("\n")
    sys.stdout.flush()

  # Make a simple test field
  field = StandardField(5, 5)
  field.set_cell((0,0), True)
  field.set_cell((0,1), True)
  field.set_cell((1,2), True)

  # Run an engine
  engine = GameEngine(next_generation_std, field, print_field)
  engine.run_until_true(IterativeStopRule(10))


if __name__ == "__main__":
  main()
