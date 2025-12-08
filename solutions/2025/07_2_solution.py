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

def dfs(grid: Grid, coord: Coordinate, visit: set) -> int:
        
    log.debug('checking %d:%d', coord.x, coord.y)
    if (
#        coord.get_value_str(Coordinate.Position.LEFT) == None
#        or coord.get_value_str(Coordinate.Position.CENTER_UP) == None
#        or coord.get_value_str(Coordinate.Position.RIGHT) == None
        coord in visit
        or coord.get_value_str(Coordinate.Position.CENTER) == '.'
    ):
        log.debug('returning 0')
        return 0
    
    if coord.get_value_str(Coordinate.Position.CENTER_DOWN) == None:
        log.debug('returning 1')
        return 1

    visit.add(coord)

    # count = 0
    # count += dfs(grid, grid.get_coordinate(coord.x, coord.y + Coordinate.Position.CENTER_DOWN.y_offset), visit)
    # count += dfs(grid, grid.get_coordinate(coord.x + Coordinate.Position.LEFT.x_offset, coord.y + Coordinate.Position.CENTER_DOWN.y_offset), visit)
    # count += dfs(grid, grid.get_coordinate(coord.x + Coordinate.Position.RIGHT.x_offset, coord.y + Coordinate.Position.CENTER_DOWN.y_offset), visit)

    count = 0
    if coord.get_value_str(Coordinate.Position.CENTER_DOWN) == '|':
        count += dfs(grid, grid.get_coordinate(coord.x, coord.y + Coordinate.Position.CENTER_DOWN.y_offset), visit)
    elif coord.get_value_str(Coordinate.Position.CENTER_DOWN) == '^':
        count += dfs(grid, grid.get_coordinate(coord.x + Coordinate.Position.LEFT.x_offset, coord.y + Coordinate.Position.CENTER_DOWN.y_offset), visit)
        count += dfs(grid, grid.get_coordinate(coord.x + Coordinate.Position.RIGHT.x_offset, coord.y + Coordinate.Position.CENTER_DOWN.y_offset), visit)


    visit.remove(coord)

    log.debug('returning %d', count)
    return count
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

    #
    #
    #

    starting_x = str(input_data[0]).find('S')
    starting_coord = grid.get_coordinate(starting_x, 1)

    paths = dfs(grid, starting_coord, set())

    return str(paths)

################################################################################
# END
################################################################################
