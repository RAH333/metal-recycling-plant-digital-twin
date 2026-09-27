import json
import os

class SafetyMonitor:
    def __init__(self, config_path="config/threshold_config.json"):
        # Local paths logic for execution variations
        if not os.path.exists(config_path):
            self.config = {
                "shredder": {"max_vibration_mm_s": 7.5, "max_motor_temp_celsius": 85.0},
                "furnace": {"optimal_melting_temp_celsius": 1200.0, "max_safe_temp_celsius": 1500.0}
            }
        else:
            with open(config_path, "r") as f:
                self.config = json.load(f)

    def evaluate_telemetry(self, telemetry):
        """Evaluates plant safety & compliance status."""
        alerts = []
        
        # Check Shredder Vibration
        if telemetry["shredder_vibration_mm_s"] > self.config["shredder"]["max_vibration_mm_s"]:
            alerts.append(f"CRITICAL: High Shredder Vibration ({telemetry['shredder_vibration_mm_s']} mm/s)! Check for mechanical jamming.")
            
        # Check Furnace Temperature
        if telemetry["furnace_temp_celsius"] > self.config["furnace"]["max_safe_temp_celsius"]:
            alerts.append(f"DANGER: Furnace Overheating ({telemetry['furnace_temp_celsius']}°C)! Trigger cooling system sequence.")
            
        # Check PPE Compliance
        if telemetry["ppe_breach_detected"] == 1:
            alerts.append("COMPLIANCE ALERT: PPE Breach detected in the production area via safety vision automation.")
            
        return alerts if alerts else ["Status: Operational Safe State"]
      
