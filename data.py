import pandas as pd
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')

data1 = data1[['DATE_TIME', 'DC_POWER', 'AC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD']]
data2['DATE_TIME'] = data2['DATE_TIME'].apply(lambda x: x[8:10] + '-' + x[5:7] + '-' + x[0:4] + ' ' + x[11:16])

data = {}

for i in range(len(data1)):
  data[data1.iloc[i]['DATE_TIME']] = {'DC_POWER': 0, 'AC_POWER': 0, 'DAILY_YIELD': 0}

dc, ac = 0, 0
for i in range(len(data1)):
  if i > 0 and data1.iloc[i - 1]['DATE_TIME'][:10] != data1.iloc[i]['DATE_TIME'][:10]:
    dc, ac = 0, 0
  data[data1.iloc[i]['DATE_TIME']]['DC_POWER'] += data1.iloc[i]['DC_POWER']
  data[data1.iloc[i]['DATE_TIME']]['AC_POWER'] += data1.iloc[i]['AC_POWER']
  dc += data1.iloc[i]['DC_POWER']
  ac += data1.iloc[i]['AC_POWER']
  data[data1.iloc[i]['DATE_TIME']]['ACCU_DC_POWER'] = dc
  data[data1.iloc[i]['DATE_TIME']]['ACCU_AC_POWER'] = ac
  data[data1.iloc[i]['DATE_TIME']]['DAILY_YIELD'] += data1.iloc[i]['DAILY_YIELD']
for i in range(len(data2)):
  if data2.iloc[i]['DATE_TIME'] not in data: continue
  data[data2.iloc[i]['DATE_TIME']]['AMBIENT_TEMPERATURE'] = data2.iloc[i]['AMBIENT_TEMPERATURE']
  data[data2.iloc[i]['DATE_TIME']]['MODULE_TEMPERATURE'] = data2.iloc[i]['MODULE_TEMPERATURE']
  data[data2.iloc[i]['DATE_TIME']]['IRRADIATION'] = data2.iloc[i]['IRRADIATION']

df = pd.DataFrame(data).transpose()

df.to_csv('data.csv')

print(df)