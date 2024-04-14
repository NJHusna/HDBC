# %%
import os
import glob
import pandas as pd
import duckdb
from IPython.display import display
# %%
# Initialized duckdb database
conn = duckdb.connect()
# %%
# https://duckdb.org/docs/sql/statements/create_table
# Specify the path containing CSV files
path = 'Dataset/'
# Retrieve the list of CSV files in the path using glob
csv_files = glob.glob(path + '*.csv')
# "Basename --> refers to the name of a file or directory without its directory path
# store DataFrames using Dictionary
dfs = {}
for file_path in csv_files:
    table = os.path.basename(file_path).split('.')[0]
    df = pd.read_csv(file_path) # Read data from CSV file into DataFrame
    dfs[table] = df
    
# %%
# Create Tables for Dataframes
for table, df in dfs.items():
    conn.register(table, df) # Register df as table
    conn.execute(f"CREATE TABLE {table} AS SELECT * FROM {table}").df() # query to create table
    print(f"DataFrame for {table}:")
    display(df)

# %%
# Check the Datatype
for table, df in dfs.items():
    description = conn.execute(f"DESCRIBE {table}").df()
    print(f"Description for DataFrame '{table}':")
    display(description)


# %%
# Create View to read the file
for file_path in csv_files:
    df = conn.execute(f"SELECT * FROM read_csv('{file_path}', header=True)").df()
    print(f"Table: {table}")
    display(df)

# %%
# create a temporary table from a CSV file
# for file_path in csv_files:
#     df = conn.execute(f"CREATE TEMP TABLE {table} AS SELECT * FROM read_csv('{file_path}', header=True)").df()
#     print(f"Table: {table}")
#     display(df)

# conn.execute("SET temp_directory = '/path/to/directory/'")

# %%
for table, df in dfs.items():
    conn.execute(f"COPY (SELECT * FROM {table}) TO '{table}.parquet'")

# %%
for table, df in dfs.items():
    conn.execute(f"COPY (SELECT * FROM '{table}.parquet') TO '{table}'")

# %%

# Define the new folder path
new_folder_path = 'Copy of Datasets/'

# Create the new folder if it doesn't exist
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Copy tables to Parquet files
for table, df in dfs.items():
    parquet_file_path = os.path.join(new_folder_path, f"{table}.parquet")
    conn.execute(f"COPY (SELECT * FROM {table}) TO '{parquet_file_path}'")
# %%
# Copy Parquet files back to tables
for table, df in dfs.items():
    parquet_file_path = os.path.join(new_folder_path, f"{table}.parquet")
    conn.execute(f"COPY (SELECT * FROM '{parquet_file_path}') TO '{new_folder_path}{table}'")

# %%
