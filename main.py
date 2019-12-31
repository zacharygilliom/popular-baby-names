import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_csv("Popular_Baby_Names.csv")


# some exploratory analysis to see how our data is organized
print(df.columns)
print(df.head())

# Noticed that some of the first names are all caps.
# lets change it to standard typesetting with the first letter capitalized
# This will help with readability
df["Child's First Name"] = df["Child's First Name"].apply(lambda x: x.lower().capitalize())
print(df.head())	

# want to create multiple scatter plots by each child's name
for df in [i for i in df.groupby("Child's First Name") if i[1]['Count'].mean() > 150]:
	plt.scatter(x=df[1]['Year of Birth'], y=df[1]['Count'], label=df[0])
	plt.legend(loc=1)

plt.title('Occurences of baby names by birth year that are averaging greater than 175')
plt.xlabel('Year of Birth')
plt.ylabel('Occurences of name in each year')

plt.show()
