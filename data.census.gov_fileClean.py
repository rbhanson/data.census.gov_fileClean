import pandas as pd

#read csv file drop first row
df = pd.read_csv('data/ACSDP5Y2019.DP05_data_with_overlays_2021-07-26T175211.csv')
df.drop(0, axis=0, inplace=True)

#select the fields you desire
df = df[['GEO_ID','NAME', 'DP05_0001E']]

#split GEOID feild to extract the FIPS Code
df[['US','geoJoiner']]=df['GEO_ID'].str.split('S', 1, expand=True)

del df['US']

#Assign the value to float to be mapped
df['DP05_0001E'] = df['DP05_0001E'].astype(float)

df.to_excel (r'data/cleaned.xlsx', index = None, header=True)





