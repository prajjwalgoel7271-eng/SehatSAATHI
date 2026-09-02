import os
import json

BASE_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

# ── 1. TIER 1 CONTENT (Ages 3-5: Precursor) ──
TIER1_EN = {
    "language": "English",
    "code": "en",
    "tier": 1,
    "rhyme_game": [
        {
            "id": "r1",
            "prompt_audio_text": "Which word rhymes with Cat?",
            "target_word": "Cat",
            "options": [
                {"id": "opt1", "word": "Hat", "emoji": "🎩", "correct": True},
                {"id": "opt2", "word": "Dog", "emoji": "🐶", "correct": False},
                {"id": "opt3", "word": "Sun", "emoji": "☀️", "correct": False}
            ]
        },
        {
            "id": "r2",
            "prompt_audio_text": "Which word rhymes with Star?",
            "target_word": "Star",
            "options": [
                {"id": "opt1", "word": "Car", "emoji": "🚗", "correct": True},
                {"id": "opt2", "word": "Pen", "emoji": "🖊️", "correct": False},
                {"id": "opt3", "word": "Fish", "emoji": "🐟", "correct": False}
            ]
        },
        {
            "id": "r3",
            "prompt_audio_text": "Which word rhymes with Tree?",
            "target_word": "Tree",
            "options": [
                {"id": "opt1", "word": "Bee", "emoji": "🐝", "correct": True},
                {"id": "opt2", "word": "Ball", "emoji": "⚽", "correct": False},
                {"id": "opt3", "word": "Cup", "emoji": "🥤", "correct": False}
            ]
        },
        {
            "id": "r4",
            "prompt_audio_text": "Which word begins with the sound /S/?",
            "target_word": "Sun",
            "options": [
                {"id": "opt1", "word": "Sun", "emoji": "☀️", "correct": True},
                {"id": "opt2", "word": "Moon", "emoji": "🌙", "correct": False},
                {"id": "opt3", "word": "Tree", "emoji": "🌳", "correct": False}
            ]
        }
    ],
    "subitizing_game": [
        {"id": "s1", "count": 2, "shape": "⭐", "display_ms": 700},
        {"id": "s2", "count": 4, "shape": "🍎", "display_ms": 700},
        {"id": "s3", "count": 1, "shape": "🐱", "display_ms": 700},
        {"id": "s4", "count": 3, "shape": "⚽", "display_ms": 700}
    ],
    "motor_midline": {
        "instruction": "Trace the glowing curved line from the left star to the right star across the center!",
        "target_points": [
            {"x": 10, "y": 50},
            {"x": 30, "y": 20},
            {"x": 50, "y": 50},
            {"x": 70, "y": 80},
            {"x": 90, "y": 50}
        ]
    }
}

TIER1_HI = {
    "language": "Hindi",
    "code": "hi",
    "tier": 1,
    "rhyme_game": [
        {
            "id": "r1",
            "prompt_audio_text": "कौन सा शब्द 'बिल्ली' से तुक मिलाता है?",
            "target_word": "बिल्ली",
            "options": [
                {"id": "opt1", "word": "दिल्ली", "emoji": "🏛️", "correct": True},
                {"id": "opt2", "word": "कुत्ता", "emoji": "🐶", "correct": False},
                {"id": "opt3", "word": "सूरज", "emoji": "☀️", "correct": False}
            ]
        },
        {
            "id": "r2",
            "prompt_audio_text": "कौन सा शब्द 'तारा' से तुक मिलाता है?",
            "target_word": "तारा",
            "options": [
                {"id": "opt1", "word": "कार", "emoji": "🚗", "correct": True},
                {"id": "opt2", "word": "पानी", "emoji": "💧", "correct": False},
                {"id": "opt3", "word": "मछली", "emoji": "🐟", "correct": False}
            ]
        },
        {
            "id": "r3",
            "prompt_audio_text": "कौन सा शब्द 'रात' से तुक मिलाता है?",
            "target_word": "रात",
            "options": [
                {"id": "opt1", "word": "बात", "emoji": "💬", "correct": True},
                {"id": "opt2", "word": "गेंद", "emoji": "⚽", "correct": False},
                {"id": "opt3", "word": "पेड़", "emoji": "🌳", "correct": False}
            ]
        },
        {
            "id": "r4",
            "prompt_audio_text": "कौन सा शब्द /स/ की ध्वनि से शुरू होता है?",
            "target_word": "सूरज",
            "options": [
                {"id": "opt1", "word": "सूरज", "emoji": "☀️", "correct": True},
                {"id": "opt2", "word": "चाँद", "emoji": "🌙", "correct": False},
                {"id": "opt3", "word": "पेड़", "emoji": "🌳", "correct": False}
            ]
        }
    ],
    "subitizing_game": TIER1_EN["subitizing_game"],
    "motor_midline": {
        "instruction": "बाएँ तारे से दाएँ तारे तक बीच की रेखा के ऊपर उंगली चलाएँ!",
        "target_points": TIER1_EN["motor_midline"]["target_points"]
    }
}

