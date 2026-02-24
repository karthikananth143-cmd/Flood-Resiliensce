import json
import random
import time

def generate_telemetry():
    while True:
        telemetry = {
            "MonsoonIntensity": random.randint(2, 10),
            "TopographyDrainage": random.randint(2, 10),
            "RiverManagement": random.randint(2, 10),
            "Deforestation": random.randint(2, 10),
            "Urbanization": random.randint(2, 10),
            "ClimateChange": random.randint(2, 10),
            "DamsQuality": random.randint(2, 10),
            "Siltation": random.randint(2, 10),
            "AgriculturalPractices": random.randint(2, 10),
            "Encroachments": random.randint(2, 10),
            "IneffectiveDisasterPreparedness": random.randint(2, 10),
            "DrainageSystems": random.randint(2, 10),
            "CoastalVulnerability": random.randint(2, 10),
            "Landslides": random.randint(2, 10),
            "Watersheds": random.randint(2, 10),
            "DeterioratingInfrastructure": random.randint(2, 10),
            "PopulationScore": random.randint(2, 10),
            "WetlandLoss": random.randint(2, 10),
            "InadequatePlanning": random.randint(2, 10),
            "PoliticalFactors": random.randint(2, 10)
        }
        
        with open('live_telemetry.json', 'w') as f:
            json.dump(telemetry, f)
        
        time.sleep(3)

generate_telemetry()