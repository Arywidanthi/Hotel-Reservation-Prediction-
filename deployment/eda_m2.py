import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title= 'Hotel Reservation- EDA',
    layout = 'wide',
    initial_sidebar_state='expanded'
)

def run():

    #Membuat Title
    st.title('Hotel Classification')

    #Membuat Sub Header
    st.subheader('Exploratory Data for Hotel Reservation')

    # Menambahkan Gambar
    image = Image.open('hotel.jpg')
    st.image(image, caption='Hotel King')

    # Menambahkan Deskripsi
    st.write('##### Membuat model classification untuk memprediksi apakah guest hotel yang melakukan reservation akan cancel atau tidak.')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
        Pada page kali ini, penulis akan melakukan eksplorasi sederhana.
        Dataset yang digunakan adalah dataset Hotel Reservation pada Kaggle.
        '''
     #show DataFrame
    data = pd.read_csv('Hotel Reservations.csv')
    st.dataframe(data)

    st.markdown('---')
    #overall pie
    booking_status = data['booking_status'].value_counts()

    fig, ax = plt.subplots(figsize=(2, 4))
    colors = sns.color_palette("mako", len(booking_status))
    ax.pie(booking_status.values, labels=booking_status.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_aspect('equal')
    ax.set_title('Jumlah customer cancel dan tidak')

    st.pyplot(fig)


    # Membuat Histogram Berdasarkan Input (versi select box)
    st.write('### Histogram berdasarkan input user')
    pilihan = st.selectbox('Pilih kolom:', ('type_of_meal_plan', 'market_segment_type', 'room_type_reserved', 'no_of_adults', 'no_of_children'))

    fig = plt.figure(figsize=(15, 5))

    if pilihan == 'type_of_meal_plan':
        meal_plan = data.groupby(['type_of_meal_plan', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='type_of_meal_plan', y='count', hue='booking_status', data=meal_plan, palette='mako', errwidth=0)
    elif pilihan == 'market_segment_type':
        market_segment = data.groupby(['market_segment_type', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='market_segment_type', y='count', hue='booking_status', data=market_segment, palette='mako', errwidth=0)
    elif pilihan == 'room_type_reserved':
        room_type = data.groupby(['room_type_reserved', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='room_type_reserved', y='count', hue='booking_status', data=room_type, palette='mako', errwidth=0)
    elif pilihan == 'no_of_adults':
        no_adult = data.groupby(['no_of_adults', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='no_of_adults', y='count', hue='booking_status', data=no_adult, palette='mako', errwidth=0)
    elif pilihan == 'no_of_children':
        no_children = data.groupby(['no_of_children', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='no_of_children', y='count', hue='booking_status', data=no_children, palette='mako', errwidth=0)

    st.pyplot(fig)




    # Membuat Histogram Berdasarkan Input (versi radio button)
    st.write('### Histogram berdasarkan input user')
    pilihan = st.radio('Pilih kolom:', ('no_of_weekend_nights', 'no_of_week_nights', 'required_car_parking_space', 'repeated_guest', 'no_of_special_requests'))

    fig = plt.figure(figsize=(15, 5))

    if pilihan == 'no_of_weekend_nights':
        no_weekend = data.groupby(['no_of_weekend_nights', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='no_of_weekend_nights', y='count', hue='booking_status', data=no_weekend, palette='mako', errwidth=0)
    elif pilihan == 'no_of_week_nights':
        no_week = data.groupby(['no_of_week_nights', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='no_of_week_nights', y='count', hue='booking_status', data=no_week, palette='mako', errwidth=0)
    elif pilihan == 'required_car_parking_space':
        car_parking = data.groupby(['required_car_parking_space', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='required_car_parking_space', y='count', hue='booking_status', data=car_parking, palette='mako', errwidth=0)
    elif pilihan == 'repeated_guest':
        repeat_guest = data.groupby(['repeated_guest', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='repeated_guest', y='count', hue='booking_status', data=repeat_guest, palette='mako', errwidth=0)
    elif pilihan == 'no_of_special_requests':
        no_req = data.groupby(['no_of_special_requests', 'booking_status']).size().reset_index(name='count')
        sns.barplot(x='no_of_special_requests', y='count', hue='booking_status', data=no_req, palette='mako', errwidth=0)
    st.pyplot(fig)
if __name__ == '__main__':
    run()