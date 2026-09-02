import urllib.request
import urllib.error
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://127.0.0.1:5000"

def post_json(path, data):
    req = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode('utf-8')
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        print("POST HTTP Error:", e.code, e.read().decode('utf-8'))
        raise e

def get_json(path):
    try:
        with urllib.request.urlopen(f"{BASE_URL}{path}") as resp:
            raw = resp.read().decode('utf-8')
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        print("GET HTTP Error:", e.code, e.read().decode('utf-8'))
        raise e

def run_tests():
    print("--- TESTING ALL DYSLEXIA ROUTES FOR BHOJPURI (BHO) ---")
    
    # 1. Questionnaire Content
    q_content = get_json("/api/dyslexia/content/questionnaire?lang=bho")
    q_len = len(q_content.get('questions', q_content.get('content', {}).get('questions', [])))
    print("[1] Questionnaire content (BHO):", q_len, "questions")
    assert q_len == 8, f"Expected 8 questions, got {q_len}"

    # 2. Questionnaire Analyze
    q_res = post_json("/api/dyslexia/analyze/questionnaire", {
        "answers": {"q1": 0, "q2": 1, "q3": 0, "q4": 0, "q5": 0, "q6": 0, "q7": 0, "q8": 0},
        "lang": "bho"
    })
    print("[2] Questionnaire analyze:", q_res)
    assert "score" in q_res, "Score missing from questionnaire response"

    # 3. RAN Content
    ran_content = get_json("/api/dyslexia/content/ran_items?lang=bho")
    ran_grids = len(ran_content.get('grids', ran_content.get('content', {}).get('grids', [])))
    print("[3] RAN content (BHO):", ran_grids, "grids")
    assert ran_grids == 4, f"Expected 4 grids, got {ran_grids}"

    # 4. RAN Analyze
    ran_res = post_json("/api/dyslexia/analyze/ran", {
        "grid_times": [12.0, 11.5, 13.0, 14.0],
        "grid_errors": [0, 0, 0, 0],
        "total_items": 40,
        "recognized_count": 40,
        "lang": "bho"
    })
    print("[4] RAN analyze score:", ran_res)
    assert "score" in ran_res, "Score missing from RAN response"

    # 5. Phonological Content
    p_content = get_json("/api/dyslexia/content/phonological_tasks?lang=bho")
    p_tasks = len(p_content.get('tasks', p_content.get('content', {}).get('tasks', [])))
    print("[5] Phonological content (BHO):", p_tasks, "tasks")
    assert p_tasks == 8, f"Expected 8 tasks, got {p_tasks}"

    # 6. Phonological Analyze
    p_res = post_json("/api/dyslexia/analyze/phonological", {
        "task_results": [{"id": "p1", "correct": True, "time_sec": 2.1}],
        "lang": "bho"
    })
    print("[6] Phonological analyze score:", p_res)
    assert "score" in p_res, "Score missing from phonological response"

    # 7. Nonwords Content
    nw_content = get_json("/api/dyslexia/content/nonwords?lang=bho")
    nw_items = len(nw_content.get('items', nw_content.get('content', {}).get('items', [])))
    print("[7] Nonwords content (BHO):", nw_items, "items")
    assert nw_items == 8, f"Expected 8 items, got {nw_items}"

    # 8. Decoding Analyze
    d_res = post_json("/api/dyslexia/analyze/decoding", {
        "decoding_items": [{"target": "वूग", "spoken": "वूग"}],
        "lang": "bho"
    })
    print("[8] Decoding analyze score:", d_res)
    assert "score" in d_res, "Score missing from decoding response"

    # 9. Oral Spelling Analyze
    os_res = post_json("/api/dyslexia/analyze/oral_spelling", {
        "reading_time_sec": 20.0,
        "words_correct": 30,
        "spelling_attempts": [{"target": "बिलाई", "spelling": "बिलाई"}],
        "lang": "bho"
    })
    print("[9] Oral Spelling analyze score:", os_res)
    assert "score" in os_res, "Score missing from oral spelling response"

    # 10. Calculate Risk
    risk_res = post_json("/api/dyslexia/calculate_risk", {
        "age": 8,
        "gender": "male",
        "background_score": 6.25,
        "ran_score": 0.0,
        "phonological_score": 0.0,
        "decoding_score": 0.0,
        "oral_reading_score": 0.0
    })
    print("[10] Calculate overall risk:", risk_res)
    assert "composite_score" in risk_res, "composite_score missing from risk response"

    print("\n>>> ALL BHOJPURI DYSLEXIA TESTS PASSED PERFECTLY! <<<")

if __name__ == "__main__":
    run_tests()
