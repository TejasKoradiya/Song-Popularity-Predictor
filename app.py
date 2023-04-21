from flask import Flask, request, render_template
from features import extract_features
import pickle as pk
from sklearn.preprocessing import LabelEncoder
import pandas as pd
app = Flask(__name__)

le = LabelEncoder()

def preprocess(url):
    test_feat = extract_features(url)
    df = pd.DataFrame(test_feat,index=[0])
    df['explicit'] = le.fit_transform(df['explicit'])
    df = df.iloc[:,[12,0,1,2,3,4,5,6,7,8,9,10,11,13]]
    return df,test_feat
    

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST','GET'])
def submit():
    url = request.form['url']
    test_vals,test_feat = preprocess(url)
    model = pk.load(open("flaskmodel.pkl","rb"))
    otp = model.predict(test_vals)
    feat_format = "<br>".join([f"{key} = {value}" for key,value in zip(test_feat.keys(),test_feat.values())])
    print("Prediction: ",otp)
    return "Prediction: {} <br><br> Features: <br>{}".format(otp[0],feat_format)

if __name__ == '__main__':
    app.run(port=5500)
