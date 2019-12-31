import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_csv("Popular_Baby_Names.csv")



# print(df.columns)
# print(df.head())

# print(df["Child's First Name"].head())

# df = df.groupby("Child's First Name")
# x = df['Year of Birth']
# plt.bar(x, y)
# plt.show()

# print(df[["Child's First Name", 'Count']].head())

# x = df["Child's First Name"]
# y = df['Count']
# plt.scatter(x,y)
# plt.show()

# print(df.head())

# df_Otto = df.get_group('Otto')
# print(df_Otto.head())


for df in [i for i in df.groupby("Child's First Name") if i[1]['Count'].mean() > 175]:
	plt.scatter(x=df[1]['Year of Birth'], y=df[1]['Count'], label=df[0])
	plt.legend(loc=1)



plt.show()

# test for the for loop
# **********************************************
# list_name = []
# for i in df.groupby("Child's First Name"):
# 	print(i[1]['Count'].mean())


# Uncomment this if the for loop doesn't work
# ***********************************************
# df_Otto = get_df_by_name('Otto', df, "Child's First Name")
# df_Geraldine = get_df_by_name('GERALDINE', df, "Child's First Name")
# df_Gianna = get_df_by_name('GIANNA', df, "Child's First Name")

# plt.scatter(x=df_Gianna['Year of Birth'], y = df_Gianna['Count'])
# plt.scatter(x=df_Geraldine['Year of Birth'], y = df_Geraldine['Count'])
# plt.scatter(x=df_Otto['Year of Birth'], y=df_Otto['Count'])
# plt.show()
# ************************************************