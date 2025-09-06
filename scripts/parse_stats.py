#!/usr/bin/env python3
import os, csv

RAW_DIR = "../results/raw"
OUT_FILE = "../results/summary/results.csv"

def extract_stats(stats_file):
    ipc, lookups, mispred = None, 0, 0
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
    rows = []
    for workload in os.listdir(RAW_DIR):
        wl_path = os.path.join(RAW_DIR, workload)
        if os.path.isdir(wl_path):
            for bp in os.listdir(wl_path):
                stats_file = os.path.join(wl_path, bp, "stats.txt")
                if os.path.isfile(stats_file):
                    ipc, mispred_rate = extract_stats(stats_file)
                    rows.append((workload, bp, ipc, mispred_rate))

    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Workload", "BranchPredictor", "IPC", "MispredRate"])
        writer.writerows(rows)

    print(f"✅ Results written to {OUT_FILE}")

if __name__ == "__main__":
    main()