# ── 2. TIER 2 CONTENT (Ages 6-9: Manifestation) ──
TIER2_EN = {
    "language": "English",
    "code": "en",
    "tier": 2,
    "dyslexia": {
        "comprehension_passage": {
            "title": "The Brave Little Pup",
            "text": "Leo is a small brown puppy who lives in a quiet village. One afternoon, Leo found a lost kitten behind the old barn. He barked gently to guide the kitten back to its mother.",
            "questions": [
                {
                    "id": "q1",
                    "question": "What kind of animal is Leo?",
                    "options": ["A small brown puppy", "A little kitten", "A big horse"],
                    "correct": 0
                },
                {
                    "id": "q2",
                    "question": "Where did Leo find the kitten?",
                    "options": ["In a park", "Behind the old barn", "Inside the house"],
                    "correct": 1
                },
                {
                    "id": "q3",
                    "question": "How did Leo guide the kitten?",
                    "options": ["By running away", "By barking gently", "By climbing a tree"],
                    "correct": 1
                }
            ]
        },
        "spelling": [
            {"target": "plant", "type": "real"},
            {"target": "clock", "type": "real"},
            {"target": "bright", "type": "real"},
            {"target": "strop", "type": "pseudo"},
            {"target": "flim", "type": "pseudo"}
        ]
    },
    "dyscalculia": {
        "magnitude_comparison": [
            {"id": "m1", "num1": 8, "num2": 3, "correct_larger": 8},
            {"id": "m2", "num1": 14, "num2": 19, "correct_larger": 19},
            {"id": "m3", "num1": 25, "num2": 17, "correct_larger": 25},
            {"id": "m4", "num1": 6, "num2": 11, "correct_larger": 11},
            {"id": "m5", "num1": 32, "num2": 28, "correct_larger": 32}
        ],
        "fact_retrieval": [
            {"id": "f1", "expr": "2 + 3", "answer": 5, "instant_threshold_sec": 1.8},
            {"id": "f2", "expr": "5 + 5", "answer": 10, "instant_threshold_sec": 1.8},
            {"id": "f3", "expr": "9 - 4", "answer": 5, "instant_threshold_sec": 2.0},
            {"id": "f4", "expr": "4 + 4", "answer": 8, "instant_threshold_sec": 1.8},
            {"id": "f5", "expr": "10 - 3", "answer": 7, "instant_threshold_sec": 2.2}
        ],
        "number_sequence": [
            {"id": "seq1", "prompt": "2, 4, 6, _", "options": [7, 8, 9], "correct": 8},
            {"id": "seq2", "prompt": "5, 10, 15, _", "options": [20, 25, 30], "correct": 20},
            {"id": "seq3", "prompt": "10, 9, 8, _", "options": [6, 7, 5], "correct": 7},
            {"id": "seq4", "prompt": "3, 6, 9, _", "options": [10, 11, 12], "correct": 12}
        ]
    },
    "dysgraphia": {
        "dictated_sentences": [
            {"id": "ds1", "level": "simple", "text": "The sun is hot."},
            {"id": "ds2", "level": "complex", "text": "The quick brown fox jumps over the lazy dog."}
        ]
    }
}

