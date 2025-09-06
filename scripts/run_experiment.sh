#!/bin/bash
# run_experiment.sh
# Run gem5 O3CPU with multiple branch predictors
# Saves results in ../results/raw/<BP>/

# -------------------
# Config
# -------------------
GEM5=~/HPC-Projects/gem5/build/X86/gem5.opt
SE=~/HPC-Projects/gem5/configs/deprecated/example/se.py
PROG=~/HPC-Projects/gem5/tests/test-progs/hello/bin/x86/linux/hello

# Branch predictors to test
BPS=("TournamentBP" "LocalBP" "BiModeBP" "LTage")

# -------------------
# Run each predictor
# -------------------
for BP in "${BPS[@]}"; do
    OUTDIR="../results/raw/${BP}"
    echo ">>> Running $BP"
    mkdir -p $OUTDIR

    $GEM5 \
        --outdir=$OUTDIR \
        $SE \
        -c $PROG \
        --cpu-type=O3CPU \
        --bp-type=$BP \
        --caches --l2cache
done

