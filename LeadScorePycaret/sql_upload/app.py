# visualize the new_leads data from postgres database into streamlit

import streamlit as st
import pandas as pd
import numpy as np
import psycopg2


# Connect to postgres database

conn = psycopg2.connect(
    host="localhost",
    database="Leads",
    user = "postgres",
    password = "Lorenzo_22",
    port = "5432"
)

# Create a cursor object

cur = conn.cursor()

# Execute a query

cur.execute("SELECT * FROM new_leads LIMIT 20")

# Fetch all the records
results = cur.fetchall()
column_names = [desc[0] for desc in cur.description]

df = pd.DataFrame(results, columns=column_names)


# Close the cursor and connection to so the server can allocate

cur.close()



