################################################################################
# 01_2_solution.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

class SafeDial():
    
    def __init__(self):
        self.position = 50
        self.zeros = 0

    def turn_left(self, steps: int):
        for _ in range(steps):
            self.position -= 1
            if self.position < 0:
                self.position = 99
            if self.position == 0:
                self.zeros += 1
   
    def turn_right(self, steps: int):
        for _ in range(steps):
            self.position += 1
            if self.position > 99:
                self.position = 0
            if self.position == 0:
                self.zeros += 1

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    dial = SafeDial()

    for line in input_data:
        direction = line[0]
        steps = int(line[1:])
        if direction == 'L':
            dial.turn_left(steps)
        elif direction == 'R':
            dial.turn_right(steps)
        else:
            raise ValueError(f"Unknown direction: {direction}")
        
    return str(dial.zeros)

################################################################################
# END
################################################################################
