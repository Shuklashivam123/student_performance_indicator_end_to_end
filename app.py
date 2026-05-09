# --------------------- REQUIRED LIBRARIES ---------------------
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler  # (model ke preprocessing ke liye use hota hai)
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
# CustomData -> form se input data ko DataFrame me convert karta hai
# PredictPipeline -> trained model ko load karke prediction karta hai


# --------------------- FLASK APP INITIALIZATION ---------------------
application = Flask(__name__)
app = application   # 'app' name se bhi use kar sake isliye alias


# --------------------- ROUTES ---------------------

## 1. Home Page Route
@app.route('/')
def index():
    # index.html render karega (basically landing page)
    return render_template('index.html')


## 2. Prediction Route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    # Agar sirf page khola (GET request)
    if request.method == 'GET':
        return render_template('home.html')   # form wala page dikhayega

    # Agar form submit kiya (POST request)
    else:
        # --------------------- STEP 1: Collect Form Data ---------------------
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),  # swapped in form
            writing_score=float(request.form.get('reading_score'))   # swapped in form
        )

        # --------------------- STEP 2: Convert to DataFrame ---------------------
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        # --------------------- STEP 3: Prediction Pipeline ---------------------
        predict_pipeline = PredictPipeline()   # trained model ko load karega
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)   # prediction karega
        print("After Prediction")

        # --------------------- STEP 4: Show Result ---------------------
        return render_template('home.html', results=round(results[0],2))  # result HTML page me dikhayega
    


# --------------------- MAIN ENTRY POINT ---------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)