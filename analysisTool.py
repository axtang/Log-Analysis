import psycopg2
import datetime


def connect():
    return psycopg2.connect('dbname=news')

# 1. What are the most popular three articles of all time?
# Present this information as a sorted list with the most popular article at the top
# Listing "author" because it will be helpful for the second question.

query1="select * from view_articles limit 3"

def popular3Articles():
    db = connect()
    c = db.cursor()
    c.execute(query1)
    c.fetchall()
    db.close()
    

# 2. Who are the most popular article authors of all time?
# Sum up all of the articles each author has written, which authors get the most page views?
# Present this as a sorted list with the most popular author at the top

query2="select * from author_popularity"

def popularAuthors():
    db = connect()
    c = db.cursor()
    c.execute(query2)
    c.fetchall()
    db.close()


# 3. On which day did more than 1% of requests lead to errors?

query3="select * from error_rates limit 1"

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

