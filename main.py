import pandas as pd
import pickle

# โหลดโมเดลจากไฟล์
with open('./model/model.pkl', 'rb') as file:
    model = pickle.load(file)

# ใส่ค่าที่ต้องการทำนาย
values = [
    {"humValue": 74, "tempValue": 38},
] 

# สร้าง DataFrame จากข้อมูล
df = pd.DataFrame(values)

# ใช้โมเดลทำนาย
predictions = model.predict(df[['humValue', 'tempValue']])

# แสดงผลลัพธ์การทำนาย
print(predictions)
