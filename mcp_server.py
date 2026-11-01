# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Zone 2 Cardiorespiratory Fitness Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentZone2CardiorespiratoryFitness

mcp = FastMCP("PersonalAgentZone2CardiorespiratoryFitness")
client = PersonalAgentZone2CardiorespiratoryFitness()

@mcp.tool()
def calculate_zone2_metabolic_corridor(
    age: float,
    resting_hr: float = 58.0,
    max_hr: float = None
) -> str:
    """Calculates Karvonen Zone 2 heart rate training corridor and Uth-Sørensen VO2max."""
    import json
    return json.dumps(client.calculate_zone2_metabolic_corridor(age, resting_hr, max_hr), indent=2)

@mcp.tool()
def schedule_weekly_aerobic_dose(
    current_weekly_zone2_minutes: float = 90.0,
    vo2_max_ml_kg_min: float = 42.0
) -> str:
    """Prescribes weekly progressive Zone 2 aerobic volume and session splits for longevity."""
    import json
    return json.dumps(client.schedule_weekly_aerobic_dose(current_weekly_zone2_minutes, vo2_max_ml_kg_min), indent=2)

if __name__ == "__main__":
    mcp.run()
