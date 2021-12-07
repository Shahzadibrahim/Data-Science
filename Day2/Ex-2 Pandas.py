import pandas as pd

# 1 ~ 3 - Assign it to a variable called chipo.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
# print(chipo)

# 4- See the first 10 entries
# print(chipo.head(10))

# 5- What is the number of observations in the dataset?
# print(chipo.shape[0])

# 6- What is the number of columns in the dataset?
# print(chipo.shape[1])

# 7- Print the name of all the columns.
# print(chipo.columns)

# 8- How is the dataset indexed?
# print(chipo.index)

# 9- Which was the most ordered item?
# print(chipo.item_name.value_counts().head(1))

# 10- How many items were ordered?
# print(chipo.item_name.unique().shape[0])

# 11- What was the most ordered item in the choice_description column?
# print(chipo.choice_description.value_counts().head())

# 12- How many items were orderd in total?
# print(chipo.quantity.sum())

# 13- Turn the item price into a float
# def num_float(x):
#     return float(x[1:-1])
# chipo.item_price = chipo.item_price.apply(num_float)
# print(chipo.head())

# 14- How much was the revenue for the period in the dataset?
# print(chipo.item_price.sum())

# 15- How many orders were made in the period?
# print(chipo.order_id.value_counts().count())
# print(len(chipo.order_id.value_counts()))
# print(chipo.order_id.value_counts().shape[0])

# 16- What is the average amount per order?
# order_grouped = chipo.groupby(by=['order_id']).sum()
# print(order_grouped['quantity'].mean())
# print(order_grouped)

# 17- How many different items are sold?
# print(chipo.groupby(['item_name'])[['quantity']].sum())
