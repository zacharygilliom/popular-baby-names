import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Chose to use seaborn over matplotlib as it provides more customization
sns.set(style='darkgrid')

df = pd.read_csv("Popular_Baby_Names.csv")


# some exploratory analysis to see how our data is organized
# print(df.columns)
# print(df.head())

# Noticed that some of the first names are all caps.
# lets change it to standard typesetting with the first letter capitalized
# This will help with readability
df["Child's First Name"] = df["Child's First Name"].apply(lambda x: x.lower().capitalize())
print(df.head())	

# want to create multiple scatter plots by each child's name
for df in [i for i in df.groupby("Child's First Name") if i[1]['Rank'].mean() < 11]:
	sns.lineplot(x=df[1]['Year of Birth'], 
			 	y=df[1]['Count'],
			 	label=df[0],
			 	err_style=None,
			 	markers=True,
			 	)
	plt.legend(loc=1)

plt.title('Rank of baby names by birth year that average in the top 10')
plt.xlabel('Year of Birth')
plt.ylabel('Occurences of name in each year')

plt.show()
