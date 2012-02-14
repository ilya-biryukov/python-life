#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


class GameEngine(object):
  """Runs life game."""

  class GameState(object):
    """Stores the current state of the game.
    Runs iterations of the game. Used to make the code in GameEngine clearer."""

    def __init__(self, init_field):
      """
      :init_field: the first generation for the game.
      """

      self._current_field = deepcopy(init_field)
      self._new_field = deepcopy(init_field)


    @property
    def current_field(self):
      return self._current_field


    def _swap_new(self):
      """Swaps _current_field and _new_field.
      Used by run_one_iter.

      :returns: None.
      """

      tmp = self._current_field
      self._current_field = self._new_field
      self._new_field = tmp


    def run_one_iter(self, next_gen_rule):
      """Runs a single iteration of the game.

      :next_gen_rule: a rule function for transforming a cell to a new generation.
      :returns: None.
      """

      field = self._current_field

      def neighbors_value(coord):
        """ Accepts a coordinate of the cell and yields the values of it's neighbors.

        :coord: the coordinate of the cell, which neighbors should be yielded.
        :returns: generator yielding the values of the cell's neighbors.
        """
        for cell_coord in field.neighbors_coords(coord):
          yield field.get_cell(cell_coord)

      for cell_coord in field.cells_coords():
        new_value = next_gen_rule(field.get_cell(cell_coord), neighbors_value(cell_coord))
        self._new_field.set_cell(cell_coord, new_value)

      self._swap_new()



  def __init__(self, next_gen_rule, init_field, presenter):
    """
    :next_gen_rule: a callable that will be called with 2 arguments - a cell value and an iterable with cell's
      neighbors' values, based on that information should return the value that the cell should contain in a
      next generation of the game.
    :init_field: the first generation that should be used.
    :presenter: callable that will be called after each iteration of the game with a single arument of a modified field.
      Should be used to show the field output to the user.
    """

    self._next_gen_rule = next_gen_rule
    self._presenter = presenter
    self._state = GameEngine.GameState(init_field)


  @property
  def next_gen_rule(self):
    return self._next_gen_rule


  @next_gen_rule.setter
  def next_gen_rule(self, value):
    self._next_gen_rule = value


  def run_until_true(self, stop_predicate):
    """
      Runs iterations of the game until stop_predicate(field) returns True.
      :stop_predicate: a callable that is called before each iteration of the game, if it returns
        True the game will stop, otherwise it will continue.
      :returns: None.
    """
    # Show the initial state
    self._presenter(self._state.current_field)

    # While we are allowed to continue
    while not stop_predicate(self._state._current_field):
      # Run one iteration of the game
      self._state.run_one_iter(self._next_gen_rule)
      # Present the result
      self._presenter(self._state.current_field)
