################################################################################
# 06_1_solution.py
#
# Note: Pretty sure I took a round-about approach on this...  AND I forgot to
# copy off my part 1 before working part2.  GAH!
#
################################################################################

import logging
import math

log = logging.getLogger('solution')

#
#
#

class Homework:

    def __init__(self, data: list):
        self.data = self._preprocess3(
            self._preprocess2(
                self._preprocess1(data)))

    def _preprocess1(self, data: list) -> list:

        ops_data = data[-1]

        last_start = 0
        current_op = ops_data[0]
        result = []
        for i in range(1, len(ops_data)):
            
            if ops_data[i] == ' ':
                continue

            part = [ current_op ]
            for j in range(0, len(data) - 1):
                part.append(str(data[j][last_start:(i - 1)]))

            result.append(part)
            
            last_start = i
            current_op = ops_data[i]

        part = [ current_op ]
        for i in range(0, len(data) - 1):
            part.append(str(data[i][last_start:]))

        value_len = len(max(part, key=len))
        for i in range(1, len(part)):
            if len(part[i]) < value_len:
                part[i] = str(part[i]).ljust(value_len)

        result.append(part)

        return result
        
    def _preprocess2(self, data: list) -> list:

        log.debug('BEFORE: %s', data)

        #
        #
        #

        result = []
        for x in range(len(data)):
            new_value = [ data[x][0] ]
            for y in range(1, len(data[x])):
                new_value.append(str(data[x][y])[::-1])
            result.append(new_value)

        log.debug('AFTER: %s', result)

        return result

    def _preprocess3(self, data: list) -> list:

        log.debug('BEFORE: %s', data)

        result = []

        for input in data:
            new_record = [ input[0] ]
            for x in range(len(input[1])):
                new_value = ''
                for y in range(1, len(input)):
                    new_value += input[y][x]
                new_record.append(int(new_value))
            result.append(new_record)

        log.debug('AFTER: %s', result)
        
        return result

    def _solve(self, values: list, operation: str) -> int:
        
        if operation == '*':
            return math.prod(values)
        if operation == '%':
            result = values[0]
            for i in range(1, len(values)):
                result = result // i
            return result
        if operation == '+':
            return sum(values)
        if operation == '-':
            result = values[0]
            for i in range(1, len(values)):
                result -= i
            return result

    def get_answer(self) -> int:

        total = 0
        for problem in self.data:
            values = problem[1:]
            operations = problem[0]
            answer = self._solve(values, operations)

            log.debug('%s : %s = %d', values, operations, answer )

            total += answer

        return total
#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    homework = Homework(input_data)    
    
    return str(homework.get_answer())

################################################################################
# END
################################################################################
