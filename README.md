

# A2-gem5-HPC — Branch Prediction Experiments

## Overview
This project evaluates different branch prediction schemes in gem5 using an Out-of-Order CPU (O3CPU).  
We automate experiments, parse results into CSV, and generate plots for IPC and misprediction rate.

---

## Repo Structure
We implement/configure multiple branch predictors and evaluate them on an out-of-order (O3) core in gem5, reporting IPC, misprediction rate, and performance impact across workloads. See `reports/` for results and write-up.

Repo layout:
- `configs/` gem5 config scripts, preset CPU/BP settings
- `scripts/` run/parse scripts (bash/python), experiment harness
- `workloads/` binaries or build scripts for benchmarks
- `results/raw/` raw gem5 stats (not versioned except .gitkeep)
- `results/summary/` CSV tables, plots
- `reports/` figures and final report


## Current Status
- gem5 (v25.0.0.1) built successfully on WSL2
- O3CPU runs correctly with caches (`--caches --l2cache`)
- Verified baseline run with TournamentBP on hello-world benchmark
- Next step: wrapper scripts to automate experiments

#Update after step 3

## Progress Log

### 2025-09-06
- Built gem5 (v25.0.0.1) successfully on WSL2.
- Verified O3CPU runs correctly with `--caches` (L1) and optional `--l2cache`.
- Confirmed TournamentBP baseline run on the hello-world benchmark.
- Added `scripts/run_experiment.sh` to automate gem5 runs and save results in `results/raw/`.
- Verified that `stats.txt` captures both IPC and branch predictor statistics (lookups, squashes).

- **Setup:** Built gem5 (v25.0.0.1) on WSL2 successfully.
- **Experiment:** Ran hello-world on O3CPU + TournamentBP with `--caches --l2cache`.
- **Results:** Simulation completed; IPC and branch predictor stats confirmed in `stats.txt`.
- **Notes:** `configs/example/se.py` is deprecated; using `configs/deprecated/example/se.py` for now.

#Update after Step 4

### 2025-09-06 (Step 4)
- **Setup:** Extended `run_experiment.sh` to batch-run multiple branch predictors (TournamentBP, LocalBP, BiModeBP, LTage).
- **Experiment:** Automated gem5 runs now save results under `results/raw/<BP>/`.
- **Results:** Wrote a Python parser (`parse_stats.py`) that extracts IPC and misprediction rate from `stats.txt`.
- **Summary:** First CSV generated at `results/summary/results.csv` with IPC + mispred rates for all predictors.
- **Notes:** This enables easy plotting and comparison between predictors in the next step.

# update after step5

### 2025-09-06 (Step 5)
- **Setup:** Installed `feh` to view plots directly from WSL terminal.
- **Experiment:** Added `plot_results.py` to generate graphs from `results/summary/results.csv`.
- **Results:** Two bar charts saved in `results/summary/`:
  - `ipc_comparison.png`
  - `mispred_rate_comparison.png`
- **Notes:** Verified images open correctly using `feh`.


#Update after Step 6

### 2025-09-06 (Step 6)
- **Setup:** Created `run_all.sh` master script to automate the full pipeline.
- **Experiment:** Running `./scripts/run_all.sh` executes:
  1. Batch gem5 runs with all branch predictors
  2. Parsing of stats into `results/summary/results.csv`
  3. Plot generation (`ipc_comparison.png`, `mispred_rate_comparison.png`)
- **Results:** One-command reproducibility achieved.
- **Notes:** This script is the main entry point for running the entire project workflow.

#Update at step 7

### 2025-09-06 (Step 7)
- **Setup:** Added real workloads (PARSEC + MiBench) to make experiments realistic.
- **Workloads:**
  - **PARSEC blackscholes** → compute-heavy benchmark  
    Build steps:
    ```bash
    git clone https://github.com/bamos/parsec-benchmark.git ~/HPC-Projects/workloads/parsec
    cd ~/HPC-Projects/workloads/parsec
    source env.sh
    parsecmgmt -a build -p blackscholes
    ```
    Binary at:
    ```
    ~/HPC-Projects/workloads/parsec/pkgs/apps/blackscholes/inst/amd64-linux.gcc/bin/blackscholes
    ```
  - **MiBench basicmath_small** → branch-heavy benchmark  
    Build steps:
    ```bash
    git clone https://github.com/embecosm/mibench.git ~/HPC-Projects/workloads/mibench
    cd ~/HPC-Projects/workloads/mibench/automotive/basicmath
    make
    ```
    Binaries at:
    ```
    basicmath_small
    basicmath_large
    ```
- **Experiment:** These workloads will be integrated into `run_all.sh` so that results are saved under: results/raw/<workload>/<predictor>/

- **Results:** Prepared realistic benchmarks for IPC + misprediction evaluation.
- **Notes:** `workloads/` folder is ignored in Git. Each user must set up workloads locally by following these steps.

## step 8 fixed and ran run_all.sh and fixed plot file now we are plotting for TournamentBP LocalBP BiModeBP LTAGE

### 2025-09-06 (Step 9)
- **Setup:** Extended predictor list to prepare for *advanced predictors*.
- **Predictors:** Currently automated for:
  - TournamentBP
  - LocalBP
  - BiModeBP
  - LTAGE
- **Results:** Verified automation works for both `basicmath_small` (math-heavy) and `blackscholes` (computation-heavy). CSV + plots generated per workload and globally.
- **Next:** 
  - Add perceptron predictors (`MultiperspectivePerceptron8KB`, `MultiperspectivePerceptron64KB`)  
  - Implement custom `GshareBP`  
  - Increase instruction cap to 100M for fairness  
  - Add calibration mode for runtime estimation
