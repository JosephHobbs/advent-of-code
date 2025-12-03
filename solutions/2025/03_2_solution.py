################################################################################
# 03_2_solution.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

class Bank:

    def __init__(self, contents: str, max_cell_count: int):
        self.contents = str(contents)
        self.max_cell_count = max_cell_count
        self.cells_to_use = []
    
    def _next_pos(self, start_pos: int, offset: int) -> int:
        
        log.debug('  searching for next max from position %d with offset %d', start_pos, offset)

        value = -1
        value_pos = -1
        for i in range(start_pos, len(self.contents) - offset):
            if int(self.contents[i]) > value:
                value = int(self.contents[i])
                value_pos = i
        
        log.debug('    found value %d at position %d', value, value_pos)

        return value_pos


    def get_max_joltage(self) -> int:

        log.debug('processing bank contents: %s', self.contents)

        start_at = 0
        for i in range(self.max_cell_count, 0, -1):
            if len(self.cells_to_use) > 0:
                start_at = self.cells_to_use[-1] + 1
            self.cells_to_use.append(self._next_pos(start_at, i - 1))

        result = ''
        for idx in self.cells_to_use:
            result += str(self.contents[idx])

        return int(result)


def solve(input_filename: str, input_data: list, use_debug: bool) -> str:
    
    result = 0

    for bank_contents in input_data:
        bank = Bank(bank_contents, 12)
        result += bank.get_max_joltage()

    return result

################################################################################
# END
################################################################################
