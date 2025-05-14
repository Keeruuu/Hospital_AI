from transformers import pipeline

# Load a pre-trained model for text classification
# We're using a simple model for demo purposes
classifier = pipeline("sentiment-analysis")  # Placeholder model

# Simulated treatment mapping (since we don't have a real medical model yet)
treatment_map = {
    "fever, cough, shortness of breath": {
        "diagnosis": "Possible Pneumonia",
        "treatment": "Antibiotics, oxygen therapy"
    },
    "headache, nausea, dizziness": {
        "diagnosis": "Possible Migraine",
        "treatment": "Pain relievers, rest"
    }
}

def suggest_treatment(symptoms):
    symptoms_list = symptoms.lower().split(", ")
    if "fever" in symptoms_list and "cough" in symptoms_list:
        return {"diagnosis": "Possible Pneumonia", "treatment": "Antibiotics, oxygen therapy"}
    elif "headache" in symptoms_list and "fever" in symptoms_list:
        return {"diagnosis": "Possible Migraine or Flu", "treatment": "Rest, hydration, pain relievers"}
    elif "sore throat" in symptoms_list and "cough" in symptoms_list:
        return {"diagnosis": "Possible Strep Throat", "treatment": "Antibiotics, throat lozenges"}
    else:
        return {"diagnosis": "Unknown", "treatment": "Consult a doctor"}
    return result

# Test the function
symptoms = "fever, cough, shortness of breath"
result = suggest_treatment(symptoms)
print(result)