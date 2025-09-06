#!/bin/bash
# run_all.sh
# Full pipeline: run predictors -> parse stats -> plot results

echo ">>> [1/3] Running gem5 experiments..."
./run_experiment.sh

echo ">>> [2/3] Parsing stats into CSV..."
./parse_stats.py

echo ">>> [3/3] Generating plots..."
./plot_results.py

echo "✅ All steps complete. Check results in ../results/summary/"
