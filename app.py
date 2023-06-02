
from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from flask_ngrok import run_with_ngrok

import pandas as pd
import numpy as np
import re
import pickle
import nltk
import joblib

from process import preparation, generate_response

preparation()

# =[Variabel Global]=============================

app   = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk Halaman Utama atau Home]	
@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

# Routing for API response chatbot
@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == '__main__':
	
	# Load model yang telah ditraining
	#model = load('model_iris_dt.model')

	# Run Flask di google colab 
	run_with_ngrok(app)
	app.run()
	
	


