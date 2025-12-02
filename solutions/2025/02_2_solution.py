################################################################################
# 02_1_solution.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

def check_for_silly(product_id: int) -> bool:

    # Found a more general solution that works for repeating patterns of any
    # length on geeksforgeeks.org. Way easier than my original solution.
    # https://www.geeksforgeeks.org/python/python-check-if-string-repeats-itself/

    product_id_str = str(product_id)
    result = product_id_str in (product_id_str + product_id_str)[1:-1]
    return result


def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    source_data = str(input_data[0]).split(',')

    result = 0

    for data_raw in source_data:
        id1, id2 = data_raw.split('-', 2)

        log.debug('processing range %s to %s', id1, id2)
        for i in range(int(id1), int(id2) + 1):
            if check_for_silly(i):
                log.debug('  found silly product id: %d', i)
                result += i
            
    return str(result)

################################################################################
# END
################################################################################
