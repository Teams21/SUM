import streamlit as st
import pickle
from datetime import datetime

# Load the model
filename = 'ml_models/banking_model.h5'
model = pickle.load(open(filename, 'rb'))

# Dictionaries to map integer values to categorical values
job_d = {
    0: 'admin.',
    1: 'blue-collar',
    2: 'entrepreneur',
    3: 'housemaid',
    4: 'management',
    5: 'retired',
    6: 'self-employed',
    7: 'services',
    8: 'student',
    9: 'technician',
    10: 'unemployed',
    11: 'unknown'
}

education_d = {
    0: 'primary',
    1: 'secondary',
    2: 'tertiary',
    3: 'unknown'
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

# Title of the application
title = 'Will the customer take advantage of the bank\'s offer?'

def main():
    # Set the page configuration
    st.set_page_config(page_title=title)

    # Container for the overview
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    # Display an image
    st.image(
        'https://media1.popsugar-assets.com/files/thumbor/7CwCuGAKxTrQ4wPyOBpKjSsd1JI/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/04/19/743/n/41542884/5429b59c8e78fbc4_MCDTITA_FE014_H_1_.JPG'
    )

    # Display the title
    with overview:
        st.title(title)

    # Input fields for user data
    with left:
        job_radio = st.radio('Job', list(job_d.keys()), format_func=lambda x: job_d[x])
        education_radio = st.radio('Education', list(education_d.keys()), format_func=lambda x: education_d[x])
        default_radio = st.radio('Default', list(default_d.keys()), format_func=lambda x: default_d[x])
        housing_radio = st.radio('Housing', list(housing_d.keys()), format_func=lambda x: housing_d[x])
        loan_radio = st.radio('Loan', list(loan_d.keys()), format_func=lambda x: loan_d[x])
        contact_radio = st.radio('Contact', list(contact_d.keys()), format_func=lambda x: contact_d[x])
        month_radio = st.radio('Month', list(month_d.keys()), format_func=lambda x: month_d[x])
        poutcome_radio = st.radio('Poutcome', list(poutcome_d.keys()), format_func=lambda x: poutcome_d[x])

    with right:
        age_slider = st.slider('Age', value=50, min_value=18, max_value=95)
        balance_slider = st.slider('# Balance', min_value=-8019, max_value=102127)
        day_slider = st.slider('# Day', min_value=1, max_value=31)
        duration_slider = st.slider('Duration', min_value=0, max_value=4918, step=10)
        campaign_slider = st.slider('Campaign', min_value=1, max_value=63)
        previous_slider = st.slider('Previous', min_value=0, max_value=275)

    # Collecting the input data
    data = [[
        age_slider,
        job_radio,
        education_radio,
        default_radio,
        balance_slider,
        housing_radio,
        loan_radio,
        contact_radio,
        day_slider,
        month_radio,
        duration_slider,
        campaign_slider,
        poutcome_radio,
        previous_slider
    ]]

    # Making prediction
    accept_offer = model.predict(data)
    s_confidence = model.predict_proba(data)

    # Displaying the prediction and confidence
    with prediction:
        st.header(f'{title} {"Yes" if accept_offer[0] == 1 else "No"}')
        st.subheader(f'Confidence: {s_confidence[0][accept_offer][0] * 100:,.2f} %')

if __name__ == '__main__':
    main()
