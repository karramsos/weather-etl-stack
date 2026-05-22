DO $$
BEGIN
	IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'superset') THEN
		CREATE ROLE superset LOGIN PASSWORD 'superset';
	END IF;
END
$$;

SELECT 'CREATE DATABASE superset_db OWNER superset'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'superset_db')\gexec
