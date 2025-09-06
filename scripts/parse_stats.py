#!/usr/bin/env python3
import os
import re
import csv

RAW_DIR = "../results/raw"
OUT_FILE = "../results/summary/results.csv"

def extract_stats(stats_file):
    ipc = None
    lookups = 0
    mispred = 0

    with open(stats_file) as f:
        for line in f:
            if "sim_ipc" in line or "system.cpu.ipc" in line:
                ipc = float(line.split()[1])
            if "branchPred.lookups_0::total" in line:
                lookups = int(line.split()[1])
            if "branchPred.squashes_0::total" in line:
                mispred = int(line.split()[1])

    mispred_rate = (mispred / lookups) if lookups > 0 else 0
    return ipc, mispred_rate

def main():
    predictors = []
    rows = []

    for bp in os.listdir(RAW_DIR):
        stats_file = os.path.join(RAW_DIR, bp, "stats.txt")
        if os.path.isfile(stats_file):
            ipc, mispred_rate = extract_stats(stats_file)
            predictors.append(bp)
            rows.append((bp, ipc, mispred_rate))

    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["BranchPredictor", "IPC", "MispredRate"])
        writer.writerows(rows)

    print(f"✅ Results written to {OUT_FILE}")

if __name__ == "__main__":
    main()
