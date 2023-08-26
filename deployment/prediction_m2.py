import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load All Files
load_model = joblib.load("best_model.pkl")

def run():

#min and max value user bisa input minimal 16 dan max angka 60, value nilai default
    with st.form('key=hotel_reservation_form'):
        booking_id = st.number_input('Booking ID', step=1)
        no_adults= st.number_input('Number of Adults', min_value=1)
        no_children = st.number_input('Number of Children', value=0)
        no_weekend = st.number_input('Number of Weekend', value=0)
        no_week = st.number_input('Number of Week', value=0)
        meal_plan = st.radio('Meal Plan', ['Meal Plan 1', 'Not Selected', 'Meal Plan 2', 'Meal Plan 3'])
        car_parking = st.radio('Required Car Parking?', [0 , 1])
        room_type = st.radio('Room Type', ['Room_Type 1', 'Room_Type 4', 'Room_Type 2', 'Room_Type 6', 'Room_Type 5','Room_Type 7', 'Room_Type 3'])
        lead_time = st.number_input('Lead Time', min_value=0, max_value=400, value=0)
        arrival_year = st.slider('Arrival Year', 2019,2023)
        arrival_month = st.slider('Arrival Month', 1,12)
        arrival_date = st.slider('Arrival Date', 1,31)
        market_segment = st.radio('Market Segment Type', ['Offline', 'Online', 'Corporate', 'Aviation', 'Complementary'])
        repeated_guest =  st.radio('Repeated Guest', [0 , 1])
        no_of_previous_cancellations = st.number_input('Number of Previous cancellations', min_value=0)
        previous_bookings_not_canceled = st.number_input('Number of Previous Booking Not Canceled', min_value=0)
        average_price = st.number_input('Average Price', min_value=65)
        special_req = st.number_input('Number of Special Request', min_value=0)
        st.markdown('---')

        submitted  = st.form_submit_button('Predict')

        #Data input
        # Create New Data

        data_inf = {
            'Booking_ID': booking_id,
            'no_of_adults': no_adults,
            'no_of_children': no_children,
            'no_of_weekend_nights':no_weekend,
            'no_of_week_nights':no_week,
            'type_of_meal_plan': meal_plan,
            'required_car_parking_space': car_parking,
            'room_type_reserved': room_type,
            'lead_time': lead_time,
            'arrival_year': arrival_year,
            'arrival_month': arrival_month,
            'arrival_date': arrival_date,
            'market_segment_type': market_segment,
            'repeated_guest': repeated_guest,
            'no_of_previous_cancellations': no_of_previous_cancellations,
            'no_of_previous_bookings_not_canceled': previous_bookings_not_canceled,
            'avg_price_per_room': average_price,
            'no_of_special_requests': special_req
        }

        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)

    if submitted:
        # Predict using the model
        data_inf_pred = load_model.predict(data_inf)

        # Display the result
        st.write('# Booking Status:', data_inf_pred)

if __name__ == '__main__':
    run()
