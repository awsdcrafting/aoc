#!/bin/bash

DAY=${1:-$(date +%-d)}
YEAR=${2:-$(date +%Y)}

cd "$YEAR/$DAY/"
python solve.py