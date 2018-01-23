# Log Analysis - Tool building

This is a Udacity project.

This project is intend to build a SQL reporting tool that summarizes articles, authors, and log data from a large news database.


## Preparations

(Preferrably you want to run run this tool in a virtual environment inside of your local machine. The list below shows you, first, how to install a virtual machine into your local machine, and secondly, how to install the tool inside this virtual machine.)

1. Download and install the VirtualBox package (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
2. Download and install Vagrant (https://www.vagrantup.com/downloads.html). 
3.Download/clone the database data from Udacity's GitHub account (https://github.com/udacity/fullstack-nanodegree-vm) into your Vagrant file. Don't forget to unzip the file after download is completed.

## How to run this tool

1. To bring the virtual machine online, on your terminal, go to the file location where Vagrant was installed at and type in **vagrant up** then log into it with **vagrant ssh**. To check the version, run **vagrant --version**.
2. Then, **cd /vagrant**.
3. To load the news databse into your virtual machine, **psql -d news -f newsdata.sql**.
4. To explore the database, use the following commands: 
-**-d news** to connect to the database named "news"
-**-f newsdata.sql**
-**\dt** to check out the tables
-**\dv** to check out the views
-**\q** to exit the table or the database
<br>
5. (error) If you encounter an error message in the command line, such as "psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused", it means the database server is not set up/ run correctly. It can also happen when an older version of the VM configuration exists on your directory. Simply fix this by downloading the VM configuration into a new directory and restart from the 3rd step of the Preparation process.

## To create views with psql commands (don't forget the ";"!)
In SQL, a view is a virtual table based on the result_set of an SQL statement.
Copy, paste, and run the following views onto the command line once logged into the news database.
#### Question: What are the most popular 3 articles of all time? -- view_articles
```CREATE VIEW view_articles AS
SELECT author, title, count(slug) AS VIEWS
FROM articles, log
WHERE log.path like ('%', articles.slug)
GROUP BY articles.title, articles.author
ORDER BY views DESC;```
<br>

#### Question: Who are the most popular article authors of all time? -- author_popularity
```CREATE VIEW author_popularity AS
SELECT name, sum(view_articles.views) AS total_popularity
FROM authors, view_articles
WHERE view_articles.author = authors.id
GROUP BY authors.name
ORDER BY total_popularity DESC;```
<br>

#### Question: On which day did more than 1% of requests lead to errors?
```CREATE VIEW error_days AS
SELECT date(time), concat(round(100*(case log.status WHEN '200 OK' then 0 else 1 end)/count(*), 2), " %") as error_rate
FROM log
GROUP BY date(time)
ORDER BY error_rate DESC;```