################################################################################
# 05_1_solution.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

class Range():

    def __init__(self, range: str):
        start, end = range.split('-')
        self.start = int(start)
        self.end = int(end)

class IngredientChecker():

    def __init__(self):
        self.ranges = []
    
    def add_range(self, range: Range):
        self.ranges.append(range)

    def is_in_range(self, ingredient: int) -> bool:
        for range in self.ranges:
            if ingredient >= range.start and ingredient <= range.end:
                return True
            
        return False

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    checker = IngredientChecker()
    ingredients = []

    for line in input_data:
        if not line.strip():
            continue
        if '-' in line:
            checker.add_range(Range(line))
        else:
            ingredients.append(int(line))
        
    count_good = 0
    for ingredient in ingredients:
        if checker.is_in_range(ingredient):
            count_good += 1
    
    return str(count_good)

################################################################################
# END
################################################################################
