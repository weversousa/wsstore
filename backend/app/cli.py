from app.database import db
from app.model import User


def init_app(app):
    @app.cli.command('create-tables')
    def create_tables():
        """Cria todas as tabelas."""
        db.create_all()

    @app.cli.command('drop-tables')
    def drop_tables():
        """Deleta todas as tabelas."""
        db.drop_all()
