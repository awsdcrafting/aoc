#!/bin/bash

SESSION=$(cat ./session)
DAY=${1:-$(date +%-d)}
YEAR=${2:-$(date +%Y)}
url="https://adventofcode.com/$YEAR/day/$DAY/input"
mkdir -p "$YEAR/$DAY"
curl -o "$YEAR/$DAY/input" --cookie "$SESSION" "$url"

cp skeleton.py "$YEAR/$DAY/solve.py"

