from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

model_path = '/home/user/PROJECTS/Big_mart_Sales_Prediction/models/model2.pkl'
model = joblib.load((model_path))
# booster = xgb.Booster()
# booster.load_model('model.bin')
scaler_path = '/home/user/PROJECTS/Big_mart_Sales_Prediction/models/scaled.pkl' 
scale = joblib.load((scaler_path))

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def result():

    item_weight= float(request.form['Item_Weight'])
    item_fat_content=float(request.form['Item_Fat_Content'])
    item_visibility= float(request.form['Item_Visibility'])
    item_type= float(request.form['Item_Type'])
    item_mrp = float(request.form['Item_MRP'])
    outlet_establishment_year= float(request.form['Outlet_Year'])
    outlet_size= float(request.form['Outlet_Size'])
    outlet_location_type= float(request.form['Outlet_Location_Type'])
    outlet_type= float(request.form['Outlet_Type'])

    feature_value = np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    features_name = ['Item_Weight', 'Item_Visibility','Item_Type', 'Item_MRP', 'Outlet_Year',
    'Item_Fat_Content','Outlet_Size', 'Outlet_Location_Type','Outlet_Type']

    df = pd.DataFrame(feature_value, columns=features_name)

    Y_pred=model.predict(df)
    output=round(Y_pred[0],2)


    # return jsonify({'Prediction': float(Y_pred)})
    return render_template('result.html',prediction = output)

if __name__ == "__main__":
    app.run(debug=True)   #port=9457
