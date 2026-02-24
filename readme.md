AI-Powered Flood & Disaster Resilience System 🌊
This project is a real-time environmental monitoring and predictive analytics platform designed to provide early warnings for flood disasters. By combining a simulated Internet of Things (IoT) architecture with Machine Learning (ML), the system processes live environmental telemetry to calculate flood probabilities for regions like Tamil Nadu.

📋 Project Overview
The system analyzes 20 critical environmental variables (such as Monsoon Intensity, River Management, and Deforestation) through a Random Forest regression model. It features a live IoT simulator that streams data into a centralized monitoring dashboard for real-time decision-making.

🛠️ Tech Stack
Language: Python 3.x

ML Framework: Scikit-learn, Pandas, NumPy

Dashboard: Streamlit

Data Format: JSON, CSV

🚀 Getting Started
1. Prerequisites
Ensure you have Python installed. You can check by running:

Bash
python --version
2. Installation
Clone this repository and install the required dependencies:

Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
3. Training the Model
If you need to retrain the model using the provided flood.csv:

Open the training script in Google Colab or locally.

Ensure flood.csv is in the directory.

Run the script to generate flood_prediction_model.pkl.

4. Running the System
To see the full end-to-end pipeline, you need to run two processes simultaneously:

Step A: Start the IoT Simulator (Simulates live sensor data)

Bash
python simulator.py
Step B: Launch the Dashboard (Open a new terminal)

Bash
python -m streamlit run app.py
📊 Core Features
Virtual Sensor Network: Continuous generation of 20 environmental metrics.

Predictive Engine: Real-time risk scoring using Random Forest.

Automated Alerts: Visual health statuses (Normal, Warning, Critical) based on ML thresholds.

🎯 Objectives
Demonstrate a complete end-to-end IoT-to-ML data pipeline.

Provide a scalable architecture for disaster mitigation.

Enable rapid deployment of early-warning systems in high-risk zones.
