
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

