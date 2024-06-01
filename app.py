import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()

filename = "ml_models/model"
model = pickle.load(open(filename, "rb"))

job_d = {
    0: "admin.",
    1: "unknown",
    2: "unemployed",
    3: "management",
    4: "housemaid",
    5: "entrepreneur",
    6: "student",
    7: "blue-collar",
    8: "self-employed",
    9: "retired",
    10: "technician",
    11: "services"
}

marital_d = {
    0: "divorced",
    1: "married",
    2: "single"
}

education_d = {
    0: "primary",
    1: "secondary",
    2: "tertiary",
    3: "unknown"
}

default_d = {
    0: 'no',
    1: 'yes'
}

housing_d = {
    0: 'no',
    1: 'yes'
}

loan_d = {
    0: 'no',
    1: 'yes'
}

contact_d = {
    0: 'cellular',
    1: 'telephone',
    2: 'unknown'
}

month_d = {
    0: 'apr',
    1: 'aug',
    2: 'dec',
    3: 'feb',
    4: 'jan',
    5: 'jul',
    6: 'jun',
    7: 'mar',
    8: 'may',
    9: 'nov',
    10: 'oct',
    11: 'sep'
}

poutcome_d = {
    0: 'failure',
    1: 'other',
    2: 'success',
    3: 'unknown'
}

y_d = {
    0: 'no',
    1: 'yes'
}

def main():
    st.set_page_config(page_title="Will the customer take advantage of the bank's offer?")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image(
        "https://media1.popsugar-assets.com/files/thumbor/7CwCuGAKxTrQ4wPyOBpKjSsd1JI/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/04/19/743/n/41542884/5429b59c8e78fbc4_MCDTITA_FE014_H_1_.JPG%22"
    )

    with overview:
        st.title("Will the customer take advantage of the bank's offer?")

    with left:
        job_radio = st.radio("Job", list(job_d.keys()), format_func=lambda x: job_d[x])
        marital_radio = st.radio("Martial", list(marital_d.keys()), format_func=lambda x: marital_d[x])
        education_radio = st.radio("Education", list(education_d.keys()), format_func=lambda x: education_d[x])
        default_radio = st.radio("Default", list(default_d.keys()), format_func=lambda x: default_d[x])
        housing_radio = st.radio("Housing", list(housing_d.keys()), format_func=lambda x: housing_d[x])
        loan_radio = st.radio("Loan", list(loan_d.keys()), format_func=lambda x: loan_d[x])
        contact_radio = st.radio("Contact", list(contact_d.keys()), format_func=lambda x: contact_d[x])
        month_radio = st.radio("Month", list(month_d.keys()), format_func=lambda x: month_d[x])
        poutcome_radio = st.radio("Poutcome", list(poutcome_d.keys()), format_func=lambda x: poutcome_d[x])
        y_radio = st.radio("Y", list(y_d.keys()), format_func=lambda x: y_d[x])


    with right:
        age_slider = st.slider("Age", value=50, min_value=18, max_value=95)
        balance_slider = st.slider("# Balance", min_value=-8019, max_value=102127)
        day_slider = st.slider("# Day", min_value=1, max_value=31)
        duration_slider = st.slider("Duration", min_value=0, max_value=4918, step=10)
        campaign_slider = st.slider("Campaign", min_value=1, max_value=63)
        pdays_slider = st.slider("P_days", min_value=-1, max_value=871)
        previous_slider = st.slider("Previous", min_value=0, max_value=275)

    data = []

    survival = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.header("Czy dana osoba przeżyje? {0}".format("Tak" if survival[0] == 1 else "Nie"))
        st.subheader("Pewność predykcji {0:,.2f} %".format(s_confidence[0][survival][0]*100))
        st

if __name__ == "__main__":
    main()