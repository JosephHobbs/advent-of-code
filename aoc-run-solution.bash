#!/bin/bash
################################################################################
# aoc-run-solution.bash
################################################################################

if [[ -d ".venv" ]]
then
  echo "Using existing virtual environment..."
  source .venv/bin/activate
else
  echo "Initializing new virtual environment..."
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
fi

python3 aoc-run-solution.py $@

################################################################################
# END
################################################################################
