from experta import KnowledgeEngine, Fact, Rule
from knowledge_base import RenewableEnergyKnowledgeBase

def run_inference_engine(terrain, climate, energy_consumption, budget, land_size, maintenance_preference, seasonal_variations):
    engine = RenewableEnergyKnowledgeBase()

    # Reset the engine to ensure no old facts persist
    engine.reset()

    recommendation = None  # Initialize the recommendation variable

    # Create a callback to capture the recommendation
    class RecommendationCapture(KnowledgeEngine):
        @Rule(Fact(action='find_renewable_energy_solution'),
              Fact(terrain=terrain), Fact(climate=climate),
              Fact(energy_consumption=energy_consumption), Fact(budget=budget),
              Fact(land_size=land_size), Fact(maintenance_preference=maintenance_preference),
              Fact(seasonal_variations=seasonal_variations))
        def provide_recommendation(self):
            nonlocal recommendation
            if terrain == "flat" and climate == "sunny":
                recommendation = "Recommendation: Solar energy is ideal for your location."
            elif terrain == "hilly" and climate == "windy":
                recommendation = "Recommendation: Wind energy is ideal for your location."
            elif terrain == "coastal" and climate == "moderate":
                recommendation = "Recommendation: Tidal energy is ideal for your location."
            else:
                recommendation = "No suitable recommendation found for your input."
    
    # Run the inference engine with the new capture class
    capture_engine = RecommendationCapture()
    capture_engine.declare(Fact(action="find_renewable_energy_solution"))
    capture_engine.declare(Fact(terrain=terrain))
    capture_engine.declare(Fact(climate=climate))
    capture_engine.declare(Fact(energy_consumption=energy_consumption))
    capture_engine.declare(Fact(budget=budget))
    capture_engine.declare(Fact(land_size=land_size))
    capture_engine.declare(Fact(maintenance_preference=maintenance_preference))
    capture_engine.declare(Fact(seasonal_variations=seasonal_variations))
    capture_engine.run()

    return recommendation
