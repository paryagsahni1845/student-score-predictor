from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
# Assuming src.pipeline.predict_pipeline exists and works as expected
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    """Renders the welcome home page."""
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    """
    Handles GET and POST requests for predicting student exam performance.
    GET: Renders the prediction form.
    POST: Processes form data, makes a prediction, and displays the result.
    """
    if request.method=='GET':
        # Pass results=None for the initial GET request to prevent UndefinedError
        return render_template('home.html', results=None)
    else:
        # Create a CustomData object from form submissions
        # IMPORTANT: Ensure 'reading_score' and 'writing_score' are correctly mapped
        # to their respective form input names.
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')), # Corrected mapping
            writing_score=float(request.form.get('writing_score'))  # Corrected mapping
        )
        
        # Convert custom data to a pandas DataFrame for prediction
        pred_df=data.get_data_as_data_frame()
        print("Input DataFrame for Prediction:")
        print(pred_df)
        print("Before Prediction")

        # Initialize and run the prediction pipeline
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("After Prediction")
        
        # Render the home.html template with the prediction result
        # results[0] is used assuming the predict method returns a list/array with the score at index 0
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    # Run the Flask application
    # debug=True should only be used during development, not in production
    app.run(host="0.0.0.0", debug=True)