TIER2_HI = {
    "language": "Hindi",
    "code": "hi",
    "tier": 2,
    "dyslexia": {
        "comprehension_passage": {
            "title": "छोटा बहादुर पिल्ला",
            "text": "लियो एक छोटा भूरा पिल्ला है जो एक शांत गाँव में रहता है। एक दोपहर, लियो को पुराने खलिहान के पीछे एक खोया हुआ बिल्ली का बच्चा मिला। उसने बिल्ली के बच्चे को उसकी माँ के पास पहुँचाने के लिए धीरे से भौंका।",
            "questions": [
                {
                    "id": "q1",
                    "question": "लियो किस प्रकार का जानवर है?",
                    "options": ["एक छोटा भूरा पिल्ला", "एक छोटी बिल्ली", "एक बड़ा घोड़ा"],
                    "correct": 0
                },
                {
                    "id": "q2",
                    "question": "लियो को बिल्ली का बच्चा कहाँ मिला?",
                    "options": ["एक पार्क में", "पुराने खलिहान के पीछे", "घर के अंदर"],
                    "correct": 1
                },
                {
                    "id": "q3",
                    "question": "लियो ने बिल्ली के बच्चे की मदद कैसे की?",
                    "options": ["भागकर", "धीरे से भौंककर", "पेड़ पर चढ़कर"],
                    "correct": 1
                }
            ]
        },
        "spelling": [
            {"target": "पौधा", "type": "real"},
            {"target": "घड़ी", "type": "real"},
            {"target": "सूरज", "type": "real"},
            {"target": "स्ट्रॉप", "type": "pseudo"},
            {"target": "फ्लिम", "type": "pseudo"}
        ]
    },
    "dyscalculia": TIER2_EN["dyscalculia"],
    "dysgraphia": {
        "dictated_sentences": [
            {"id": "ds1", "level": "simple", "text": "सूरज बहुत गर्म है।"},
            {"id": "ds2", "level": "complex", "text": "तेज़ भूरी लोमड़ी आलसी कुत्ते के ऊपर से कूदती है।"}
        ]
    }
}

# ── 3. TIER 3 CONTENT (Ages 10-13: Compensation-Resistant) ──
TIER3_EN = {
    "language": "English",
    "code": "en",
    "tier": 3,
    "multi_round_ran": {
        "round1_colors": ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"],
        "round2_letters": ["A", "B", "D", "O", "P", "S", "T", "Z"],
        "round3_mixed": ["Red", "A", "5", "Blue", "D", "9", "Green", "K"]
    },
    "adaptive_nonwords": [
        {"id": "nw1", "level": 1, "complexity": "2-letter", "nonword": "og", "phonemes": "o-g"},
        {"id": "nw2", "level": 1, "complexity": "2-letter", "nonword": "ib", "phonemes": "i-b"},
        {"id": "nw3", "level": 2, "complexity": "blends", "nonword": "strop", "phonemes": "s-t-r-o-p"},
        {"id": "nw4", "level": 2, "complexity": "blends", "nonword": "flint", "phonemes": "f-l-i-n-t"},
        {"id": "nw5", "level": 3, "complexity": "multisyllabic", "nonword": "flimberate", "phonemes": "flim-ber-ate"},
        {"id": "nw6", "level": 3, "complexity": "multisyllabic", "nonword": "sprottle", "phonemes": "sprot-tle"}
    ],
    "sight_word_decay": [
        {
            "id": "swd1",
            "target": "caught",
            "brief_display_ms": 1200,
            "distractor_task": "Count backwards from 20 to 15",
            "delayed_choices": [
                {"text": "cought", "is_target": False},
                {"text": "caught", "is_target": True},
                {"text": "chaught", "is_target": False},
                {"text": "coght", "is_target": False}
            ]
        },
        {
            "id": "swd2",
            "target": "enough",
            "brief_display_ms": 1200,
            "distractor_task": "Tap the odd number: 4, 8, 7, 2",
            "delayed_choices": [
                {"text": "enuff", "is_target": False},
                {"text": "anough", "is_target": False},
                {"text": "enough", "is_target": True},
                {"text": "enougth", "is_target": False}
            ]
        }
    ],
    "long_comprehension_passage": {
        "title": "Ecosystem Dynamics & Adaptation",
        "text": "Forest ecosystems rely on intricate food webs where every organism plays a vital role. Plants convert sunlight into organic nutrients through photosynthesis. Primary consumers feed on plants, while apex predators control herbivore populations, preventing overgrazing and soil erosion.",
        "questions": [
            {
                "id": "lq1",
                "question": "What is the primary role of apex predators mentioned in the text?",
                "options": ["Convert sunlight into energy", "Control herbivore populations to prevent erosion", "Produce organic nutrients"],
                "correct": 1
            },
            {
                "id": "lq2",
                "question": "Which process allows plants to create nutrients?",
                "options": ["Photosynthesis", "Herbivory", "Erosion"],
                "correct": 0
            },
            {
                "id": "lq3",
                "question": "What would happen if apex predators disappeared?",
                "options": ["Plants would grow faster", "Overgrazing and soil erosion would increase", "Sunlight would decrease"],
                "correct": 1
            }
        ]
    }
}

