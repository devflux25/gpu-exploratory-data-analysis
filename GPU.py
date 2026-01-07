import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings as wr
import re
wr.filterwarnings('ignore')

path = r"C:\Users\Kairav\OneDrive\Desktop\archive (2)\gpu_1986-2026.csv"
df  = pd.read_csv(path)
print(df.head())
print("\n")
print(df.shape)
print("\n")
print(type(df))
print("\n")
df.info()
print("\n")
print(df.describe().T)
print("\n")
print(df.columns.tolist())


#visvulize for brand releasend by each brands
# 
data_set_1 = df.groupby('Brand')['Graphics Card__Release Date'].count()
#data_set_2 = df['Graphics Card__Release Date'].value_counts()
data_set_1 = data_set_1.sort_values(ascending=False)
plt.figure(figsize=(8, 6))
plt.bar(data_set_1.index ,data_set_1.values,edgecolor = "Black")
plt.xlabel("Brand")
plt.ylabel("No of cards per company")
plt.title("Graphics Card Release Count by Brand")
plt.show()

#gpu clock spped by year 

df['Graphics Card__Release Date'] = pd.to_datetime(df['Graphics Card__Release Date'], errors='coerce').dt.year

df['Clock Speeds__GPU Clock'] = df['Clock Speeds__GPU Clock'].str.replace('MHz','')
df['Clock Speeds__GPU Clock'] = pd.to_numeric(df['Clock Speeds__GPU Clock'])
plot_data = df.dropna(subset=['Graphics Card__Release Date', 'Clock Speeds__GPU Clock'])
data_set_2 = df.groupby('Graphics Card__Release Date')['Clock Speeds__GPU Clock']

yearly_trend = plot_data.groupby('Graphics Card__Release Date')['Clock Speeds__GPU Clock'].mean()

plt.figure(figsize=(8, 6))
plt.plot(yearly_trend.index,yearly_trend.values,color='red',linestyle ='-',marker='o',markersize=9)
plt.xlabel("Years")
plt.ylabel("clock Speeds")
plt.title("GPU Clock Speed Trends: Early Growth to Modern Limits")
plt.grid(True)
plt.show()  

# memory size or Vram by years 
 
def parse_memory(val):
    if pd.isna(val): return None
    
    # 1. Normalize: Uppercase and string conversion
    s = str(val).upper()
    
    
    match = re.search(r"(\d+\.?\d*)", s) 
    if not match: return None 
    
    number = float(match.group(1))
    
    # 3. Handle Units
    if 'GB' in s: return number 
    if 'MB' in s: return number /1024
    if 'KB' in s: return number / 1048576
    
    return None


#df['Top__MEMORY SIZE'] = np.where(df['Top__MEMORY TYPE'] == 'VRAM')
df1 = pd.DataFrame()

df1['Top__MEMORY SIZE'] = df['Top__MEMORY SIZE'].apply(parse_memory)
df1['Graphics Card__Release Date'] = df['Graphics Card__Release Date']


data_3 = df1.groupby('Graphics Card__Release Date')['Top__MEMORY SIZE'].mean()
plt.figure(figsize=(8,6))
plt.plot(data_3.index,data_3.values,color = 'blue',marker='o',markersize=5)
plt.xlabel("Years")
plt.ylabel("VRAM in GB")
plt.title("Average GPU VRAM by Release Year")
plt.grid(True)
plt.show()  


#Clock Speed vs TDP (scatter plot)

df['TDP_Numeric'] = pd.to_numeric(df['Board Design__TDP'].astype(str).str.replace('W', ''), errors='coerce')
df['updated clock speeds'] = pd.to_numeric(df['Clock Speeds__GPU Clock'].astype(str), errors='coerce')
x = df['updated clock speeds']
y = df['TDP_Numeric']

plt.scatter(x,y,s=13,alpha=0.5)

#Extreme outliers were excluded from the visualization to improve readability
plt.xlim(0,1250)
plt.ylim(0,450)
plt.title("Clock Speed vs TDP")
plt.xlabel('Clock Speed (MHZ)')
plt.ylabel('TDP (W)')
plt.show()

#VRAM vs TDP scatter plot

#df['Top__MEMORY SIZE']=pd.to_numeric(df['Top__MEMORY SIZE'].astype(str),errors='coerce')

x = df['TDP_Numeric']
y=  df1['Top__MEMORY SIZE']

plt.scatter(x,y,s=13,alpha=0.5)
plt.title("VRAM vs Power Consumption (TDP): Memory Scaling Trade-offs")
plt.xlim(0,1500)
plt.ylabel('VRAM (GB)')
plt.xlabel('TDP (W)')
plt.show()

