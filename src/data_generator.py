import random
import time
import pandas as pd

def generate_plant_telemetry():
    """Simulates a single stream of telemetry data from the recycling line."""
    materials = ["Ferrous (Iron/Steel)", "Non-Ferrous (Aluminum/Copper)", "Contaminant/Waste"]
    
    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "scanned_material": random.choice(materials),
        "sorting_accuracy_pct": round(random.uniform(92.0, 99.5), 2),
        "shredder_vibration_mm_s": round(random.uniform(2.0, 9.0), 2),  # intentionally crosses threshold sometimes
        "shredder_temp_celsius": round(random.uniform(50.0, 90.0), 2),
        "furnace_temp_celsius": round(random.uniform(1100.0, 1550.0), 2),
        "ppe_breach_detected": random.choices([0, 1], weights=[0.95, 0.05])[0]
    }
    return data

if __name__ == "__main__":
    print("Generating sample live log packet:")
    print(generate_plant_telemetry())
  
