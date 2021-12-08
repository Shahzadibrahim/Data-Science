import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# sns.catplot( "Sex", "Age", data=df, kind="box")
# plt.show()

# sns.scatterplot(data=df, x="Sex", y="Age")
# plt.show()

# sns.barplot(data=df, x="Sex", y="Survived")
# plt.show()


# sns.barplot(x="Pclass", y="Age", data=df)
# plt.show()

# sns.set_style("whitegrid")
# sns.lineplot(data=df, x="Age", y="SibSp")
# plt.show()

# sns.histplot(df["Age"], binwidth=0.05)
# plt.show()


# df['Sex'].unique()
# encoded_dict={"male":0,"female":1}
# df["Sex"]=df["Sex"].map(encoded_dict)
# sns.distplot(df['Age'])
# sns.distplot(df['Sex']);
# plt.title("Seaborn distplot")
# plt.show()

