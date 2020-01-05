import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set(style='darkgrid')

df = pd.read_csv("Popular_Baby_Names.csv")

df["Child's First Name"] = df["Child's First Name"].apply(lambda x: x.lower().capitalize())

# for df in [i for i in df.groupby('Gender',"Child's First Name") if i[1]['Rank'].mean() < 12]:
# 	sns.lineplot(x=df[1]['Year of Birth'], 
# 			 	y=df[1]['Count'],
# 			 	label=df[0],
# 			 	err_style=None,
# 			 	markers=True,
# 			 	)
# 	plt.legend(loc=1)

df_grouped = df.groupby(['Gender', "Child's First Name"])
for df in df_grouped:
	print(df)

# print(df_grouped)

# plt.title('Rank of baby names by birth year that average in the top 10')
# plt.xlabel('Year of Birth')
# plt.ylabel('Occurences of name in each year')

# plt.show()