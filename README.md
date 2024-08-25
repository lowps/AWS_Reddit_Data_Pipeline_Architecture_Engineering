# AWS_Reddit_Data_Pipeline_Architecture_Engineering

# Project Overview
This project offers a robust data pipeline for extracting, transforming, and loading (ETL) Reddit data into an Amazon Redshift data warehouse. It utilizes a suite of tools and services such as Docker, Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift to efficiently manage and process the data.

# Overview
The pipeline is designed to:

1. Extract data from Reddit using its API.
2. Store the raw data into an S3 bucket from Airflow.
3. Transform the data using AWS Glue and Amazon Athena.
4. Load the transformed data into Amazon Redshift for analytics and querying.

# Architecture
1. Reddit API: Source of the data.
2. Apache Airflow & Celery: Orchestrates the ETL process and manages task distribution.
4. PostgreSQL: Temporary storage and metadata management.
5. Amazon S3: Raw data storage.
6. AWS Glue: Data cataloging and ETL jobs.
7. Amazon Athena: SQL-based data transformation.
8. Amazon Redshift: Data warehousing and analytics.

## License
This project is licensed under the MIT License. See the [LICENSE]/(LICENSE) file for details.
