import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

model = joblib.load('flood_prediction_model.pkl')

st.title("🌊 Smart Flood Prediction Dashboard")
st.markdown("Real-time environmental monitoring and early-warning ML system.")

features = [
    'MonsoonIntensity', 'TopographyDrainage', 'RiverManagement', 'Deforestation', 
    'Urbanization', 'ClimateChange', 'DamsQuality', 'Siltation', 'AgriculturalPractices', 
    'Encroachments', 'IneffectiveDisasterPreparedness', 'DrainageSystems', 
    'CoastalVulnerability', 'Landslides', 'Watersheds', 'DeterioratingInfrastructure', 
    'PopulationScore', 'WetlandLoss', 'InadequatePlanning', 'PoliticalFactors'
]

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("IoT Sensor Hub")
    st.write("Fetch latest environmental telemetry.")
    fetch_data = st.button("Fetch Live Sensor Data", use_container_width=True)

with col2:
    st.subheader("AI System Status")
    
    if fetch_data:
        live_data = {feature: np.random.randint(2, 11) for feature in features}
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Monsoon Intensity", live_data['MonsoonIntensity'])
        m2.metric("Dams Quality", live_data['DamsQuality'])
        m3.metric("Drainage Systems", live_data['DrainageSystems'])
        m4.metric("River Mgmt", live_data['RiverManagement'])
        
        input_df = pd.DataFrame([live_data])
        
        with st.spinner("Processing through ML Model..."):
            time.sleep(0.5)  
            
            probability = model.predict(input_df)[0]
            prob_percent = probability * 100
            
            st.markdown("### Estimated Flood Probability:")
            if prob_percent > 55:
                st.error(f"🚨 CRITICAL: {prob_percent:.2f}% Risk of Flooding detected! Initiate emergency protocols.")
            elif prob_percent > 45:
                st.warning(f"⚠️ WARNING: {prob_percent:.2f}% Risk. Monitor conditions closely.")
            else:
                st.success(f"✅ NORMAL: {prob_percent:.2f}% Risk. Conditions are stable.")
    else:
        st.info("System standing by. Click 'Fetch Live Sensor Data' to ping the network.")