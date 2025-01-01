

from experta import *

class RenewableEnergyKnowledgeBase(KnowledgeEngine):
    @DefFacts()
    def _initial_fact(self):
        yield Fact(action="find_renewable_energy_solution")

    # Rule for Solar Energy Solution
    @Rule(Fact(terrain='flat'), Fact(climate='sunny'))
    def solar_energy_solution(self):
        self.declare(Fact(
            recommendation="Solar energy is ideal for your location.",
            alternatives=["Hybrid Solar-Wind", "Small Wind Turbines"]
        ))
        self.halt()  # Stop processing further rules

    # Rule for Wind Energy Solution
    @Rule(Fact(terrain='hilly'), Fact(climate='windy'))
    def wind_energy_solution(self):
        self.declare(Fact(
            recommendation="Wind energy is ideal for your location.",
            alternatives=["Micro-Hydro Power", "Hybrid Wind-Solar"]
        ))
        self.halt()  # Stop processing further rules

    # Rule for Tidal Energy Solution
    @Rule(Fact(terrain='coastal'), Fact(climate='moderate'))
    def tidal_energy_solution(self):
        self.declare(Fact(
            recommendation="Tidal energy is ideal for your location.",
            alternatives=["Offshore Wind Turbines", "Hybrid Tidal-Solar"]
        ))
        self.halt()  # Stop processing further rules

    # Rule for Large-Scale Solution (Energy consumption > 1000 kWh and Budget > 5000)
    @Rule(Fact(action='find_renewable_energy_solution'), Fact(energy_consumption=P(lambda x: x > 1000)), Fact(budget=P(lambda x: x > 5000)))
    def large_scale_solution(self):
        self.declare(Fact(
            recommendation="Large-scale solar farms are recommended for high energy demands and sufficient budget.",
            alternatives=["Wind Farms", "Hydroelectric Power"]
        ))
        self.halt()  # Stop processing further rules

    # Rule for Small-Scale Solution (Land size < 20 sqm and Low maintenance)
    @Rule(Fact(action='find_renewable_energy_solution'), Fact(land_size=P(lambda x: x < 20)), Fact(maintenance_preference='Low'))
    def small_scale_solution(self):
        self.declare(Fact(
            recommendation="Compact solar panels or small wind turbines are ideal for limited land and low maintenance.",
            alternatives=["Hybrid Solar-Wind", "Community Solar Programs"]
        ))
        self.halt()  # Stop processing further rules

    # Rule for Seasonal Variations
    @Rule(Fact(action='find_renewable_energy_solution'), Fact(seasonal_variations='Yes'))
    def seasonal_solution(self):
        self.declare(Fact(
            recommendation="Hybrid renewable systems are recommended for locations with significant seasonal changes.",
            alternatives=["Battery Storage Systems", "Geothermal Energy"]
        ))
        self.halt()  # Stop processing further rules

    # Rule for Unknown Inputs (Unknown terrain or climate)
    @Rule(Fact(action='find_renewable_energy_solution'), 
          OR(Fact(terrain="unknown"), Fact(climate="unknown")), salience=10)
    def unknown_solution(self):
        self.declare(Fact(
            recommendation="Insufficient data to provide a precise recommendation.",
            alternatives=["No alternative, please provide details"]
        ))
        self.halt()  # Stop processing further rules
