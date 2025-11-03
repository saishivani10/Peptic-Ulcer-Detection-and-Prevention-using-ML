import numpy as np
import pandas as pd
# data visualization (kept as optional imports)
import matplotlib.pyplot as plt
import seaborn as sns
# machine learning
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import os

# Module-level model placeholders (built lazily)
_MODEL_TREE = None
_MODEL_FOREST = None
_MODEL_GNB = None
_SYMPTOMS = None
_DISEASE = None

symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions','continuous_sneezing', 'shivering',
'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain'
,'constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples',
            'blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease = ['Fungalinfection','Allergy','GERD','Chroniccholestasis','DrugReaction','Pepticulcerdiseae','AIDS','Diabetes','Gastroenteritis','BronchialAsthma','Hypertension','Migraine','Cervicalspondylosis','Paralysis(brainhemorrhage)','Jaundice','Malaria','Chickenpox','Dengue','Typhoid','hepatitisA','HepatitisB','HepatitisC','HepatitisD','HepatitisE','Alcoholichepatitis','Tuberculosis'
,'CommonCold','Pneumonia','Dimorphichemmorhoids(piles)','Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis','Arthritis',
         '(vertigo)Paroymsal Positional Vertigo','Acne','Urinary tract infection','Psoriasis','Impetigo']


def _norm_label(s):
    import re
    return re.sub(r'[^a-z0-9]', '', str(s).lower())


def build_models(verbose=False):
    """Build and return (tree, forest, gnb, symptoms, disease).

    This function caches models in module-level variables so repeated calls are cheap.
    """
    global _MODEL_TREE, _MODEL_FOREST, _MODEL_GNB, _SYMPTOMS, _DISEASE
    if _MODEL_TREE is not None:
        return _MODEL_TREE, _MODEL_FOREST, _MODEL_GNB, _SYMPTOMS, _DISEASE

    # Read CSVs using paths relative to this file for cross-platform compatibility
    base_dir = os.path.dirname(os.path.abspath(__file__))
    train_path = os.path.join(base_dir, 'training.csv')
    test_path = os.path.join(base_dir, 'Testing.csv')
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    # normalize column names: remove stray spaces so they match symptom keys
    train.columns = train.columns.str.replace(' ', '', regex=False)
    test.columns = test.columns.str.replace(' ', '', regex=False)

    # symptoms list (reuse original variable content)
    _SYMPTOMS = [
        'itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze'
    ]

    _DISEASE = list(disease)

    # Build robust mapping for prognosis labels to integer classes.
    all_labels = pd.concat([train['prognosis'], test['prognosis']], ignore_index=True).unique()
    mapping = {}
    for lab in all_labels:
        nlab = _norm_label(lab)
        found = None
        for i, d in enumerate(_DISEASE):
            if _norm_label(d) == nlab:
                found = i
                break
        if found is None:
            for i, d in enumerate(_DISEASE):
                if _norm_label(d) in nlab or nlab in _norm_label(d):
                    found = i
                    break
        if found is None:
            found = len(_DISEASE)
            _DISEASE.append(lab)
        mapping[lab] = found

    train['prognosis'] = train['prognosis'].map(mapping)
    test['prognosis'] = test['prognosis'].map(mapping)

    X_train = train[_SYMPTOMS]
    y_train = np.ravel(train[['prognosis']])
    X_test = test[_SYMPTOMS]
    y_test = np.ravel(test[['prognosis']])

    # Train models
    _MODEL_TREE = DecisionTreeClassifier().fit(X_train, y_train)
    _MODEL_FOREST = RandomForestClassifier().fit(X_train, y_train)
    _MODEL_GNB = GaussianNB().fit(X_train, y_train)

    if verbose:
        print(f' Train score: {round(_MODEL_TREE.score(X_train, y_train), 2) * 100}')
        print(f' Test score: {round(_MODEL_TREE.score(X_test, y_test), 2) * 100}')
        tree_predict = _MODEL_TREE.predict(X_test)
        print(f'accuracy_score: {round(accuracy_score(y_test, tree_predict),2)*100} %')

    return _MODEL_TREE, _MODEL_FOREST, _MODEL_GNB, _SYMPTOMS, _DISEASE


def predict_symptoms(input_symptoms, algorithm='tree'):
    """Return predicted disease name given an iterable of symptom strings.

    The function will build models on first call (lazily).
    """
    global _MODEL_TREE, _MODEL_FOREST, _MODEL_GNB, _SYMPTOMS, _DISEASE
    if _MODEL_TREE is None:
        # build models silently
        build_models(verbose=False)

    # ensure symptoms list is available
    if _SYMPTOMS is None:
        build_models()

    # normalize input
    if not isinstance(input_symptoms, (list, set, tuple)):
        try:
            input_symptoms = list(input_symptoms)
        except Exception:
            input_symptoms = [input_symptoms]

    input_set = set(map(str, input_symptoms))

    # create feature vector
    local_result = [1 if s in input_set else 0 for s in _SYMPTOMS]
    labels = [local_result]

    if algorithm == 'random':
        pred = _MODEL_FOREST.predict(labels)
    elif algorithm == 'gnb':
        pred = _MODEL_GNB.predict(labels)
    else:
        pred = _MODEL_TREE.predict(labels)

    try:
        idx = int(pred[0])
    except Exception:
        return None

    if 0 <= idx < len(_DISEASE):
        return _DISEASE[idx]
    return None


if __name__ == '__main__':
    # if run as script, build models with verbose output and run a demo prediction
    build_models(verbose=True)
    sample = {'itching','skin_rash','nodal_skin_eruptions'}
    print('Sample prediction ->', predict_symptoms(sample))
                           

                  
