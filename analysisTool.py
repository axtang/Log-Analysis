import psycopg2
import time
import sys


def connect():
    return psycopg2.connect("dbname=news")

query1 = "select title, views from view_articles limit 3"
query2 = "select name, total_popularity from author_popularity"
query3 = "select to_char(date, 'YYY-MON-DD') as date, \
error_rate from error_days where error_rate > 1.0"

# 1. What are the most popular three articles of all time?
# Present this information as a sorted list with the most
# popular article at the top
# Listing "author" because it will be helpful for the second
# question.


def popular3Articles(query1):
    db = connect()
    c = db.cursor()
    c.execute(query1)
    output = c.fetchall()
    for i in range(len(output)):
        title = output[i][0]
        views = output[i][1]
        print ("%s, %d" % (title, views))
    db.close()


# 2. Who are the most popular article authors of all time?
# Sum up all of the articles each author has written, which
# authors get the most page views?
# Present this as a sorted list with the most popular author
# at the top


def popularAuthors(query2):
    db = connect()
    c = db.cursor()
    c.execute(query2)
    output = c.fetchall()
    for i in range(len(output)):
        name = output[i][0]
        total_popularity = output[i][1]
        print("%s, %d" % (name, total_popularity))
    db.close()


# 3. On which day did more than 1% of requests lead to errors?


def errorDays(query3):
    db = connect()
    c = db.cursor()
    c.execute(query3)
    output = c.fetchall()
    for i in range(len(output)):
        date = output[i][0]
        error_rate = output[i][1]
        print("%s,%d" % (date, error_rate))
    db.close()


if __name__ == "__main__":
    with open('LAOutput.txt', 'w') as f:
        sys.stdout = f
        print('These 3 articles have been accessed the most:', file=f)
        popular3Articles(query1)

        print('From the most popular to the least popular authors:', file=f)
        popularAuthors(query2)

        print('On this date more than 1% of requests lead to errors:', file=f)
        errorDays(query3)


def connect():
    return psycopg2.connect('dbname=news')

# 1. What are the most popular three articles of all time?
# Present this information as a sorted list with the most popular
# article at the top
# Listing "author" because it will be helpful for the second question.


query1 = "select * from view_articles limit 3"


def popular3Articles():
    db = connect()
    c = db.cursor()
    c.execute(query1)
    c.fetchall()
    db.close()


# 2. Who are the most popular article authors of all time?
# Sum up all of the articles each author has written, which authors get
# the most page views?
# Present this as a sorted list with the most popular author at the top


query2 = "select * from author_popularity"


def popularAuthors():
    db = connect()
    c = db.cursor()
    c.execute(query2)
    c.fetchall()
    db.close()


# 3. On which day did more than 1% of requests lead to errors?


query3 = "select * from error_rates limit 1"


def errorDays():
    db = connect()
    c = db.cursor()
    c.execute(query3)
    c.fetchall()
    db.close()


if __name__ == "__main__":
    print('These 3 articles have been accessed the most:')
    popular3Articles()

    print('From the most popular to the least popular authors:')
    popularAuthors()

    print('On this date more than 1% of requests lead to errors:')
    errorDays()
