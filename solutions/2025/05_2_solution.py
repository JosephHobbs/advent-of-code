################################################################################
# 05_2_solution.py
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

def _combine_range(range1: Range, range2: Range) -> Range:

    log.debug('%d-%d vs. %d-%d', range1.start, range1.end, range2.start, range2.end)

    #         10     15 
    #     5                  20
    if range2.start <= range1.start <= range1.end <= range2.end:
        log.debug('range 1 completely inside range 2')
        return Range(str(range2.start) + '-' + str(range2.end))

    #     5                  20
    #         10     15 
    if range1.start <= range2.start <= range2.end <= range1.end:
        log.debug('range 2 completely inside range 1')
        return Range(str(range1.start) + '-' + str(range1.end))

    #     5          15
    #          10            20
    if range1.start <= range2.start <= range1.end <= range2.end:
        log.debug('range 2 overlaps end of range 1')
        return Range(str(range1.start) + '-' + str(range2.end))

    #          10            20
    #     5          15
    if range2.start <= range1.start <= range2.end <= range1.end:
        log.debug('range 2 overaps start of range 1')
        return Range(str(range2.start) + '-' + str(range1.end))
    
    log.debug('no overlap detected')
    return None

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    ranges = []

    for line in input_data:
        if not '-' in line:
            continue
        ranges.append(Range(line))

    log.debug('---------- BEFORE ----------')
    for rng in ranges:
        rng_count = rng.end - rng.start + 1
        log.debug('%d-%d = %d', rng.start, rng.end, rng_count)

    done = False
    while (not done):

        combine_left = None
        combine_right = None
        combination = None

        for x in range(len(ranges) - 1):
            left_range = ranges[x]
            for y in range(x + 1, len(ranges)):
                right_range = ranges[y]

                combination = _combine_range(left_range, right_range)
                if combination:
                    log.debug('new range: %d-%d', combination.start, combination.end)
                    combine_left = left_range
                    combine_right = right_range

                if combination:
                    break

            if combination:
                break

        if combination:
            ranges.remove(combine_left)
            ranges.remove(combine_right)
            ranges.append(combination)
        else:
            done = True

    log.debug('---------- AFTER ----------')
    total = 0
    for rng in ranges:
        rng_count = rng.end - rng.start + 1
        log.debug('%d-%d = %d', rng.start, rng.end, rng_count)
        total += rng_count

    return str(total)

################################################################################
# END
################################################################################
