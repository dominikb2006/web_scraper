
set -e

psql --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER plan_it PASSWORD 'riders123';
    ALTER USER plan_it CREATEDB;
    CREATE DATABASE riders_db;
    GRANT ALL PRIVILEGES ON DATABASE riders_db TO plan_it;
    ALTER DATABASE riders_db OWNER TO plan_it;
EOSQL