TIER3_HI = {
    "language": "Hindi",
    "code": "hi",
    "tier": 3,
    "multi_round_ran": {
        "round1_colors": ["लाल", "नीला", "हरा", "पीला", "बैंगनी", "नारंगी"],
        "round2_letters": ["अ", "क", "म", "च", "प", "र", "स", "त"],
        "round3_mixed": ["लाल", "क", "५", "नीला", "म", "९", "हरा", "त"]
    },
    "adaptive_nonwords": [
        {"id": "nw1", "level": 1, "complexity": "2-letter", "nonword": "वूग", "phonemes": "wug"},
        {"id": "nw2", "level": 1, "complexity": "2-letter", "nonword": "बिफ", "phonemes": "bif"},
        {"id": "nw3", "level": 2, "complexity": "blends", "nonword": "स्ट्रॉप", "phonemes": "strop"},
        {"id": "nw4", "level": 2, "complexity": "blends", "nonword": "प्लिंक", "phonemes": "plink"},
        {"id": "nw5", "level": 3, "complexity": "multisyllabic", "nonword": "फ्लिम्बर", "phonemes": "flimber"},
        {"id": "nw6", "level": 3, "complexity": "multisyllabic", "nonword": "स्प्रोटल", "phonemes": "sprottle"}
    ],
    "sight_word_decay": [
        {
            "id": "swd1",
            "target": "क्योंकि",
            "brief_display_ms": 1200,
            "distractor_task": "20 से 15 तक उल्टी गिनती करें",
            "delayed_choices": [
                {"text": "क्योकि", "is_target": False},
                {"text": "क्योंकि", "is_target": True},
                {"text": "कयोंकि", "is_target": False},
                {"text": "क्यौकि", "is_target": False}
            ]
        },
        {
            "id": "swd2",
            "target": "विज्ञान",
            "brief_display_ms": 1200,
            "distractor_task": "विषम संख्या चुनें: 4, 8, 7, 2",
            "delayed_choices": [
                {"text": "विग्यान", "is_target": False},
                {"text": "विज्ञान", "is_target": True},
                {"text": "विज्यान", "is_target": False},
                {"text": "विजञान", "is_target": False}
            ]
        }
    ],
    "long_comprehension_passage": {
        "title": "पारिस्थितिकी तंत्र और संतुलन",
        "text": "जंगल का पारिस्थितिकी तंत्र एक जटिल खाद्य जाल पर निर्भर करता है जहाँ प्रत्येक जीव एक महत्वपूर्ण भूमिका निभाता है। पौधे प्रकाश संश्लेषण के माध्यम से सूर्य के प्रकाश को ऊर्जा में बदलते हैं। प्राथमिक उपभोक्ता पौधों को खाते हैं, जबकि शीर्ष शिकारी शाकाहारी जीवों की आबादी को नियंत्रित करते हैं ताकि अत्यधिक चरने और मिट्टी के कटाव को रोका जा सके।",
        "questions": [
            {
                "id": "lq1",
                "question": "गद्यांश के अनुसार शीर्ष शिकारियों की क्या भूमिका है?",
                "options": ["सूर्य के प्रकाश को ऊर्जा में बदलना", "शाकाहारियों को नियंत्रित कर मिट्टी के कटाव को रोकना", "पौधों का निर्माण करना"],
                "correct": 1
            },
            {
                "id": "lq2",
                "question": "पौधे किस प्रक्रिया द्वारा पोषक तत्व बनाते हैं?",
                "options": ["प्रकाश संश्लेषण", "मृदा अपरदन", "वाष्पोत्सर्जन"],
                "correct": 0
            },
            {
                "id": "lq3",
                "question": "यदि शीर्ष शिकारी समाप्त हो जाएं तो क्या होगा?",
                "options": ["पौधे तेज़ी से बढ़ेंगे", "अत्यधिक चरने से मिट्टी का कटाव बढ़ेगा", "धूप कम हो जाएगी"],
                "correct": 1
            }
        ]
    }
}

# ── 4. TIER 4 CONTENT (Ages 14+: Executive Function & Academic Distress) ──
TIER4_EN = {
    "language": "English",
    "code": "en",
    "tier": 4,
    "academic_distress_questionnaire": [
        {"id": "q1", "text": "I feel anxious or uneasy when asked to read aloud in class or group settings.", "domain": "reading_anxiety"},
        {"id": "q2", "text": "I avoid tasks that involve long reading assignments or complex documents.", "domain": "reading_avoidance"},
        {"id": "q3", "text": "I experience significant frustration when attempting timed math calculations.", "domain": "math_frustration"},
        {"id": "q4", "text": "I feel my handwriting or writing speed holds me back despite knowing the answers.", "domain": "writing_distress"},
        {"id": "q5", "text": "I spend double or triple the expected time completing reading or writing homework.", "domain": "effort_burden"},
        {"id": "q6", "text": "I lose my line frequently or reread sentences multiple times to understand them.", "domain": "reading_mechanics"},
        {"id": "q7", "text": "I feel mental fatigue or headache quickly when working with numbers or tables.", "domain": "math_fatigue"},
        {"id": "q8", "text": "I try to hide my reading/writing difficulties from peers or teachers.", "domain": "social_masking"},
        {"id": "q9", "text": "I worry that my academic speed does not reflect my true intelligence.", "domain": "discrepancy_distress"},
        {"id": "q10", "text": "I avoid choosing courses or careers that require extensive reading or writing.", "domain": "academic_avoidance"}
    ],
    "options": [
        {"text": "Never", "score": 0},
        {"text": "Sometimes", "score": 1},
        {"text": "Often / Constantly", "score": 2}
    ],
    "advanced_cognitive": TIER3_EN
}

