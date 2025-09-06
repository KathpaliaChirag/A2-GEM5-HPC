#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = "../results/summary/results.csv"
OUT_DIR = "../results/summary"

def plot_global(df):
    """Global comparison across all workloads (averages)."""
    grouped = df.groupby("BranchPredictor").mean(numeric_only=True)

    # IPC comparison
    plt.figure(figsize=(6,4))
    grouped["IPC"].plot(kind="bar", legend=False)
    plt.title("Average IPC (all workloads)")
    plt.ylabel("IPC")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "ipc_comparison.png"))
    plt.close()

    # Misprediction rate comparison
    plt.figure(figsize=(6,4))
    grouped["MispredRate"].plot(kind="bar", legend=False)
    plt.title("Average Misprediction Rate (all workloads)")
    plt.ylabel("Misprediction Rate")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "mispred_rate_comparison.png"))
    plt.close()

def plot_per_workload(df):
    """Separate plots for each workload."""
    for wl, group in df.groupby("Workload"):
        # IPC plot
        plt.figure(figsize=(6,4))
        plt.bar(group["BranchPredictor"], group["IPC"])
        plt.title(f"IPC for {wl}")
        plt.ylabel("IPC")
        plt.xlabel("Branch Predictor")
        plt.tight_layout()
        plt.savefig(os.path.join(OUT_DIR, f"{wl}_ipc.png"))
        plt.close()

        # Misprediction Rate plot
        plt.figure(figsize=(6,4))
        plt.bar(group["BranchPredictor"], group["MispredRate"])
        plt.title(f"Misprediction Rate for {wl}")
        plt.ylabel("Misprediction Rate")
        plt.xlabel("Branch Predictor")
        plt.tight_layout()
        plt.savefig(os.path.join(OUT_DIR, f"{wl}_mispred.png"))
        plt.close()

def main():
    df = pd.read_csv(CSV_FILE)

    # Drop rows with missing IPC (like old LTage typo runs)
    df = df.dropna(subset=["IPC"])

    print("✅ Generating global plots...")
    plot_global(df)

    print("✅ Generating per-workload plots...")
    plot_per_workload(df)

    print(f"✅ Plots saved in {OUT_DIR}")

if __name__ == "__main__":
    main()
