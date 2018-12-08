# !/usr/bin/env python3
import psycopg2
# DataBase command for 3 quieries
# 1.What are the most popular three articles of all time?
report1 = """SELECT articles.title,count(*)
  FROM log , articles
  WHERE log.path=concat('/article/',articles.slug)
  GROUP BY articles.title
  ORDER BY count(*) DESC LIMIT 3 ; """
# 2.Who are the most popular article authors of all time?
report2 = """ SELECT authors.name, count(*)
  FROM articles , authors , log
  WHERE authors.id = articles.author
  AND log.path = concat('/article/', articles.slug)
  GROUP BY authors.name
  ORDER BY count(*) DESC ; """
# 3. On which days did more than 1% of requests lead to errors?
# use WITH clause reference
# [https://www.postgresql.org/docs/9.1/queries-with.html]
report3 = """ WITH total_stat AS (SELECT time::date AS datte ,status
FROM log), error_total AS (SELECT datte, count(*)
FROM total_stat
WHERE total_stat.status != '200 OK'
GROUP BY datte
ORDER BY datte), logs_total AS (SELECT datte, count(*)
FROM total_stat
GROUP BY datte
ORDER BY datte), error_calc AS (SELECT logs_total.datte,
       error_total.count::float / logs_total.count::float * 100 AS calc_result
FROM error_total,
     logs_total
WHERE error_total.datte = logs_total.datte)
select * from error_calc where calc_result > 1;
"""

# display the popular articles


def articles():
    articles = base_Q(report1)
    print('<<<<<<<<<<<<<>>>>>>>>>>>>>>')
    print('**** The most popular three articles of all time is : ****')
    print('<<<<<<<<<<<<<>>>>>>>>>>>>>>')
    for i in articles:
        print('"{article}" - {count} views'.format(article=i[0], count=i[1]))


# display the popular authors
def authors():
    authors = base_Q(report2)
    print('<<<<<<<<<<<<<>>>>>>>>>>>>>>')
    print('**** The most popular article authors of all time : ****')
    print('<<<<<<<<<<<<<>>>>>>>>>>>>>>')
    for i in authors:
        print('{author} - {count} views'.format(author=i[0], count=i[1]))


# display the days with error more than 1%
def logss():
    logss = base_Q(report3)
    print('<<<<<<<<<<<<<>>>>>>>>>>>>>>')
    print('**** Days with more than 1% of error requests ****')
    print('<<<<<<<<<<<<<>>>>>>>>>>>>>>')
    for i in logss:
        print('{logs:%B %e, %Y} - {error_cal:.1f}% errors'.format(
          logs=i[0], error_cal=i[1]))

# reference partial Quote
# [https://github.com/lauwrentius/Logs-Analysis/blob/master/reporting.py]
# connect to the DB


def base_Q(Query):
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(Query)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    articles()
    authors()
    logss()
