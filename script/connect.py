import pandas.io.sql as sqlio
import pandas as pd
import psycopg2
from psycopg2 import sql

def db_connection_psycopg():
    pgconn = psycopg2.connect(dbname="telecom",
                              user= "postgres",
                              password= "Newsnow@1991",
                              host="localhost",
                              port="5432")
    return pgconn