#!/bin/bash

set -e

psql --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER plan_it PASSWORD 'travelers123';
    ALTER USER plan_it CREATEDB;
    CREATE DATABASE travelers_db;
    GRANT ALL PRIVILEGES ON DATABASE travelers_db TO plan_it;
    ALTER DATABASE travelers_db OWNER TO plan_it;
EOSQL
