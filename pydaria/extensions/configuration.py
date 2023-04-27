from importlib import import_module
from dynaconf import FlaskDynaconf


def load_extensions(app):
    for extension in app.config.get('EXTENSIONS'):
        module = import_module(extension)
        module.init_app(app)


def init_app(app):
    FlaskDynaconf(app)
