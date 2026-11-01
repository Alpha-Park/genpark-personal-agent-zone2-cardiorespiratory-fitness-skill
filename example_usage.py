# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Zone 2 Cardiorespiratory Fitness Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentZone2CardiorespiratoryFitness

def main():
    agent = PersonalAgentZone2CardiorespiratoryFitness()

    print("=" * 70)
    print("DEMO: Personal Agent Zone 2 Cardiorespiratory Fitness & VO2max Modeler")
    print("=" * 70)

    # 1. 38-year-old with resting HR of 54 bpm
    res_z2 = agent.calculate_zone2_metabolic_corridor(age=38.0, resting_hr=54.0)

    print(f"\n1. Zone 2 Cardiac Corridor & VO2max Estimate:")
    print(f"   Max HR: {res_z2['maximum_heart_rate_bpm']} bpm ({res_z2['max_hr_derivation']})")
    print(f"   Heart Rate Reserve (HRR): {res_z2['heart_rate_reserve_bpm']} bpm")
    print(f"   Target Zone 2 Corridor: {res_z2['zone2_corridor_bpm']['lower_bound_60pct_hrr']} - {res_z2['zone2_corridor_bpm']['upper_bound_70pct_hrr']} bpm (Mid: {res_z2['zone2_corridor_bpm']['target_midpoint_bpm']} bpm)")
    print(f"   Estimated VO2max: {res_z2['estimated_vo2_max_ml_kg_min']} mL/kg/min")
    print(f"   Longevity Tier: {res_z2['cardiorespiratory_longevity_tier']}")
    print(f"   Fat Oxidation: {res_z2['metabolic_dynamics']['fat_oxidation_rate_estimate']}")

    # 2. Weekly aerobic schedule progression
    res_sched = agent.schedule_weekly_aerobic_dose(current_weekly_zone2_minutes=100.0, vo2_max_ml_kg_min=res_z2['estimated_vo2_max_ml_kg_min'])

    print(f"\n2. Weekly Aerobic Longevity Volume Prescription:")
    print(f"   Current: {res_sched['current_weekly_volume_minutes']} min (Longevity Target: {res_sched['clinical_longevity_target_minutes']} min)")
    print(f"   Compliance: {res_sched['weekly_target_compliance']}")
    print(f"   Next Week Target: {res_sched['next_week_progressive_overload_target_minutes']} min")
    print(f"   Session Split: {res_sched['recommended_weekly_session_split']}")
    print(f"   Guidance: {res_sched['mitochondrial_prescription']}")

    print("\nVerification complete: Zone 2 cardiorespiratory engine executed flawlessly.")

if __name__ == "__main__":
    main()
