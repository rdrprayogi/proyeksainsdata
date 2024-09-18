import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('stok_barangfix.csv')
label_encoder = LabelEncoder()
data['Kategori_encoded'] = label_encoder.fit_transform(data['Kategori'])

print(data)
print("Kategori dalam bentuk numerik:", data['Kategori_encoded'].values)
