# Disease Information & Assistance Service
# This module provides medical guidance based on predicted skin disease

DISEASE_INFO = {
    "Atopic_Dermatitis": {
        "description": "Atopic dermatitis is a chronic inflammatory skin condition characterized by itchy and inflamed skin.",
        "symptoms": [
            "Dry skin",
            "Severe itching",
            "Red or brownish patches",
            "Sensitive skin"
        ],
        "care_tips": [
            "Use fragrance-free moisturizers",
            "Avoid harsh soaps and detergents",
            "Keep skin hydrated",
            "Avoid scratching affected areas"
        ],
        "consult_doctor_if": [
            "Symptoms worsen",
            "Skin becomes infected",
            "Sleep is disturbed due to itching"
        ]
    },

    "Basal_Cell_Carcinoma": {
        "description": "Basal cell carcinoma is a type of skin cancer that develops due to prolonged exposure to ultraviolet radiation.",
        "symptoms": [
            "Pearly or waxy bump",
            "Flat, flesh-colored lesion",
            "Bleeding or scabbing sore"
        ],
        "care_tips": [
            "Avoid sun exposure",
            "Use broad-spectrum sunscreen",
            "Do not ignore persistent skin lesions"
        ],
        "consult_doctor_if": [
            "Lesion grows rapidly",
            "Bleeding does not stop",
            "Pain or discomfort occurs"
        ]
    },

    "Benign_Keratosis": {
        "description": "Benign keratosis is a non-cancerous skin growth commonly seen in older adults.",
        "symptoms": [
            "Waxy or scaly raised skin",
            "Brown, black, or light tan color",
            "Mild itching"
        ],
        "care_tips": [
            "Keep skin clean and moisturized",
            "Avoid scratching",
            "Monitor changes in appearance"
        ],
        "consult_doctor_if": [
            "Rapid growth",
            "Bleeding",
            "Sudden color changes"
        ]
    },

    "Eczema": {
        "description": "Eczema is a condition that causes the skin to become itchy, red, dry, and cracked.",
        "symptoms": [
            "Dry and itchy skin",
            "Red rashes",
            "Skin inflammation"
        ],
        "care_tips": [
            "Apply moisturizing creams regularly",
            "Avoid allergens",
            "Use mild soaps"
        ],
        "consult_doctor_if": [
            "Severe itching",
            "Skin infection",
            "Persistent symptoms"
        ]
    },

    "Fungal_Infection": {
        "description": "Fungal infections occur when fungi infect the skin, leading to irritation and discomfort.",
        "symptoms": [
            "Itchy rash",
            "Redness",
            "Peeling or cracking skin"
        ],
        "care_tips": [
            "Keep affected area dry",
            "Avoid sharing personal items",
            "Maintain proper hygiene"
        ],
        "consult_doctor_if": [
            "Infection spreads",
            "No improvement with care",
            "Pain increases"
        ]
    },

    "Melanocytic_Nevi": {
        "description": "Melanocytic nevi are common skin moles formed by clusters of pigmented cells.",
        "symptoms": [
            "Small dark spots",
            "Uniform color",
            "Smooth borders"
        ],
        "care_tips": [
            "Monitor changes in size or color",
            "Avoid excessive sun exposure"
        ],
        "consult_doctor_if": [
            "Change in shape or size",
            "Bleeding or itching",
            "Irregular borders appear"
        ]
    },

    "Melanoma": {
        "description": "Melanoma is a serious form of skin cancer that develops from pigment-producing cells.",
        "symptoms": [
            "Asymmetrical mole",
            "Irregular borders",
            "Multiple colors in lesion"
        ],
        "care_tips": [
            "Avoid sun exposure",
            "Regular skin self-examination",
            "Use sunscreen"
        ],
        "consult_doctor_if": [
            "Rapid changes in mole",
            "Bleeding",
            "Pain or swelling"
        ]
    },

    "Psoriasis": {
        "description": "Psoriasis is a chronic autoimmune condition causing rapid skin cell buildup.",
        "symptoms": [
            "Red patches with silvery scales",
            "Dry cracked skin",
            "Itching or burning"
        ],
        "care_tips": [
            "Keep skin moisturized",
            "Avoid stress",
            "Follow a healthy lifestyle"
        ],
        "consult_doctor_if": [
            "Joint pain",
            "Severe flare-ups",
            "Difficulty performing daily tasks"
        ]
    },

    "Seborrheic_Keratosis": {
        "description": "Seborrheic keratosis is a common non-cancerous skin growth.",
        "symptoms": [
            "Waxy growths",
            "Brown or black lesions",
            "Rough texture"
        ],
        "care_tips": [
            "Avoid scratching",
            "Maintain skin hygiene"
        ],
        "consult_doctor_if": [
            "Sudden growth",
            "Bleeding",
            "Pain develops"
        ]
    },

    "Viral_Infection": {
        "description": "Viral skin infections are caused by viruses affecting the skin layers.",
        "symptoms": [
            "Blisters",
            "Rashes",
            "Red or swollen skin"
        ],
        "care_tips": [
            "Avoid touching infected area",
            "Maintain cleanliness",
            "Avoid close contact with others"
        ],
        "consult_doctor_if": [
            "Fever develops",
            "Infection spreads",
            "Pain increases"
        ]
    }
}


def get_disease_info(disease_name): 
    """
    Fetch disease information based on predicted disease name. 
    """
    return DISEASE_INFO.get(
        disease_name,
        {
            "description": "No information available.",
            "symptoms": [],
            "care_tips": [],
            "consult_doctor_if": []
        }
    )