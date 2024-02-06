'''Module 5: We will use python and SQL to create and manage a database, perform various SQL operations,
inlcuding joins, filters, and aggregations.

Author: Cole Nollette
Date: 2/6/24
Title: Datafun-05-sql
'''

# Imports
import pandas as pd
import pyarrow
import matplotlib
import pathlib
import logging
import sqlite3
import csv


# Configure Logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program begins")
logging.info("Program finished")

# Database Creation and Schema
'''Database Creation and Schema is defined in repository's README
'''

# Define Functions

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


# Define Main Function
def main():
    db_filepath = 'project.db'

    # Create database Schema and populate
    execute_sql_from_file(db_filepath, 'create_tables.sql')
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregations.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operatoins completed successfully")

    # Conditional Script

    if __name__== '__main__':
        main()