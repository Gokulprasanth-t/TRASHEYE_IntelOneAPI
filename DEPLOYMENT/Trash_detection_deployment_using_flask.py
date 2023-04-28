#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)


model = load_model("C:/Users/gokul/Downloads/resnet.h5")


@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    
    image = request.files['image'].read()
    
    
    npimg = np.frombuffer(image, np.uint8)
    
    
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    
    
    predictions = model.predict(img)
    
    
    class_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
    
    
    pred_class_idx = np.argmax(predictions)
    
    
    pred_class_label = class_labels[pred_class_idx]
    
    return jsonify({'prediction': pred_class_label})

if __name__ == '__main__':
    app.run(debug=True)

