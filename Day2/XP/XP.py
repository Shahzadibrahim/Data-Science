import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split


#1.
#categorical features
#Answer: represent types of data which may be divided into groups and can only take on a limited number of possible values.
#ordinal:invloves some order and the values are related to each other in some way, for example a movie review can have 'Good','Bad','Poor'
#nominal: assigns names to clumns without any specific order.a certain name is not greater than another
#continuous features.
#Continuous variables are numeric variables that have an infinite number of values between any two values.
#A continuous variable can be numeric or date/time. For example, the length of a part or the date and time a payment is received.
# scaling:
# Min-Max Normalization - Scales all the data between [0, 1] as a default but you can pick any 2 numbers to scale between.
#
# Standarization - Standard scaling subtracts the mean and divides by the standard deviation.
# This centers the feature on zero with unit variance.
#
# Transformation:
# If we have skewed data, and we want the data to be in a more normal distribution we can use data transformations. The most common one is log transformations.
#
# Binning:
# we can bine a numerical column of a database into a range of two numbers.

url='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)
# print(titanic_df.head())

# print(titanic_df.Parch.value_counts())

# print(titanic_df.describe())

# print(titanic_df.columns)

# titanic_df['Age'].hist()
# plt.title('Age distribution')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()


# print(titanic_df.groupby(["Survived"]).Age.mean())

# titanic_df[titanic_df['Survived']==1]['Age'].hist()
# plt.show()

# print(titanic_df.Embarked.value_counts())

# titanic_df=pd.get_dummies(titanic_df, columns=['Embarked'])
# print(titanic_df)

# titanic_df['Sex'].unique()
# encoded_dict={"male":0,"female":1}
# titanic_df["Sex"]=titanic_df["Sex"].map(encoded_dict)
# print(titanic_df)

# titanic_df = titanic_df.drop(['Name','Ticket','Cabin','Fare'], axis=1)
# print(titanic_df.head(200))

# titanic_df=titanic_df.dropna()
# print(titanic_df)

# mm_scaler = MinMaxScaler()
# age_scaled =mm_scaler.fit_transform(titanic_df['Age'].values.reshape(-1,1))
# titanic_df['age_scaled'] = age_scaled
# titanic_df[['Age', 'age_scaled']].head()
#
# titanic_df['age_scaled'].hist()
# plt.title('Age distribution')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()

# print(titanic_df.Age.value_counts())

# titanic_df=titanic_df.loc[(titanic_df.Age)<70]
# print(titanic_df)

# X=titanic_df[['Age','Sex']]
# y = titanic_df['Survived']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# print(X_test)
# print(y_test)