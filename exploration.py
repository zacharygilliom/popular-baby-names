import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set(style='darkgrid')

df = pd.read_csv("Popular_Baby_Names.csv")

def get_gender_summaries(df, gender):
	df = df[df['Gender'] == gender]
	un_vals = len(df["Child's First Name"].unique())
	tot_vals = len(df)
	print('Unique names for ' + gender + 's')
	print(un_vals)
	print('Total names for ' + gender + 's')
	print(tot_vals)
	print('Percent of unique names')
	print(str(int((un_vals / tot_vals) * 100)) + '%')
	return None

def get_ethnicity_summaries(df,eth):
	df = df[df['Ethnicity'] == eth]
	un_vals = len(df["Child's First Name"].unique())
	tot_vals = len(df)
	print('Unique names for ' + eth + 's')
	print(un_vals)
	print('Total names for ' + eth + 's')
	print(tot_vals)
	print('Percent of unique names')
	print(str(int((un_vals / tot_vals) * 100)) + '%')
	return None


# print(df.head())


df["Child's First Name"] = df["Child's First Name"].apply(lambda x: x.lower().capitalize())
df['Gender'] = df['Gender'].apply(lambda x: x.lower().capitalize())
df['Ethnicity'] = df['Ethnicity'].apply(lambda x: x.lower().capitalize())


for index, row in df.iterrows():
	if df.loc[index, 'Ethnicity'] == 'Black non hisp':
		df.loc[index, 'Ethnicity'] = 'Black non hispanic'
	elif df.loc[index, 'Ethnicity'] == 'Asian and paci':
		df.loc[index, 'Ethnicity'] = 'Asian and pacific islander'
	elif df.loc[index, 'Ethnicity'] == 'White non hisp':
		df.loc[index, 'Ethnicity'] = 'White non hispanic'
	

# print(len(df['Ethnicity'].unique()))

for e in df['Ethnicity'].unique():
	print('\n')
	get_ethnicity_summaries(df,e)

print('\n')
get_gender_summaries(df, 'Male')
print('\n')
get_gender_summaries(df,'Female')


fig, axs = plt.subplots(nrows=2)
sns.boxenplot(x='Ethnicity',
			y='Count',
			hue='Gender',
			data=df,
			ax = axs[0],
			palette='Set3'
			)

sns.violinplot(x='Count',
			y='Ethnicity',
			hue='Gender',
			split=True,
			data=df,
			ax=axs[1],
			palette='Set3'
			)


plt.show()

