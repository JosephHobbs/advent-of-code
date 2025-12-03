################################################################################
# 03_1_solution.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

class Bank:

    def __init__(self, contents: str):
        self.contents = str(contents)
    
    def get_max_joltage(self) -> int:

        log.debug('processing bank contents: %s', self.contents)

        digit1 = -1
        digit1_pos = -1
        for i in range(len(self.contents) - 1):
            if int(self.contents[i]) > digit1:
                digit1 = int(self.contents[i])
                digit1_pos = i
        
        log.debug('  found digit 1 %d at position %d', digit1, digit1_pos)

        digit2 = -1
        for i in range(digit1_pos + 1, len(self.contents)):
            if int(self.contents[i]) > digit2:
                digit2 = int(self.contents[i])
        
        log.debug('  found digit 2 %d', digit2)

        return int(str(digit1) + str(digit2))



def solve(input_filename: str, input_data: list, use_debug: bool) -> str:
    
    result = 0

    for bank_contents in input_data:
        bank = Bank(bank_contents)
        result += bank.get_max_joltage()

    return result

################################################################################
# END
################################################################################
