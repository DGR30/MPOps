import json

print("=== Evaluating Model ===")

with open("model.json") as f:
    model = json.load(f)

accuracy = model["accuracy"]

result = {
    "accuracy": accuracy
}

with open("current_perf.json", "w") as f:
    json.dump(result, f, indent=2)

print("Evaluation complete")
print("Accuracy:", accuracy)