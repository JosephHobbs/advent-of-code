################################################################################
# 04_1_solution.py
################################################################################

import logging
from utils.grid import Coordinate, Grid

log = logging.getLogger('solution')

#
#
#



#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    rows = len(input_data[0].strip())
    cols = len(input_data)

    grid = Grid()
    for line in input_data:
        grid.add_row_str(line.strip())

    accessible_rolls = 0
    for y in range(rows):
        for x in range(cols):
            coord = grid.get_coordinate(x, y)
            if coord.get_value_str(Coordinate.Position.CENTER) == '@':
                log.debug('found paper roll at %d:%d', x, y)

                adjacent_rolls = 0
                for neighbor in Coordinate.Position:
                    if neighbor == Coordinate.Position.CENTER:
                        continue
                    if coord.get_value_str(neighbor) == '@':
                        log.debug(' found adjacent roll at %s', neighbor.name)
                        adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    log.debug(' roll at %d:%d is accessible', x, y)
                    accessible_rolls += 1

    return str(accessible_rolls)

################################################################################
# END
################################################################################
