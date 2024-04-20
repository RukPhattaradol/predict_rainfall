import numpy as np
import pandas as pd

# สร้างข้อมูลสุ่ม
np.random.seed(0)
num_samples = 10000 #จำนวนrowที่ต้องการ

humValues = np.random.uniform(50, 70, num_samples).round(2)
tempValues = np.random.uniform(28, 38, num_samples).round(2)
rainChances = np.random.uniform(40, 100, num_samples).round(2)

# สร้าง DataFrame
random_data = pd.DataFrame({
    'humValue': humValues,
    'tempValue': tempValues,
    'rain': rainChances
})

# บันทึก DataFrame เป็นไฟล์ CSV
random_data.to_csv('simpledata.csv', index=False)
