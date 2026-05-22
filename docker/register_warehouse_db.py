from superset.app import create_app
from superset import db


def upsert_database() -> None:
    app = create_app()
    with app.app_context():
        from superset.models.core import Database

        database_name = "Weather Warehouse"
        sqlalchemy_uri = "postgresql+psycopg2://db_user:db_password@db:5432/db"

        existing = (
            db.session.query(Database)
            .filter(Database.database_name == database_name)
            .one_or_none()
        )

        if existing is None:
            database = Database(database_name=database_name, sqlalchemy_uri=sqlalchemy_uri)
            database.expose_in_sqllab = True
            database.allow_run_async = False
            database.allow_ctas = True
            database.allow_cvas = True
            database.allow_dml = False
            db.session.add(database)
            action = "created"
        else:
            existing.sqlalchemy_uri = sqlalchemy_uri
            existing.expose_in_sqllab = True
            action = "updated"

        db.session.commit()
        print(f"Superset database connection {action}: {database_name}")


if __name__ == "__main__":
    upsert_database()
