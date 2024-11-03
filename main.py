import mysql_client as client
import datetime

rows = client.cmd(("SELECT date_created, transactions.name, amount, categories.name "
                   "FROM transactions "
                   "JOIN categories ON transactions.categories_id=categories.categories_id "
                   "ORDER BY date_created"), ())

for r in rows:
    print(r[0].strftime("%Y-%m-%d") + ": " + r[1] + " - $" + str(r[2]) + " <" + r[3] + ">")

