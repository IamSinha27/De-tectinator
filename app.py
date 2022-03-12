
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os
from Filter import main

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
<<<<<<< Updated upstream
@app.route("/index", methods=['POST', 'GET'])
=======
>>>>>>> Stashed changes
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route("/Predict", methods=['POST', 'GET'])
def Predict():
    #Moving forward code
    DATA = main()
    return render_template("Predict.html",DATA = DATA)


if __name__ == "__main__":
    app.run(debug=True)