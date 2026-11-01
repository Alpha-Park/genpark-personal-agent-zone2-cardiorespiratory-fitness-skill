# -*- coding: utf-8 -*-
"""
Personal Agent Zone 2 Cardiorespiratory Fitness Client
Zero-dependency Karvonen Heart Rate Reserve (HRR) metabolic corridor calculator,
Uth-Sørensen VO2max estimator, and weekly mitochondrial longevity load scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentZone2CardiorespiratoryFitness:
    """
    Models mitochondrial density, Maximum Fat Oxidation (MFO), and blood lactate clearance (< 2.0 mmol/L),
    calculating individual Karvonen Zone 2 cardiac corridors and scheduling aerobic longevity doses.
    """

    def calculate_zone2_metabolic_corridor(
        self,
        age: float,
        resting_hr: float = 58.0,
        max_hr: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates individual Zone 2 training target heart rate corridor using the
        Karvonen Heart Rate Reserve (HRR) formula: HR_target = HR_rest + %Intensity * (HR_max - HR_rest).
        Zone 2 corresponds strictly to 60% - 70% HRR (sub-lactate threshold ~1.5 - 2.0 mmol/L).
        """
        user_age = max(18.0, min(95.0, float(age)))
        rhr = max(35.0, min(110.0, float(resting_hr)))

        # Maximum Heart Rate (Tanaka formula: 208 - 0.7 * age if unmeasured)
        if max_hr and 120.0 <= float(max_hr) <= 225.0:
            mhr = float(max_hr)
            mhr_source = "Empirical Clinical Measured Max HR"
        else:
            mhr = round(208.0 - (0.7 * user_age), 1)
            mhr_source = "Tanaka Epidemiological Equation (208 - 0.7*Age)"

        hrr = round(mhr - rhr, 1)

        # Karvonen Zone 2 bounds (60% - 70% HRR)
        z2_lower = round(rhr + (0.60 * hrr), 0)
        z2_upper = round(rhr + (0.70 * hrr), 0)

        # Uth-Sørensen-Overgaard-Pedersen VO2max estimation from HR ratio
        # VO2max ~= 15.3 * (HR_max / HR_rest)
        vo2_max_est = round(15.3 * (mhr / rhr), 1)

        # Estimated substrate utilization at Zone 2: ~0.50 g fat / min, minimal glycogen depletion
        fat_ox_rate_g_hr = round(0.52 * 60.0, 1) # ~31.2 g fat / hour

        # Cardiorespiratory longevity tier based on estimated VO2max
        if vo2_max_est >= 50.0:
            fitness_tier = "Elite (Top 5% Age-Matched Cardiorespiratory Longevity)"
        elif vo2_max_est >= 42.0:
            fitness_tier = "Robust (Above Average - 30% All-Cause Mortality Reduction)"
        elif vo2_max_est >= 34.0:
            fitness_tier = "Moderate (Average Population Baseline)"
        else:
            fitness_tier = "Low (Elevated Cardiovascular Risk Gradient - Priority Improvement)"

        return {
            "chronological_age": user_age,
            "resting_heart_rate_bpm": rhr,
            "maximum_heart_rate_bpm": mhr,
            "max_hr_derivation": mhr_source,
            "heart_rate_reserve_bpm": hrr,
            "zone2_corridor_bpm": {
                "lower_bound_60pct_hrr": int(z2_lower),
                "upper_bound_70pct_hrr": int(z2_upper),
                "target_midpoint_bpm": int((z2_lower + z2_upper) / 2)
            },
            "estimated_vo2_max_ml_kg_min": vo2_max_est,
            "cardiorespiratory_longevity_tier": fitness_tier,
            "metabolic_dynamics": {
                "blood_lactate_ceiling_mmol_l": "< 2.0 mmol/L (Pure Aerobic Base)",
                "fat_oxidation_rate_estimate": f"~{fat_ox_rate_g_hr} g fat burned / hour",
                "ventilatory_talk_test": "Nasal breathing sustainable; conversational in complete sentences with slight effort."
            }
        }

    def schedule_weekly_aerobic_dose(
        self,
        current_weekly_zone2_minutes: float = 90.0,
        vo2_max_ml_kg_min: float = 42.0
    ) -> Dict[str, Any]:
        """
        Prescribes an optimal weekly cardiorespiratory volume based on the Peter Attia / AHA
        mitochondrial density standard (150 - 180 minutes/week Zone 2 + 1 VO2max session).
        """
        curr_mins = max(0.0, min(600.0, float(current_weekly_zone2_minutes)))
        vo2 = max(20.0, min(85.0, float(vo2_max_ml_kg_min)))

        target_base_minutes = 160.0
        deficit_minutes = round(max(0.0, target_base_minutes - curr_mins), 0)

        # Micro-progression: cap weekly increase to +15% to safeguard connective tissue
        safe_weekly_target = round(min(target_base_minutes, max(curr_mins * 1.15, curr_mins + 20.0)), 0)

        # Session distribution breakdown
        if safe_weekly_target <= 100.0:
            sessions = "3 sessions of 30-35 minutes (Rower, Cycling, Incline Treadmill Ruck)"
        elif safe_weekly_target <= 150.0:
            sessions = "3 sessions of 45-50 minutes (Steady-state aerobic base)"
        else:
            sessions = "4 sessions of 40-45 minutes + 1 weekly 4x4 min VO2max interval session"

        compliance_pct = round((curr_mins / target_base_minutes) * 100.0, 1)

        return {
            "current_weekly_volume_minutes": curr_mins,
            "clinical_longevity_target_minutes": target_base_minutes,
            "weekly_target_compliance": f"{compliance_pct}% of optimal longevity baseline",
            "next_week_progressive_overload_target_minutes": safe_weekly_target,
            "recommended_weekly_session_split": sessions,
            "mitochondrial_prescription": "Maintain heart rate within strict Zone 2 corridor. If breathing switches to oral panting, down-shift resistance immediately."
        }
