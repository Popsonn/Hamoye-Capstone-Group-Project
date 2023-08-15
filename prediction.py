import joblib
import os
import numpy as np

def predict(features):
    # Encoding dictionaries
    encoding_grade = {'No Proliferation': 1, 'Limited Proliferation': 2, 'Aggressive Proliferation': 3}
    encoding_rt = {'Not Received': 0, 'Received': 1}
    encoding_t_stage = {'Very Small': 1, 'Small': 2, 'Medium': 3, 'Large': 4}
    encoding_ct = {'Not Received': 0, 'Received': 1}
    encoding_n_stage = {'No Metastasis': 0, 'Metastasis to 1 Lymph Node': 1,
                        'Metastasis to 2 Lymph Nodes': 2, 'Metastasis to Multiple Lymph Nodes': 3}

    # Convert features to a numpy array
    features = np.array(features)

    # Perform encoding for each column
    features[:, 0] = [encoding_grade.get(item, -1) for item in features[:, 0]]
    features[:, 1] = [encoding_rt.get(item, -1) for item in features[:, 1]]
    features[:, 2] = [encoding_t_stage.get(item, -1) for item in features[:, 2]]
    features[:, 3] = [encoding_ct.get(item, -1) for item in features[:, 3]]
    features[:, 4] = [encoding_n_stage.get(item, -1) for item in features[:, 4]]

    # Convert features to float
    features = features.astype(float)

    model_path = os.path.join(os.path.dirname(__file__), "ensembled_model2.sav")
    ensembled_model = joblib.load(model_path)
    result = ensembled_model.predict(features)

    if result == 1:
        return "Death"
    else:
        return "Survival"
