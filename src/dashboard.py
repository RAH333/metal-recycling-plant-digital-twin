import time
from data_generator import generate_plant_telemetry
from segregation_analyzer import SegregationAnalyzer
from safety_monitor import SafetyMonitor

def run_control_room_simulation(runtime_cycles=5):
    analyzer = SegregationAnalyzer()
    monitor = SafetyMonitor()
    
    print("==================================================================")
    print("      DESIRE METALS RECYCLING PLANT - DIGITAL TWIN SYSTEM         ")
    print("==================================================================\n")
    
    for i in range(runtime_cycles):
        telemetry = generate_plant_telemetry()
        route_action = analyzer.process_material(telemetry["scanned_material"])
        alerts = monitor.evaluate_telemetry(telemetry)
        
        print(f"--- [Timestamp: {telemetry['timestamp']}] Line Status Update ---")
        print(f" Material Detected : {telemetry['scanned_material']} -> Action: {route_action}")
        print(f" Sorting Accuracy  : {telemetry['sorting_accuracy_pct']}%")
        print(f" Shredder Vibration: {telemetry['shredder_vibration_mm_s']} mm/s | Furnace Temp: {telemetry['furnace_temp_celsius']}°C")
        print(f" Active Plant Safety Alerts: {alerts}")
        print(f" Cumulative Plant Yield Efficiency: {analyzer.get_segregation_efficiency()}%\n")
        
        time.sleep(1)

if __name__ == "__main__":
    run_control_room_simulation()
  
