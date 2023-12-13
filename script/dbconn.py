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

# read function to the telecom data
def db_read_table_psycopg(pgconn, table_name):
    sql = f'SELECT * FROM {table_name}'
    df = sqlio.read_sql_query(sql,pgconn)
    return df