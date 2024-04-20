import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# โหลดข้อมูล
df = pd.read_csv('./data/data.csv')

# แยก features และ target
X = df[['humValue', 'tempValue']]
y = df['rain']

# แบ่งข้อมูลเป็น train และ test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างและฝึกโมเดล
model = RandomForestRegressor()
model.fit(X_train, y_train)

# ทำนายค่าต่อเนื่องของความน่าจะเป็นของการฝนตก
predictions = model.predict(X_test)
print("Predicted probabilities of rain:", predictions)

# บันทึกโมเดลเป็นไฟล์ pkl
with open('./model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
