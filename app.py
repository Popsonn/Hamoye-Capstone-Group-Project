import streamlit as st
import numpy as np
from prediction import predict

def main():
    st.markdown('<h1 class="title">Survival of Tongue Cancer Patients</h1>', unsafe_allow_html=True)
    st.write('Predict whether a patient with tongue cancer will survive or not')

    st.markdown('<h5 class="title">Patient Diagnostic Features</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        grade = st.radio("Tumor Grade", ['No Proliferation', 'Limited Proliferation', 'Aggressive Proliferation'],
                      help='Select 1 out of 3 options for the tumor grade ')
        rt = st.radio("Radiation Therapy Status", ['Not Received', 'Received'],
                      help='Select 1 out of 2 options for the operation status ')
        t_stage = st.radio("Tumor Size", ['Very Small', 'Small', 'Medium', 'Large'],
                      help='Select 1 out of 2 options of the tumor size')

    with col2:
        ct = st.radio("Chemotherapy Status", ['Not Received', 'Received'],
                      help='Select 1 out of 2 options of the chemotherapy status')
        n_stage = st.radio("Metastasis to Lymph Nodes", ['No Metastasis', 'Metastasis to 1 Lymph Node', 'Metastasis to 2 Lymph Nodes', 'Metastasis to Multiple Lymph Nodes'],
                           help='Select 1 out of 4 options for metastasis')
        follow_time = st.number_input(
            'Follow-up Days', min_value=1, max_value=150, value=30, step=1, help='Enter a whole number representing the length of the follow-up period in days')

    if st.button("Predict Survival", key='predict_button'):
        result = predict(
            np.array([[grade, rt, t_stage, ct, n_stage, follow_time]])
        )
        st.markdown('<div class="result">{}</div>'.format(result), unsafe_allow_html=True)

    st.markdown(
        '`Created by` Team Python | 2023 | \
            `Code:` [GitHub](https://github.com/Oladimeji-Williams/Tongue_Cancer/blob/main/README.md)'
    )

if __name__ == "__main__":
    main()