TIER4_HI = {
    "language": "Hindi",
    "code": "hi",
    "tier": 4,
    "academic_distress_questionnaire": [
        {"id": "q1", "text": "कक्षा या समूह में जोर से पढ़ने के लिए कहे जाने पर मुझे घबराहट महसूस होती है।", "domain": "reading_anxiety"},
        {"id": "q2", "text": "मैं ऐसे कार्यों से बचता हूँ जिनमें लंबे समय तक पढ़ने या जटिल दस्तावेज़ शामिल हों।", "domain": "reading_avoidance"},
        {"id": "q3", "text": "समयबद्ध गणितीय गणनाएँ करते समय मुझे बहुत हताशा होती है।", "domain": "math_frustration"},
        {"id": "q4", "text": "उत्तर जानने के बावजूद मुझे लगता है कि मेरी लिखावट या लिखने की गति मुझे पीछे रखती है।", "domain": "writing_distress"},
        {"id": "q5", "text": "होमवर्क पूरा करने में मुझे अपेक्षित समय से दो से तीन गुना अधिक समय लगता है।", "domain": "effort_burden"},
        {"id": "q6", "text": "पढ़ते समय मैं अक्सर पंक्ति भूल जाता हूँ या समझने के लिए वाक्यों को बार-बार पढ़ता हूँ।", "domain": "reading_mechanics"},
        {"id": "q7", "text": "संख्याओं या तालिकाओं के साथ काम करते समय मुझे जल्दी मानसिक थकान होती है।", "domain": "math_fatigue"},
        {"id": "q8", "text": "मैं अपनी पढ़ने/लिखने की कठिनाइयों को दोस्तों या शिक्षकों से छिपाने की कोशिश करता हूँ।", "domain": "social_masking"},
        {"id": "q9", "text": "मुझे चिंता होती है कि मेरी पढ़ाई की गति मेरी वास्तविक बुद्धिमत्ता को नहीं दर्शाती।", "domain": "discrepancy_distress"},
        {"id": "q10", "text": "मैं ऐसे विषयों या करियर का चयन करने से बचता हूँ जिनमें अधिक पढ़ना या लिखना पड़ता है।", "domain": "academic_avoidance"}
    ],
    "options": [
        {"text": "कभी नहीं", "score": 0},
        {"text": "कभी-कभी", "score": 1},
        {"text": "अक्सर / लगातार", "score": 2}
    ],
    "advanced_cognitive": TIER3_HI
}


def build():
    lang_map = {
        "en": (TIER1_EN, TIER2_EN, TIER3_EN, TIER4_EN),
        "hi": (TIER1_HI, TIER2_HI, TIER3_HI, TIER4_HI)
    }

    for lang_code, (t1, t2, t3, t4) in lang_map.items():
        out_dir = os.path.join(CONTENT_DIR, lang_code)
        os.makedirs(out_dir, exist_ok=True)

        with open(os.path.join(out_dir, 'sld_tier1.json'), 'w', encoding='utf-8') as f:
            json.dump(t1, f, ensure_ascii=False, indent=2)

        with open(os.path.join(out_dir, 'sld_tier2.json'), 'w', encoding='utf-8') as f:
            json.dump(t2, f, ensure_ascii=False, indent=2)

        with open(os.path.join(out_dir, 'sld_tier3.json'), 'w', encoding='utf-8') as f:
            json.dump(t3, f, ensure_ascii=False, indent=2)

        with open(os.path.join(out_dir, 'sld_tier4.json'), 'w', encoding='utf-8') as f:
            json.dump(t4, f, ensure_ascii=False, indent=2)

        print(f"[OK] Created SLD Tier 1-4 JSON files for {lang_code}")

if __name__ == "__main__":
    build()
