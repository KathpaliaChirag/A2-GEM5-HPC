We implement/configure multiple branch predictors and evaluate them on an out-of-order (O3) core in gem5, reporting IPC, misprediction rate, and performance impact across workloads. See `reports/` for results and write-up.

Repo layout:
- `configs/` gem5 config scripts, preset CPU/BP settings
- `scripts/` run/parse scripts (bash/python), experiment harness
- `workloads/` binaries or build scripts for benchmarks
- `results/raw/` raw gem5 stats (not versioned except .gitkeep)
- `results/summary/` CSV tables, plots
- `reports/` figures and final report
