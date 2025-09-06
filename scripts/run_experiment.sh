#!/bin/bash
# run_experiment.sh
# Wrapper script to run gem5 with O3CPU + branch predictor
# Saves results into ../results/raw/

# -------------------
# Arguments
# -------------------
BP=$1            # branch predictor (e.g., TournamentBP, LocalBP, BiModeBP)
OUTDIR="../results/raw/${BP}"

# -------------------
# Paths (adjust if your gem5 folder is elsewhere)
# -------------------
GEM5=~/HPC-Projects/gem5/build/X86/gem5.opt
SE=~/HPC-Projects/gem5/configs/deprecated/example/se.py
PROG=~/HPC-Projects/gem5/tests/test-progs/hello/bin/x86/linux/hello

# -------------------
# Run
# -------------------
mkdir -p $OUTDIR

$GEM5 \
    --outdir=$OUTDIR \
    $SE \
    -c $PROG \
    --cpu-type=O3CPU \
    --bp-type=$BP \
    --caches --l2cache
