# logAnalysis
Project: Logs Analysis This is the first project of Udacity: Full Stack Web Developer Nanodegree

About the project : create a reporting tool that analyze the logs and prints out reports based on the data in the database for a newspaper site powered by PostgreSQL datebase.

The report should answer the following questions: What are the most popular three articles of all time? Who are the most popular article authors of all time? On which days did more than 1% of requests lead to errors?

Requirements: The code should generate correct answers to the questions The code should generate output in clearly formatted plain text.

Set up the environment: 1/Install Python3 2/Download and install VirtualBox 3/Download and install Vagrant 4/Make sure you have newsdata.sql, the SQL script file with all the data. It can be downloaded from the Udacity course page or from this link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 5/Put the newsdata.sql file into the vagrant directory 6/By Git bash Navigate to the /vagrant directory and run vagrant up to start the virtual machine 7/Run vagrant ssh to log in the virtual machine 8/Run psql -d news -f newsdata.sql on the virtual machine /vagrant folder to create the database 9/The logs reporting tool should saved in /vagrent , it is executed with the following command: python logsAnalysis.py The answers to the three questions should now be displayed.
