import streamlit as st
import numpy as np
import pandas as pd
import joblib

model=joblib.load('Logistic_Regression_dry_bean_model.pkl')
label_encoder=joblib.load('label_encoder (1).pkl')
scaler=joblib.load('scaler (1).pkl')


st.title('Dry Bean Classification Application')
st.write('This model Predict Dr Beans types according to the input features below.Enter your values')

Perimeter=st.slider('Perimeter:',538,1847)
Eccentricity=st.slider('Eccentricity:',0.4,0.9)
Solidity=st.slider('Solidity:',0.96,0.99)
roundness=st.slider('roundness:',0.68,0.99)
ShapeFactor1=st.slider('ShapeFactor1:',0.00,0.01)
ShapeFactor2=st.slider('ShapeFactor2:',0.00,0.01)
ShapeFactor4=st.slider('ShapeFactor4:',0.98,1.00)

features=np.array([[Perimeter,Eccentricity,Solidity,roundness,ShapeFactor1,ShapeFactor2,ShapeFactor4]])
scaled_features=scaler.transform(features)

if st.button('Predict Bean Type'):
    prediction_encoded=model.predict(scaled_features)
    prediction_label=label_encoder.inverse_transform(prediction_encoded)[0]
    st.success(f'Predict Bean type :{prediction_label}')
