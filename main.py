# Import libraries
import mysql_client as client
import datetime
from matplotlib import pyplot as plt
import numpy as np
import array

rows = client.cmd(("SELECT date_created, transactions.name, amount, categories.name, categories.categories_id "
                   "FROM transactions "
                   "JOIN categories ON transactions.categories_id=categories.categories_id "
                   "ORDER BY date_created"), ())

# Creating dataset
categories = ['grocery', 'travel', 'restaurant', 'shopping', 'other']
category_sums = array.array('f', [0.0, 0.0, 0.0, 0.0, 0.0])

for r in rows:
    print(r[0].strftime("%Y-%m-%d") + ": " + r[1] + " - $" + str(r[2]) + " <" + r[3] + ">")
    category_sums[r[4]-1]+=r[2]




# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(category_sums, labels=categories)

# show plot
plt.show()