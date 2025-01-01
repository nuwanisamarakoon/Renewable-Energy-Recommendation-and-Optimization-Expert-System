# Renewable-Energy-Recommendation-and-Optimization-Expert-System

This repository contains a Renewable Energy Recommendation and Optimization Expert System developed using Python, Experta, and Streamlit. The system provides tailored recommendations for renewable energy solutions based on user-provided inputs such as terrain type, climate, energy consumption, budget, land size, maintenance preference, and seasonal variations.

**Features**

Expert System Rules: Uses Experta to define rules for recommending renewable energy solutions.

Customizable Inputs: Accepts user inputs for various parameters to generate precise recommendations.

Hybrid Solutions: Suggests alternatives for situations with variable or uncertain conditions.

User-Friendly Interface: A Streamlit-based web application for seamless interaction.

**Files**

1. knowledge_base.py

   Contains the RenewableEnergyKnowledgeBase class with rules for renewable energy recommendations.

2. inference_engine.py

   Contains the run_inference_engine function that initializes the knowledge base, declares facts, and executes the inference engine.

3. app.py

  The main Streamlit application for interacting with the system.

Setup and Installation

**Prerequisites**

Python 3.8 or later

pip (Python package manager)

Required Libraries

Install the required libraries using the following command:

pip install experta streamlit

Usage

Running the Application

Clone the repository:

git clone <repository_url>

Navigate to the project directory:

cd <project_directory>

Run the Streamlit application:

streamlit run app.py

Open the provided URL in your web browser to access the application.

**Input Parameters**

  Terrain Type: Options include flat, hilly, coastal, or unknown.
  
  Climate: Options include sunny, windy, moderate, or unknown.
  
  Energy Consumption: Monthly average energy consumption in kWh.
  
  Budget: Estimated installation budget in USD.
  
  Land Size: Available land size for installation in square meters.
  
  Maintenance Preference: Preferred level of maintenance (Low, Medium, High).
  
  Seasonal Variations: Whether the location experiences significant seasonal changes (Yes or No).

**Recommendations**

The system provides:

A primary recommendation based on the provided inputs.

Alternative solutions for flexibility.

Example

Input parameters:

Terrain Type: flat

Climate: sunny

Energy Consumption: 1500

Budget: 10000

Land Size: 30

Maintenance Preference: Low

Seasonal Variations: No

**Output:**

Recommendation: "Solar energy is ideal for your location."

Alternatives: "Hybrid Solar-Wind, Small Wind Turbines"

Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m "Add feature").

Push to the branch (git push origin feature-branch).

Open a pull request.

**Contact**

Email: nunuwanisamarakoon.online@gmail.com
