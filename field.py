#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StandardField(object):
  """A standard 2-dimensional field.
  Each point is either occupied or not, so it's represented by a Boolean value """

  def __init__(self, rows, columns):
    self._rows = rows
    self._cols = columns
    self._cells = [False for x in xrange(0, rows * columns)]


  @property
  def rows(self):
    return self._rows


  @property
  def cols(self):
    return self._cols


  def cells_coords(self):
    """Coordinates of all cells in a field.
    :returns: Generator that yields all cells' coordinates that are in a field.
      The returned values are lexicographically sorted (row, column) pairs
    """
    for row in xrange(0, self.rows):
      for col in xrange(0, self.cols):
        yield (row, col)


  def neighbors_coords(self, cell_coord):
    """Coordinates of all cell's neighbors

    :cell_coord: coordinates of a cell for which the neighbors are being generated.
    :returns: generator that yields all cell's neighbors' coordinates.
    """

    cell_row, cell_col = cell_coord

    def is_valid_neighbor(row, col):
      return row >= 0 and row < self._rows \
        and col >= 0 and col < self._cols \
        and (row != cell_row or col != cell_col)

    for row in xrange(cell_row - 1, cell_row + 2):
      for col in xrange(cell_col - 1, cell_col + 2):
        if not is_valid_neighbor(row, col):
          continue
        yield (row, col)


  def _index_from_coord(self, cell_coord):
    """Returns an index in _cells list of the element with specified coordinates.

    :cell_coord: @todo
    :returns: @todo
    """

    row, col = cell_coord
    return col + row * self.cols


  def set_cell(self, cell_coord, value):
    """Sets cell's with coordinates cell_coord to value.
    Value must be True or False

    :cell_coord: coordinates of a cell.
    :value: value to be set.
    :returns: None.
    """

    self._cells[self._index_from_coord(cell_coord)] = value


  def get_cell(self, cell_coord):
    """Get a value of a cell with cell_coord coordinates.

    :cell_coord: coordinates of a cell(must be 2-element tuple)
    :returns: value stored in a specified cell
    """

    return self._cells[self._index_from_coord(cell_coord)]

