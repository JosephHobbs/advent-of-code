################################################################################
# 02_1_solution.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

def check_for_silly(product_id: int) -> bool:

    # Split the product ID into two halves and compare them. If they are the
    # same, this is a 'silly' product id.

    product_id_str = str(product_id)
    product_id_len = len(product_id_str)
    product_id_len_part = product_id_len // 2

    part1 = product_id_str[0:product_id_len_part]
    part2 = product_id_str[product_id_len_part:product_id_len]

    return part1 == part2


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
