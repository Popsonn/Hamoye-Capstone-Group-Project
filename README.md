# Predicting Survival of Tongue Cancer Patients

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project aims to predict the survival of tongue cancer patients using machine learning models. It was developed as part of the data science internship with Hamoye during the HDSC Spring 2023 program.

## Team Members

- Oladimeji Williams (Project Lead)
- Aramide Adebesin (Assistant Project Lead)
- Confidence Chinelo (Project Query Analyst)
- Oluwaseun Ogundeko
- Deborah Popoola
- Isibor Blessing
- Harshit Khandelwal
- Akinyemi Akeem
- John Afariogun
- Aayush Pandey
- Hema Kokku
- Sangotade Idowu
- Opeyemi Owuye

## Project Description

The project utilized a dataset containing information on 1,712 tongue cancer curative surgery recipients. Each row represents one patient, and the dataset includes various attributes such as gender, survival status, follow-up time, tumor stage, operation status, radiation therapy status, chemotherapy status, tumor size, metastasis to lymph nodes, and tumor grade.

The goal of the project was to develop machine learning models to predict the survival outcome of tongue cancer patients based on these attributes. After several iterations, the best model was found to be the Random Forest Classifier.

## Repository and Dataset

The project repository can be found [here](https://zenodo.org/record/7450476/files/tongue.csv?download=1). It contains the dataset used in the paper "Predicting Survival of Tongue Cancer Patients by Machine Learning Models." The dataset consists of a CSV file and provides valuable information for further analysis and research.

## Supporting Visualizations and Materials

- The supporting visualizations for this project can be accessed on [Power BI](https://app.powerbi.com/view?r=eyJrIjoiNDJiYjVlYzQtM2QyNS00ZTE5LTg4MDMtOGM3ZWEyMzlmZTZjIiwidCI6IjU0NjJmMDc4LWFiYTgtNDE1OS05MWYwLWVhODg1MmJjOTU4NCJ9).
  - The presentation deck for the project is hosted on [Google Slides](https://docs.google.com/presentation/d/1La09J2KCr4_CrKrpAwL1rEPHHECyh_6R/edit?usp=sharing&ouid=115275109673336716857&rtpof=true&sd=true).
- The detailed report on this project can be found on [Google Docs](https://docs.google.com/document/d/1cdDtPMrdK7mvylT8GQ7FhC7igPEk0gAQsptVxLop_5o/edit?usp=sharing).

## Deployment

The project is deployed using [Streamlit](https://tonguecancer.streamlit.app/), a Python library for building interactive web applications. The deployed application allows users to input the required attributes and obtain predictions for the survival outcome of tongue cancer patients.

To run the application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## License

This project is licensed under the [MIT License](LICENSE).
