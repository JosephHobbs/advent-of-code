################################################################################
# aoc-run-solution.py
################################################################################

import argparse
import importlib
import logging
import os
import sys
import time

#
# Helper functions for script execution...
#

def _process_arguments() -> argparse.Namespace:
    '''
    Process command-line arguments in prep for execution.

    Define and process command-line arguments for this script. Return the
    processed arguments as a Namespace object.
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d', '--day',
        action='store',
        required=True,
        type=int)
    
    parser.add_argument(
        '--debug',
        action='store_true')
    
    parser.add_argument(
        '-p', '--puzzle',
        action='store',
        required=True,
        type=int)

    parser.add_argument(
        '-t', '--test',
        action='store_true'
    )
    
    parser.add_argument(
        '-y', '--year',
        action='store',
        required=True,
        type=int)
    
    return parser.parse_args()

#
# Helper Functions for Solution.
#

def read_input(filename: str) -> list:
    '''
    Reads in the input file and returns it as a list (line by line).
    '''

    data = []

    with open(filename) as input_file:
        for input_line in input_file:
            data.append(input_line.strip())

    return data

#
# Main
#

def main(aoc_year: int, aoc_day: int, aoc_puzzle: int, use_test: bool, use_debug: bool):

    # Validate that the input file exists. If test mode is enabled, generate
    # a path using the test file instead of the main input file. If the file
    # doesn't exist, exit out as we cannot continue.

    if use_test:
        input_filename = f'inputs/{aoc_year:04}-{aoc_day:02}-example.txt'
    else:
        input_filename = f'inputs/{aoc_year:04}-{aoc_day:02}-input.txt'

    if not os.path.isfile(input_filename):
        print(f'no input file found for {aoc_year} {aoc_day} at {input_filename}!')
        exit(1)

    # Validate that the solution module exists before attempting to import it.
    # If the file doesn't exist, exit out as we cannot continue.

    solution_module_name = f'{aoc_year:04}.{aoc_day:02}_{aoc_puzzle}_solution'
    solution_filename = f'solutions/{aoc_year:04}/{aoc_day:02}_{aoc_puzzle}_solution.py'

    if not os.path.isfile(solution_filename):
        print(f'no solution found for day {aoc_year} {aoc_day} puzzle {aoc_puzzle} at {solution_filename}!')
        exit(2)

    # Attempt to import the solution module. If this fails, we cannot continue.

    solution = None
    try:
        solution = importlib.import_module(name = f'solutions.{solution_module_name}')
    except ImportError as e:
        print(f'unable to load solution module: {e}')
        exit(3)

    # Read in the contents of the input file and run the solution. Return the
    # results to the user.

    start_time = time.time()
    result = solution.solve(input_filename, read_input(input_filename), use_debug)
    end_time = time.time()

    print(f'Result: {result}')
    print(f'Elapsed: {(end_time - start_time):.9f} secs')

#
# MAIN
#

if __name__ == '__main__':

    # Process program arguments

    args = _process_arguments()

    # Initialize the logging system

    logging_level = logging.INFO
    if args.debug:
        logging_level = logging.DEBUG

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging_level)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging_level)

    # Execute the main method!

    main(args.year, args.day, args.puzzle, args.test, args.debug)

################################################################################
# END
################################################################################
