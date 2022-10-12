# mysql-selfmanaged-HHA-504
HHA 504 Assignment 5: Flask and DBs - mySQL





# in VM (used GCP)

$ sudo apt-get update  

$ sude apt install mysql-server mysql-client  ### installing mysql-server and mysql-client

$ sudo mysql ### installing mysql  

$ show databases; ### retreiving databases within mysql in VM

$ CREATE USER ‘dba'@'%' IDENTIFIED BY ‘ahi2020’; ### create a new user within the server with username and password (identified by) that grants access in to the server. % is the digital location from where the user can log in/connect from

$ select * from mysql.user;

$ select * from mysql.user \G ### \G provides an organized version of data. the root user can only login from the localhost (connected to the VM physically)

$ select User from mysql.user \G ### it pulls up the list of users to verify the user that was created successfully

$ select User, Host from mysql.user; ## pulls list of users & hosts in a table

$ select User, Host, authentication_string from mysql.user; ## pulls list of users, hosts & authentication string in a table

$ mysql -u dba -p ### checking for authorization access to user. None shown

$ grant all privileges on *.* to 'dba'@'%' with grant option; ### providing the user with all privileges

$ show grants for dba; ### loading grants

$ \q

$ mysql -u dba -p ### password: 'ahi2020' Authorization granted and the user is able to perform queries 


# google collab notebook
1. MYSQL_HOSTNAME = '34.136.63.186' # Insert IP address 
2. MYSQL_USER = 'dba'
3. MYSQL_PASSWORD = 'ahi2022'
4. MYSQL_DATABASE = 'tempdata'
5. connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
6. db = create_engine(connection_string)
7. print(db.table_names())

### create database tempdata;
### in the python file, use the '.read_csv' to read the data file
### upload the datafile to the sql using the '.to_sql' command
