import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load the entire dataset (the book of examples)
data = pd.read_csv("symptom_data.csv")  # Load all rows, not just the first 15
X = data["symptoms"]  # The symptoms column
y = data["diagnosis"]  # The diagnosis column

# Create a machine learning model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X, y)  # Teach the model using the full dataset

def suggest_treatment(symptoms):
    if not symptoms:
        return {"diagnosis": "Unknown", "treatment": "Please provide symptoms"}
    
    # Use the model to guess the sickness
    diagnosis = model.predict([symptoms])[0]

    # Suggest a treatment based on the diagnosis
    treatments = {
        "Pneumonia": "Antibiotics, oxygen therapy",
        "Flu": "Rest, hydration, pain relievers",
        "Strep Throat": "Antibiotics, throat lozenges",
        "Heart Issue": "Seek emergency medical attention immediately",
        "Stomach Issue": "Rest, avoid heavy food, consult a doctor",
        "Dehydration": "Drink water, sit down, consult a doctor",
        "Food Poisoning": "Stay hydrated, rest, consult a doctor",
        "Diarrhea": "Drink oral rehydration solution, rest, consult a doctor",
        "Viral Infection": "Stay hydrated, rest, antiviral medication if prescribed",
        "Allergic Reaction": "Take antihistamines, consult a doctor",
        "Measles": "Rest, stay hydrated, consult a doctor immediately",
        "Dengue": "Rest, stay hydrated, consult a doctor immediately",
        "Anemia": "Eat iron-rich foods, consult a doctor for supplements",
        "Cold": "Rest, stay hydrated, take over-the-counter cold medicine",
        "Migraine": "Rest in a dark room, take pain relievers, consult a doctor",
        "Ear Infection": "Antibiotics if prescribed, consult a doctor",
        "Tonsillitis": "Antibiotics if bacterial, rest, consult a doctor",
        "Malaria": "Antimalarial medication, consult a doctor immediately",
        "Depression": "Talk to a trusted person, consult a doctor or therapist",
        "Gastroenteritis": "Stay hydrated, rest, consult a doctor",
        "Chickenpox": "Rest, avoid scratching, consult a doctor",
        "Low Blood Pressure": "Drink water, eat small meals, consult a doctor",
        "Skin Infection": "Keep the area clean, use antibiotic cream, consult a doctor",
        "Allergies": "Avoid allergens, take antihistamines, consult a doctor",
        "Acid Reflux": "Avoid spicy foods, eat smaller meals, consult a doctor"
    }
    
    treatment = treatments.get(diagnosis, "Consult a doctor")
    return {"diagnosis": diagnosis, "treatment": treatment}