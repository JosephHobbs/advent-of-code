################################################################################
# 07_1_solution.py
################################################################################

import logging
from utils.grid import Coordinate, Grid

log = logging.getLogger('solution')

#
#
#

def dump_grid(grid: Grid) -> str:

    result = ''
    for y in range(grid.row_count):
        for x in range(grid.col_count):
            result += grid.get_coordinate(x, y).get_value_str(Coordinate.Position.CENTER)
        result += '\n'
    
    return result

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    log.debug('INPUT:')
    grid = Grid()
    for line in input_data:
        log.debug(line)
        grid.add_row_str(line.strip())
    log.debug('\n')

    grid.set_counts(
        len(input_data),
        len(input_data[0].strip()))

    log.debug('BEFORE:')
    log.debug(dump_grid(grid))

    total_splits = 0
    # done = False
    # while (not done):
    for y in range(grid.row_count):
        for x in range(grid.col_count):
            
            coord = grid.get_coordinate(x, y)
            
            log.debug('processing %d:%d => %s', x, y, coord.get_value_str(Coordinate.Position.CENTER))

            if coord.get_value_str(Coordinate.Position.CENTER_UP) == 'S':
                grid.set_coordinate_value(x, y, '|')
            elif coord.get_value_str(Coordinate.Position.CENTER) == '^':
                if coord.get_value_str(Coordinate.Position.CENTER_UP) == '|':
                    log.debug('detected split at %d:%d', x, y)
                    splits = 0
                    if coord.get_value_str(Coordinate.Position.LEFT) != '|':
                        log.debug('new tachyon left')
                        grid.set_coordinate_value(x + Coordinate.Position.LEFT.x_offset, y, '|')
                        splits += 1
                    if coord.get_value_str(Coordinate.Position.RIGHT) != '|':
                        log.debug('new tachyon right')
                        grid.set_coordinate_value(x + Coordinate.Position.RIGHT.x_offset, y, '|')
                        splits += 1
                    total_splits += 1
                    grid.set_coordinate_value(x + 1, y, '|')
            elif coord.get_value_str(Coordinate.Position.CENTER) == '.':
                if coord.get_value_str(Coordinate.Position.CENTER_UP) == '|':
                    grid.set_coordinate_value(x, y, '|')
                
    log.debug('AFTER:')
    log.debug(dump_grid(grid))

    return str(total_splits)

################################################################################
# END
################################################################################
