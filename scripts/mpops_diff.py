import json
import sys
import os

baseline_path = "perf_store/baseline_perf.json"

if not os.path.exists(baseline_path):
    print("No baseline found. Skipping MPOps diff.")
    sys.exit(0)

with open(baseline_path) as f:
    baseline = json.load(f)

with open("current_perf.json") as f:
    current = json.load(f)

baseline_acc = baseline["accuracy"]
current_acc = current["accuracy"]
delta = current_acc - baseline_acc

print(f"Baseline accuracy: {baseline_acc}")
print(f"Current accuracy: {current_acc}")
print(f"Accuracy delta: {delta}")

# Regression threshold = -2%
if delta < -0.02:
    print("❌ MPOps regression detected")
    sys.exit(1)

print("✅ MPOps check passed")
