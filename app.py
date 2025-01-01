import streamlit as st
from inference_engine import run_inference_engine

def main():
    st.title("Renewable Energy Recommendation and Optimization Expert System")

    st.write("This expert system provides tailored recommendations for renewable energy solutions based on your inputs.")

    # Collect user inputs
    terrain = st.selectbox("Select your terrain type", ["flat", "hilly", "coastal", "unknown"])
    climate = st.selectbox("Select your climate", ["sunny", "windy", "moderate", "unknown"])
    energy_consumption = st.number_input("Average energy consumption per month (kWh):", min_value=0, step=10)
    budget = st.number_input("Estimated budget for installation ($):", min_value=0, step=100)
    land_size = st.number_input("Available land size for installation (sqm):", min_value=0, step=10)
    maintenance_preference = st.selectbox("Preferred maintenance level:", ["Low", "Medium", "High"])
    seasonal_variations = st.selectbox("Does your location experience significant seasonal changes?", ["Yes", "No"])

    # Get recommendations
    if st.button("Get Recommendation"):
        recommendations = run_inference_engine(
            terrain=terrain,
            climate=climate,
            energy_consumption=energy_consumption,
            budget=budget,
            land_size=land_size,
            maintenance_preference=maintenance_preference,
            seasonal_variations=seasonal_variations
        )

        # Display results
        if recommendations:
            st.subheader("Recommendations")
            for recommendation, alternatives in recommendations:
                st.success(recommendation)
                st.info(f"Alternatives: {', '.join(alternatives)}")
        else:
            st.error("No suitable recommendation found for the given inputs.")

if __name__ == "__main__":
    main()

