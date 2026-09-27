# metal-recycling-plant-digital-twin
Metal Recycling Plant Digital Twin

# Metal Recycling Plant Digital Twin & Safety Monitor

An operations tracking framework modeled for modern automated metal recycling lines. This digital tool mimics real-world tasks required of a Plant Production Engineer: **scrap sorting automation, structural machine health monitoring, and rigorous safety threshold analytics**.

## Project Capabilities
- **Automated Material Sorting Logic**: Categorizes incoming scrap streams into Ferrous and Non-Ferrous sorting queues.
- **Predictive Mechanical Health Monitoring**: Continuously evaluates simulated sensor metrics (vibration levels, thermal tolerances) against critical safety thresholds.
- **Production Record Logging**: Dynamically monitors plant processing yield rates.

## How to Run locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the Control Room Dashboard simulation script:
   ```bash
   python src/dashboard.py
   ```

   
```
metal-recycling-plant-digital-twin/
├── README.md
├── requirements.txt
├── config/
│   └── threshold_config.json
├── data/
│   └── mock_sensor_data.csv
├── src/
│   ├── __init__.py
│   ├── data_generator.py
│   ├── segregation_analyzer.py
│   ├── safety_monitor.py
│   └── dashboard.py
└── tests/
    └── test_analyzers.py
```
