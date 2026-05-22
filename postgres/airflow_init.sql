-- Create airflow database and user
CREATE DATABASE airflow_db;
CREATE USER airflow WITH PASSWORD 'airflow';
ALTER ROLE airflow SET client_encoding TO 'utf8';
ALTER ROLE airflow SET default_transaction_isolation TO 'read committed';
ALTER ROLE airflow SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow;
\connect airflow_db;
GRANT ALL ON SCHEMA public TO airflow;
