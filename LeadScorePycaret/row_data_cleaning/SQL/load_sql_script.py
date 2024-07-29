'''
Upload the new leads data to postgresql database using psycopg2 and pandas

'''

import pandas as pd
import numpy as np
import psycopg2

# read the excel file and convert it to a dataframe

df = pd.read_excel('C:/Users/marce/Desktop/Python/pythoncheatsheets/python_projects/Lead_scoring/data_powerBI/new_leads_BI.xlsx')



# connect to the database

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'Leads',
    user = 'postgres',
    password = 'LXXXX',
    port = '5432')

# save the dataframe to the database

# Create a cursor object
cur = conn.cursor()

# Generate the SQL statement to insert the data

table_name = 'new_leads'
cols = []
for col, dtype in zip(df.columns, df.dtypes):
    if dtype == 'int64':
        cols.append(f'{col} INTEGER')
    elif dtype == 'float64':
        cols.append(f'{col} FLOAT')
    else:
        cols.append(f'{col} VARCHAR(255)')
cols = ', '.join(cols)

placeholders = ', '.join(['%s'] * len(df.columns))

create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})"
insert_data = f"INSERT INTO {table_name} VALUES ({placeholders})"

# Execute the SQL statements
cur.execute(create_table)
for i, row in df.iterrows():
    cur.execute(insert_data, tuple(row))
    
# Commit the changes and close the cursor
conn.commit()
cur.close()

# Close the connection
conn.close()



