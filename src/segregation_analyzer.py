class SegregationAnalyzer:
    def __init__(self):
        self.total_processed = 0
        self.ferrous_count = 0
        self.non_ferrous_count = 0
        self.waste_count = 0

    def process_material(self, material_type):
        """Categorizes and updates real-time inventory counts."""
        self.total_processed += 1
        if "Ferrous" in material_type:
            self.ferrous_count += 1
            return "Route to Magnetic Separator"
        elif "Non-Ferrous" in material_type:
            self.non_ferrous_count += 1
            return "Route to Eddy Current Separator"
        else:
            self.waste_count += 1
            return "Route to Disposal/Landfill"

    def get_segregation_efficiency(self):
        if self.total_processed == 0:
            return 0.0
        return round(((self.ferrous_count + self.non_ferrous_count) / self.total_processed) * 100, 2)
      
