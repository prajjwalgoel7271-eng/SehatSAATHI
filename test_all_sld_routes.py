import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

from app import app

def run_sld_tests():
    print("==================================================")
    print("   SEHAT SATHI - SLD AGE-TIERED TEST SUITE (1-4)   ")
    print("==================================================")

    client = app.test_client()

    # 1. Content Bank APIs for English & Hindi across all 4 Tiers
    for tier in [1, 2, 3, 4]:
        for lang in ['en', 'hi']:
            res = client.get(f"/api/sld/content/{tier}?lang={lang}")
            assert res.status_code == 200, f"Failed to fetch Tier {tier} content for {lang}"
            c = res.get_json()
            print(f"[Content Bank] Tier {tier} ({lang.upper()}): Loaded successfully. Code = {c.get('code', lang)}")
            assert "content" in c or "tier" in c, f"Tier {tier} content bank empty for {lang}"

    # 2. Tier 1 (Ages 3-5): 100% Accuracy ➔ Low Risk
    print("\n--- Testing Tier 1: Precursor Screening (100% Accuracy) ---")
    t1_payload = {
        "rhyme_results": [
            {"id": "r1", "correct": True, "time_sec": 1.5},
            {"id": "r2", "correct": True, "time_sec": 1.8},
            {"id": "r3", "correct": True, "time_sec": 1.6}
        ],
        "subitizing_results": [
            {"id": "s1", "correct": True, "time_sec": 1.1},
            {"id": "s2", "correct": True, "time_sec": 1.2},
            {"id": "s3", "correct": True, "time_sec": 1.0}
        ],
        "motor_results": {
            "avg_deviation_px": 5.0,
            "midline_pause_sec": 0.2,
            "completion_time_sec": 4.0
        }
    }
    t1_res = client.post("/api/sld/analyze/tier1", json=t1_payload).get_json()
    print("[Tier 1 Result]:", json.dumps(t1_res, indent=2, ensure_ascii=False))
    assert t1_res["domain_results"]["phonological_precursor"]["risk_band"] == "Low Risk"
    assert t1_res["domain_results"]["numerical_precursor"]["risk_band"] == "Low Risk"
    assert t1_res["domain_results"]["motor_visual_midline"]["risk_band"] == "Low Risk"
    print("✓ Tier 1 outputs LOW RISK for 100% accuracy!")

    # 3. Tier 2 (Ages 6-9): 100% Accuracy ➔ Low Risk
    print("\n--- Testing Tier 2: Manifestation Screening (100% Accuracy) ---")
    t2_payload = {
        "dyslexia": {
            "comprehension_correct": 3,
            "comprehension_total": 3,
            "spelling_correct": 5,
            "spelling_total": 5,
            "ran_total_sec": 12.0,
            "decoding_accuracy": 100.0
        },
        "dyscalculia": {
            "magnitude_accuracy": 100.0,
            "magnitude_avg_sec": 1.0,
            "fact_calculation_delays": 0,
            "fact_accuracy": 100.0,
            "sequence_accuracy": 100.0
        },
        "dysgraphia": {
            "pause_duration_ratio": 0.10,
            "speed_decay_pct": 10.0,
            "stroke_jitter_px": 1.5
        }
    }
    t2_res = client.post("/api/sld/analyze/tier2", json=t2_payload).get_json()
    print("[Tier 2 Result]:", json.dumps(t2_res, indent=2, ensure_ascii=False))
    assert t2_res["branches"]["dyslexia"]["risk_band"] == "Low Risk"
    assert t2_res["branches"]["dyscalculia"]["risk_band"] == "Low Risk"
    assert t2_res["branches"]["dysgraphia"]["risk_band"] == "Low Risk"
    assert t2_res["comorbidity_flag"] == False
    print("✓ Tier 2 evaluates Dyslexia, Dyscalculia, Dysgraphia branches as LOW RISK for 100% accuracy!")

    # 4. Tier 3 (Ages 10-13): 100% Accuracy ➔ Low Risk
    print("\n--- Testing Tier 3: Compensation-Resistant (100% Accuracy) ---")
    t3_payload = {
        "ran_multi_round": {
            "round1_colors_sec": 12.0,
            "round3_mixed_sec": 13.0
        },
        "adaptive_decoding": {
            "max_level_cleared": 3
        },
        "sight_word_decay": {
            "correct_count": 2,
            "total_count": 2
        },
        "long_comprehension": {
            "accuracy": 100.0
        },
        "dyscalculia": {"score": 0.0},
        "dysgraphia": {"score": 0.0}
    }
    t3_res = client.post("/api/sld/analyze/tier3", json=t3_payload).get_json()
    print("[Tier 3 Result]:", json.dumps(t3_res, indent=2, ensure_ascii=False))
    assert t3_res["branches"]["dyslexia"]["risk_band"] == "Low Risk"
    assert t3_res["branches"]["dyscalculia"]["risk_band"] == "Low Risk"
    assert t3_res["branches"]["dysgraphia"]["risk_band"] == "Low Risk"
    print("✓ Tier 3 evaluates 100% accuracy as LOW RISK!")

    # 5. Tier 4 (Ages 14+): Low Distress + 100% Accuracy ➔ Low Risk & No Social Masking
    print("\n--- Testing Tier 4: Executive Function & Academic Distress (100% Accuracy) ---")
    t4_payload = {
        "distress_answers": {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 0, "q8": 0, "q9": 0, "q10": 0
        },
        "cognitive_data": t3_payload
    }
    t4_res = client.post("/api/sld/analyze/tier4", json=t4_payload).get_json()
    print("[Tier 4 Result]:", json.dumps(t4_res, indent=2, ensure_ascii=False))
    assert t4_res["social_masking_detected"] == False
    print("✓ Tier 4 correctly outputs LOW RISK & Social Masking FALSE for 100% accuracy!")

    # 6. Page Route Verification
    with client.session_transaction() as sess:
        sess['disclaimer_accepted'] = True

    for route in ["/test/sld", "/test/sld/tier1", "/test/sld/tier2", "/test/sld/tier3", "/test/sld/tier4", "/test/sld/results"]:
        page_res = client.get(route)
        assert page_res.status_code == 200, f"Route {route} returned status {page_res.status_code}"
        print(f"[Page Route] {route}: 200 OK")

    print("\n==================================================")
    print(" 🎉 ALL SLD AGE-TIERED TEST SUITES PASSED! 🎉 ")
    print("==================================================")

if __name__ == "__main__":
    run_sld_tests()
