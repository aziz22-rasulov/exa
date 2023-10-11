import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st

from PIL import Image


pickle_in = open("Home_price.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(market_code, rooms, floor, area, remodel_code):
    
    
    prediction=classifier.predict([[market_code, rooms, floor, area, remodel_code]])
    print(prediction)
    return prediction


def main():
    st.title("Prediction of House Price")
    html_temp = """
    <div style="background-color:blue    ;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of house price in Dushanbe. Based on data from Somon.tj, algorithm GBoosting Regressor  </h2>
    </div>
    """
    
    
    
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    m=st.radio("Type of market 👉",
        key="market",
        options=["Новостройка", "Вторичный рынок"],    )
    if m=="Вторичный рынок":
        market_code=1
    elif m=="Новостройка":
        market_code=0

    rooms = st.number_input('rooms', step=1, value=1)
    floor = st.number_input('floor', step=1, value=1)
    area = st.number_input('area', step=1, value=15)
    
    r = st.radio("Remodel",
                 key="Remodel",
                 options=["Без ремонта (коробка)", "С ремонтом", "Новый ремонт"], )
    if r == "Без ремонта (коробка)":
        remodel_code = 0
    elif r == "С ремонтом":
        remodel_code = 1
    elif r == "Новый ремонт":
        remodel_code = 2

    result=""
    if st.button("Predict"):
        result=(predict_note_authentication(market_code, rooms, floor, area, remodel_code))


    #st.success('The output is {}'.format(result))
    st.success('Predicted cost of the house is {}'.format(result)+" TJS")
    if st.button("About"):
        st.text("Built by Aziz Rasulov")

if __name__=='__main__':
    main()
