load "mysqllib.ring"

con = mysql_init()

if mysql_connect( con , "localhost" , "mahmoud18","" ) = 0
    see "what is this bro?"
    bye
ok

data = "create database newhey"

see mysql_query(con,data)
mysql_close(con)
