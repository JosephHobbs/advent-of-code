#!/bin/sh
################################################################################
# aoc-run-solution.sh
################################################################################

if [[ -d ".venv" ]]
then
  echo "Using existing virtual environment..."
  source .venv/bin/activate
else
  echo "Initializing new virtual environment..."
  uv venv .venv
  source .venv/bin/activate
  uv pip install -r requirements.txt
fi

python3 aoc-run-solution.py $@

################################################################################
# END
################################################################################
