
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
