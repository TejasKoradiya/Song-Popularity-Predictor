import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle as pk
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

dftrn = pd.read_csv('C:\\Users\\Dell\\OneDrive\\Desktop\\Project 2\\Dataset\\dataset.csv')
# dftst = pd.read_csv('C:\\Users\\Dell\\OneDrive\\Desktop\\Project 2\\test.csv')

X = dftrn.iloc[:,5:19]
# print(X)
Y = dftrn['popularity']

# Xts = dftst
# xtr,xts,ytr,yts = train_test_split(X,Y,test_size=0.3,random_state=1000)

le = LabelEncoder()
X['explicit'] = le.fit_transform(X['explicit'])
# Xts['explicit'] = le.fit_transform(Xts['explicit'])
# print(pd.DataFrame(xtr))

# sc = StandardScaler()
# X = sc.fit_transform(X)
# Xts = sc.transform(Xts)
# # print(pd.DataFrame(xtr))

lr = LinearRegression()
lr.fit(X,Y)
pk.dump(lr,open('flaskmodel.pkl','wb'))

#pickle to access the model outside this file
# testmodel = pk.load(open('flaskmodel.pkl','rb'))
# pred = testmodel.predict(Xts)
# print(pred)
# mse = metrics.mean_squared_error(yts,pred)
# print("MSE:",mse)