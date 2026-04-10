import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=names)

X = data.drop(columns='Outcome', axis=1)
Y = data['Outcome']

scaler = StandardScaler()
scaler.fit(X)
model = SVC(kernel='linear')
model.fit(scaler.transform(X), Y)

pickle.dump(scaler, open('scaler.pkl', 'wb'))
pickle.dump(model, open('model.pkl', 'wb'))

print("Success")