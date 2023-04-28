# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:46:37 2023

@author: gokul
"""

import os
import json
import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model


model_path = "C:/Users/gokul/Downloads/resnet.h5"
model = load_model(model_path)

# Define prediction function
def predict(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img, (224, 224))
    img_array = np.array(img_resized)
    img_expanded = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_expanded)
    return prediction

# Define Streamlit app
def app():
    st.title("Object Detection")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    
    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        prediction = predict(image)
        st.write("Prediction:", prediction)
