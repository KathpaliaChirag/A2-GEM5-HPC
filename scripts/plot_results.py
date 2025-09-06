#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# -------------------
# Config
# -------------------
CSV_FILE = "../results/summary/results.csv"
OUT_DIR = "../results/summary"

# -------------------
# Load data
# -------------------
df = pd.read_csv(CSV_FILE)

# -------------------
# Plot IPC
# -------------------
plt.figure(figsize=(6,4))
plt.bar(df["BranchPredictor"], df["IPC"])
plt.title("IPC for Different Branch Predictors")
plt.ylabel("Instructions Per Cycle (IPC)")
plt.xlabel("Branch Predictor")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/ipc_comparison.png")
plt.close()

# -------------------
# Plot Misprediction Rate
# -------------------
plt.figure(figsize=(6,4))
plt.bar(df["BranchPredictor"], df["MispredRate"])
plt.title("Misprediction Rate for Different Branch Predictors")
plt.ylabel("Misprediction Rate")
plt.xlabel("Branch Predictor")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/mispred_rate_comparison.png")
plt.close()

print("✅ Plots saved in results/summary/")
