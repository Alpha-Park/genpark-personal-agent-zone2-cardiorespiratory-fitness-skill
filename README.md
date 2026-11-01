# Personal Agent Zone 2 Cardiorespiratory Fitness Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Karvonen Heart Rate Reserve (HRR) metabolic corridor calculator, Uth-Sørensen VO2max estimator, and weekly mitochondrial longevity load scheduler.

## Architecture

```mermaid
flowchart TD
    Biometrics[Age, Resting HR, Measured/Tanaka Max HR] --> KarvonenEngine[Karvonen HRR Corridor Engine]
    KarvonenEngine --> Zone2Bounds[Zone 2 Lower & Upper BPM Corridor: 60-70% HRR]
    KarvonenEngine --> VO2Max[Uth-Sørensen VO2max & Longevity Tier]
    VolumeHistory[Current Weekly Aerobic Minutes] --> OverloadScheduler[Progressive Overload Scheduler]
    OverloadScheduler --> WeeklySplit[150-180 Min Target & Session Split]
```

## Quickstart

```python
from client import PersonalAgentZone2CardiorespiratoryFitness

agent = PersonalAgentZone2CardiorespiratoryFitness()
res = agent.calculate_zone2_metabolic_corridor(age=38.0, resting_hr=54.0)
print(f"Zone 2: {res['zone2_corridor_bpm']['lower_bound_60pct_hrr']} - {res['zone2_corridor_bpm']['upper_bound_70pct_hrr']} bpm | VO2max: {res['estimated_vo2_max_ml_kg_min']}")
```
