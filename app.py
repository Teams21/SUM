"""_summary_
Create a prediction from the model based on the input paramameters from the app.
"""
import pickle
from datetime import datetime
import streamlit as st
import pandas as pd

# Initialize an empty DataFrame to store data
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=[
        'Age', 'Job', 'Education', 'Default', 'Balance', 'Housing', 'Loan', 'Contact', 
        'Day', 'Month', 'Duration', 'Campaign', 'Poutcome', 'Previous'
    ])

def main():
    """_summary_
    Main function of the application.
    Create a prediction from the model based on the input paramameters from the app.
    """
    # Dictionaries to map integer values to categorical values
    app_inputs = {
        'job_d': {
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
        },
        'education_d': {
            0: 'primary',
            1: 'secondary',
            2: 'tertiary',
            3: 'unknown'
        },

        'default_d': {
            0: 'no',
            1: 'yes'
        },

        'housing_d': {
            0: 'no',
            1: 'yes'
        },

        'loan_d': {
            0: 'no',
            1: 'yes'
        },

        'contact_d': {
            0: 'cellular',
            1: 'telephone',
            2: 'unknown'
        },

        'month_d': {
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
        },

        'poutcome_d': {
            0: 'failure',
            1: 'other',
            2: 'success',
            3: 'unknown'
        }
    }


    # Title of the application
    title = 'Will the customer take advantage of the bank\'s offer?'
    # Set the page configuration
    st.set_page_config(page_title=title)

    # Container for the overview
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    # Display the title
    with overview:
        st.title(title)
        # Display an image
        st.image(
            'bank.png'
        )

    # Input fields for user data
    with left:
        job_radio = st.radio('Job',
                             list(app_inputs['job_d'].keys()),
                             format_func=lambda x: app_inputs['job_d'][x])

        education_radio = st.radio('Education',
                                   list(app_inputs['education_d'].keys()),
                                   format_func=lambda x: app_inputs['education_d'][x])

        default_radio = st.radio('Default',
                                 list(app_inputs['default_d'].keys()),
                                 format_func=lambda x: app_inputs['default_d'][x])

        housing_radio = st.radio('Housing',
                                 list(app_inputs['housing_d'].keys()),
                                 format_func=lambda x: app_inputs['housing_d'][x])

        loan_radio = st.radio('Loan',
                              list(app_inputs['loan_d'].keys()),
                              format_func=lambda x: app_inputs['loan_d'][x])

        contact_radio = st.radio('Contact',
                                 list(app_inputs['contact_d'].keys()),
                                 format_func=lambda x: app_inputs['contact_d'][x])

        month_radio = st.radio('Month',
                               list(app_inputs['month_d'].keys()),
                               format_func=lambda x: app_inputs['month_d'][x])

        poutcome_radio = st.radio('Poutcome',
                                  list(app_inputs['poutcome_d'].keys()),
                                  format_func=lambda x: app_inputs['poutcome_d'][x])

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
    # Load the model
    file_name = 'ml_models/banking_model.h5'
    model = pickle.load(open(file_name, 'rb'))
    accept_offer = model.predict(data)
    s_confidence = model.predict_proba(data)

    # Displaying the prediction and confidence
    with prediction:
        st.header(f'{title} {"Yes" if accept_offer[0] == 1 else "No"}')
        st.subheader(f'Confidence: {s_confidence[0][accept_offer][0] * 100:,.2f} %')

    # Add a button to add data to the DataFrame
    if st.button('Add Data'):
        new_data = pd.DataFrame(data, columns=[
            'Age', 'Job', 'Education', 'Default', 'Balance', 'Housing', 'Loan', 'Contact', 
            'Day', 'Month', 'Duration', 'Campaign', 'Poutcome', 'Previous'
        ])
        st.session_state.df = pd.concat([st.session_state.df, new_data], ignore_index=True)
        st.write('Data added to the DataFrame.')

    # Add a button to save the DataFrame as a CSV file
    if st.button('Save Data as CSV'):
        csv_filename = f'data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        st.session_state.df.to_csv(csv_filename, index=False)
        st.write(f'Data saved to {csv_filename}')

if __name__ == '__main__':
    main()
