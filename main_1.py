import pandas as pd
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

dataframe = pd.read_csv('data.csv')

def filter(col,text):
    return dataframe[col].astype(str).str.lower().astype(str).str.contains(text.lower())
def Search(dataframe,text):
    return dataframe[filter('HOSP_NAME',text) | filter('HOSP_TYPE',text) | filter('DISTRICT_NAME',text) | filter('SPECIALTY_NAME',text) | filter('HOSP_CONTACT_NO',text) | filter('HOSP_EMAIL_ID',text) | filter('HOSP_ADDRESS',text)]



@app.route('/data',methods=['POST'])
@cross_origin()
def Data():
    data = request.get_json()['search']
    return Search(dataframe,data).to_numpy().tolist()

if __name__=="__main__":
    app.run(debug=True)