import streamlit as st
from inference_engine import run_inference_engine

def main():
    st.title("Renewable Energy Recommendation and Optimization Expert System")

    st.write("This system provides tailored recommendations for implementing renewable energy solutions based on your location's geographical and climate conditions.")

    # Collecting user inputs
    terrain = st.selectbox("Select your terrain type", ["flat", "hilly", "coastal"])
    climate = st.selectbox("Select your climate", ["sunny", "windy", "moderate"])
    
    # Additional questions
    energy_consumption = st.number_input("How much energy do you consume on average per month (in kWh)?", min_value=0)
    budget = st.number_input("What is your estimated budget for installing renewable energy solutions?", min_value=0)
    land_size = st.number_input("How much land do you have available for installing energy systems (in square meters)?", min_value=0)
    maintenance_preference = st.selectbox("How much maintenance are you willing to perform?", ["Low", "Medium", "High"])
    seasonal_variations = st.selectbox("Does your location experience significant seasonal changes?", ["Yes", "No"])

    if st.button("Get Recommendation"):
        # Call the inference engine to process the input and get the recommendation
        recommendation = run_inference_engine(
            terrain, climate, energy_consumption, budget, land_size, maintenance_preference, seasonal_variations
        )
        
        # Display the recommendation in the frontend
        if recommendation:
            st.success(recommendation)
        else:
            st.error("No recommendation available for the given input.")

if __name__ == "__main__":
    main()
