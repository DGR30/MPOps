import json
import random

print("=== Training Model ===")

accuracy = round(random.uniform(0.85, 0.95), 3)

model = {
    "model_name": "mpops-demo-model",
    "accuracy": accuracy
}

with open("model.json", "w") as f:
    json.dump(model, f)

print("Training complete")
print("Model accuracy:", accuracy)