from experta import *

class RenewableEnergyKnowledgeBase(KnowledgeEngine):
    @DefFacts()
    def _initial_fact(self):
        # You can define some initial facts here if needed
        yield Fact(action="find_renewable_energy_solution")

    @Rule(Fact(action='find_renewable_energy_solution'), NOT(Fact(terrain=W())), NOT(Fact(climate=W())))
    def ask_for_terrain_and_climate(self):
        self.declare(Fact(terrain=input("Enter your terrain type (flat, hilly, coastal): ")))
        self.declare(Fact(climate=input("Enter your climate (sunny, windy, moderate): ")))

    @Rule(Fact(action='find_renewable_energy_solution'), NOT(Fact(energy_consumption=W())), NOT(Fact(budget=W())))
    def ask_for_energy_and_budget(self):
        self.declare(Fact(energy_consumption=input("How much energy do you consume on average per month (in kWh)? ")))
        self.declare(Fact(budget=input("What is your estimated budget for installing renewable energy solutions? ")))

    @Rule(Fact(action='find_renewable_energy_solution'), NOT(Fact(land_size=W())), NOT(Fact(maintenance_preference=W())))
    def ask_for_land_and_maintenance(self):
        self.declare(Fact(land_size=input("How much land do you have available for installing energy systems (in square meters)? ")))
        self.declare(Fact(maintenance_preference=input("How much maintenance are you willing to perform? (Low, Medium, High)")))

    @Rule(Fact(action='find_renewable_energy_solution'), NOT(Fact(seasonal_variations=W())))
    def ask_for_seasonal_variations(self):
        self.declare(Fact(seasonal_variations=input("Does your location experience significant seasonal changes? (Yes/No): ")))

    @Rule(Fact(action='find_renewable_energy_solution'), Fact(terrain='flat'), Fact(climate='sunny'))
    def solar_energy_solution(self):
        print("Recommendation: Solar energy is ideal for your location.")

    @Rule(Fact(action='find_renewable_energy_solution'), Fact(terrain='hilly'), Fact(climate='windy'))
    def wind_energy_solution(self):
        print("Recommendation: Wind energy is ideal for your location.")

    @Rule(Fact(action='find_renewable_energy_solution'), Fact(terrain='coastal'), Fact(climate='moderate'))
    def tidal_energy_solution(self):
        print("Recommendation: Tidal energy is ideal for your location.")

    # Additional rules can be added based on energy consumption, budget, land size, etc.
    # Example rule:
    @Rule(Fact(action='find_renewable_energy_solution'), Fact(energy_consumption=W()), Fact(budget=W()))
    def energy_and_budget_solution(self):
        # Add logic based on energy consumption and budget
        pass
