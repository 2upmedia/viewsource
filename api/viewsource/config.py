from flask import Flask
import os

PRODUCTION = 'production'
DEVELOPMENT = 'development'


class BaseConfig(object):
    JSONIFY_MIMETYPE = 'application/vnd.api+json'


class Production(BaseConfig):
    DEBUG = False

CONFIG_MAPPING = {
    PRODUCTION: 'viewsource.config.Production',
    DEVELOPMENT: 'viewsource.localconfig.Development'
}


def configure_app(app: Flask):
    app.config.from_object(CONFIG_MAPPING[os.environ.get('APP_ENV', DEVELOPMENT)])
