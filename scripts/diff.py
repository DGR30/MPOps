import json
import os
import sys

print("=== MPOps Diff Check ===")

baseline_path = "baseline_perf.json"

if not os.path.exists(baseline_path):
    print("No baseline found. Creating baseline.")
    os.rename("current_perf.json", baseline_path)
    sys.exit(0)

with open(baseline_path) as f:
    baseline = json.load(f)

with open("current_perf.json") as f:
    current = json.load(f)

delta = current["accuracy"] - baseline["accuracy"]

print("Baseline accuracy:", baseline["accuracy"])
print("Current accuracy:", current["accuracy"])
print("Delta:", delta)

if delta < -0.02:
    print("❌ Performance regression detected")
    sys.exit(1)

print("✅ Performance stable")