#!/bin/bash

set -e

psql --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER plan_it PASSWORD 'travelers123';
    ALTER USER plan_it CREATEDB;
    CREATE DATABASE web_scraper_db;
    GRANT ALL PRIVILEGES ON DATABASE web_scraper_db TO plan_it;
    ALTER DATABASE web_scraper_db OWNER TO plan_it;
EOSQL
#psql --username "$POSTGRES_USER" <<-EOSQL
#    CREATE USER web_scraper_app PASSWORD 'postgres';
#    CREATE USER web_scraper_app PASSWORD 'postgres';
#    ALTER USER web_scraper_app CREATEDB;
#    CREATE DATABASE web_scraper_db;
#    GRANT ALL PRIVILEGES ON DATABASE web_scraper_db TO web_scraper_db;
#    ALTER DATABASE web_scraper_db OWNER TO web_scraper_db;
#EOSQL
