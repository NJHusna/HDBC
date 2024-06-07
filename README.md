# Hotel Demand Booking and Cancellation Dashboard 🏨📊

Welcome to the Hotel Demand Booking and Cancellation Dashboard project! This project aims to provide comprehensive insights into hotel booking demand and cancellation trends, helping travelers and hoteliers make informed decisions for data from 2015 to 2017.

### Explore the Live Dashboard

Experience the Hotel Demand Booking and Cancellation Dashboard in action by visiting this [link](https://hdbc.salmonwater-b20202fe.southeastasia.azurecontainerapps.io/).

### Contributors

- **Project Supervisor**: _[JH](https://github.com/jhueilim96)_
- **Data Engineer & Analyst**: _[Husna](https://github.com/njhusna)_

### Purpose

This project serves as a demonstration of the skillset

- Data analysis & dashboard building
- Python and SQL proficiency
- Container application deployment
-  Data Modelling
- Data Transformation
- Data Warehousing using [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)

### Features & Technology

#### Dashboard App
_Interactive Visualization_: Explore a variety of charts and graphs built using **Streamlit** to understand booking and cancellation trends.
_Data Query_: Data is retrieved using a local data warehouse method powered by **DuckDB**, known for its superior performance in analytical data querying on edge devices.
_Container Deployment_: The application is packaged as a container image using **Docker** and deployed with **Azure Container Apps**.

#### Data Engineering
_Data Modelling_: Organizing hotel booking data into structured tables for efficient retrieval.
_Data Transformation_: Employing **dbt** as the transformation framework, including data cleaning, aggregation, and enrichment.
_Data Warehouse_: Utilizing **DuckDB** as the local data warehouse for fast query performance on analytical workloads.
_Medallion Framework_: Following the **Databricks medallion framework** to organize data into multiple layers (raw, bronze, silver, and gold) based on its processing stage and quality.

### Purpose

This project serves as a demonstration of the skillset

- Dimensional Data Modelling
- Data Transformation
- Data Warehousing using [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)

### Key Components

_Dimensional Modelling_: Utilizing **star schemas** to organize sports data into fact tables and dimension tables for effiecient retrieval.

_Data Transformation_: Employing **dbt** as the transformation framework, including data cleaning, aggregating, and enriching data.

_Data Warehouse_: Utilizing **DuckDB** as the local data warehouse for fast query performance on analytical workloads.

_Medallion Framework_: Following the **Databricks medallion framework** to organize data into multiple layers (raw, bronze, silver, and gold) based on its processing stage and quality.

### Requirements

To run the Tennis Analytics Data Warehouse locally, you'll need to have the following dependencies installed:

- Python 3.10
- dbt
- DuckDB
- Other necessary Python libraries (specified in requirements.txt)

You can install the required dependencies by run the following command:
```bash
pip -m pip install -r requirements.txt
```

### Usage
#### Dashboard App
To launch the dashboard, navigate to the project directory and run the following command:

```bash
streamlit run hdbc_streamlit.py
``` 
This will start a local server, and you can access the dashboard through your web browser.

### Data Engineering
The post-transformed database binary file is included as `hdbc.duckdb` for ease of usage. To reload the database from raw datasets, run the following command:

```bash
cd hdbc
dbt run
```

### Acknowledgements

All hotel booking data are credited to:
- Hotel Booking Demand Datasets by Nuno Antonio, Ana Almeida, and Luis Nunes.
- Data cleaning and preparation by Thomas Mock and Antoine Bichat for the #TidyTuesday initiative.

### Contact
For any inquiries or feedback regarding the Hotel Demand Booking and Cancellation Dashboard project, feel free to contact the contributors. We'd love to hear from you!
