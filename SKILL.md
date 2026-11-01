---
name: genpark-personal-agent-zone2-cardiorespiratory-fitness-skill
version: "1.0.0"
description: "Zero-dependency Karvonen Heart Rate Reserve (HRR) metabolic corridor calculator, Uth-Sørensen VO2max estimator, and weekly mitochondrial longevity load scheduler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Zone 2 Cardiorespiratory Fitness Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to optimize cardiovascular longevity, compute individual Karvonen Zone 2 training corridors (sub-lactate threshold < 2.0 mmol/L), estimate VO2max, and manage weekly mitochondrial base volume.

## Agent In-Context Capabilities

- **Karvonen HRR Precision**: Dynamically calculates lower and upper Zone 2 cardiac boundaries from measured or Tanaka-derived maximum heart rate and resting heart rate.
- **Uth-Sørensen VO2max Estimation**: Estimates cardiorespiratory functional capacity and all-cause mortality risk reduction.
- **Progressive Overload Aerobic Scheduling**: Enforces safe 10-15% weekly expansion towards the 150-180 minute mitochondrial fitness standard.

## Tools Summary

1. `calculate_zone2_metabolic_corridor`: Computes Zone 2 heart rate bounds (bpm), VO2max estimate, and fat oxidation rates.
2. `schedule_weekly_aerobic_dose`: Prescribes session breakdowns and progressive weekly minute targets.
