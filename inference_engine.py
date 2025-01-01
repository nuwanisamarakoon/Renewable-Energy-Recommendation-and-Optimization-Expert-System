from knowledge_base import RenewableEnergyKnowledgeBase
from experta import Fact

def run_inference_engine(terrain=None, climate=None, energy_consumption=None, budget=None, land_size=None, maintenance_preference=None, seasonal_variations=None):
    # Assign default values for missing inputs
    terrain = terrain or "unknown"
    climate = climate or "unknown"
    energy_consumption = energy_consumption or 0
    budget = budget or 1000
    land_size = land_size or 50
    maintenance_preference = maintenance_preference or "Medium"
    seasonal_variations = seasonal_variations or "No"

    engine = RenewableEnergyKnowledgeBase()
    engine.reset()

    # Declare facts
    engine.declare(Fact(action="find_renewable_energy_solution"))
    engine.declare(Fact(terrain=terrain))
    engine.declare(Fact(climate=climate))
    engine.declare(Fact(energy_consumption=energy_consumption))
    engine.declare(Fact(budget=budget))
    engine.declare(Fact(land_size=land_size))
    engine.declare(Fact(maintenance_preference=maintenance_preference))
    engine.declare(Fact(seasonal_variations=seasonal_variations))

    # Run the inference engine
    engine.run()

    # Collect recommendations
    recommendations = [
        (fact['recommendation'], fact['alternatives'])
        for fact in engine.facts.values() if isinstance(fact, dict) and 'recommendation' in fact
    ]

    return recommendations
