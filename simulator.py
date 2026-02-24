def simulate_hardware():
    seed = 12345
    features = ["MonsoonIntensity", "TopographyDrainage", "RiverManagement", "Deforestation", "Urbanization", "ClimateChange", "DamsQuality", "Siltation", "AgriculturalPractices", "Encroachments", "IneffectiveDisasterPreparedness", "DrainageSystems", "CoastalVulnerability", "Landslides", "Watersheds", "DeterioratingInfrastructure", "PopulationScore", "WetlandLoss", "InadequatePlanning", "PoliticalFactors"]
    
    while True:
        payload = "{"
        for i in range(20):
            seed = (1103515245 * seed + 12345) % 2147483648
            val = (seed % 9) + 2
            payload += '"' + features[i] + '": ' + str(val)
            if i < 19:
                payload += ", "
        payload += "}"
        
        f = open('live_telemetry.json', 'w')
        f.write(payload)
        f.close()
        
        wait_counter = 0
        while wait_counter < 30000000:
            wait_counter += 1

simulate_hardware()