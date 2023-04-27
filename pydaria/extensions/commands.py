from pydaria.extensions.database import db


def init_app(app):
    @app.cli.command()
    def createdb():
        """Creates database"""
        db.create_all()
