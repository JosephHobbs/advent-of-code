#!/bin/sh
################################################################################
# aoc-get-inputs.sh
#
# Fetches the input and example data for a given Advent of Code day and year,
# and writes the results to the inputs directory for later use.
################################################################################

# Export our AOC_SESSION variable from the .aoc-session file
export AOC_SESSION=$(cat .aoc-session)

#
# Make sure the required arguments year and day) are provided.
#

if [[ -z "${1}" ]]
then
  echo "Usage: ${0} <year> <day>"
  exit 1
fi
aoc_year=${1}

if [[ -z "${2}" ]]
then
  echo "Usage: ${0} <year> <day>"
  exit 1
fi
aoc_day=`printf "%02d" ${2}`

#
# Use aocd to pull the inputs and example data for the given year and day. Then
# process the example data to extract just the relevant portion into its own
# file so it's easier to use later.
#

aocd ${2} ${1} > inputs/${aoc_year}-${aoc_day}-input.txt
aocd ${2} ${1} --example > inputs/${aoc_year}-${aoc_day}-example-raw.txt

sed -n '/------------------------------- Example/,/--------------------------------------------------------------------------------/p' inputs/${aoc_year}-${aoc_day}-example-raw.txt | sed '1d' | sed '$d' > inputs/${aoc_year}-${aoc_day}-example.txt

################################################################################
# END
################################################################################
