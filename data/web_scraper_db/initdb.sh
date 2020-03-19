#!/bin/bash

set -e

psql --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER plan_it PASSWORD 'travelers123';
    ALTER USER plan_it CREATEDB;
    CREATE DATABASE web_scraper_db;
    GRANT ALL PRIVILEGES ON DATABASE web_scraper_db TO plan_it;
    ALTER DATABASE web_scraper_db OWNER TO plan_it;
EOSQL
