import mysql_client as client
import random
import datetime

nameOptions = ["Walmart", "Smiths", "AutoZone", "Walmart Fuel Station", "Smiths Fuel Station", "Taco Bell", "McDonalds", "Apple Store"]
valuesList = [
    (nameOptions[0], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[0], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[0], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[0], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[0], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[0], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),

    (nameOptions[1], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[1], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[1], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[1], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),
    (nameOptions[1], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 1),

    (nameOptions[2], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 5),
    (nameOptions[2], round(random.uniform(25, 150), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 5),

    (nameOptions[3], round(random.uniform(25, 65), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 2),
    (nameOptions[3], round(random.uniform(25, 65), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 2),
    (nameOptions[4], round(random.uniform(25, 65), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 2),

    (nameOptions[5], round(random.uniform(3, 25), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 3),
    (nameOptions[6], round(random.uniform(3, 25), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 3),

    (nameOptions[7], round(random.uniform(0.99, 20), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 4),
    (nameOptions[7], round(random.uniform(0.99, 20), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 4),
    (nameOptions[7], round(random.uniform(0.99, 20), 2), 1, datetime.date(2024, random.randint(1,12), random.randint(1,28)), 4)
              ]


add_transaction = ("INSERT INTO transactions "
                   "(name, amount, user_id, date_created, categories_id) "
                   "VALUES (%s, %s, %s, %s, %s)")

for i in valuesList:
    client.cmd(add_transaction, i, client.CmdType.INSERT)