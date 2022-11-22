from alchemical.flask import Alchemical
from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from apifairy import APIFairy

from config import Config


db = Alchemical()
migrate = Migrate()
ma = Marshmallow()
apifairy = APIFairy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # extensões
    from api import models
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    apifairy.init_app(app)

    # blueprints
    from api.fake import fake
    app.register_blueprint(fake)

    from api.vias import vias
    app.register_blueprint(vias, url_prefix='/api')   

    @app.shell_context_processor
    def shell_context():  # pragma: no cover
        ctx = {'db': db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, '__bases__') and \
                    db.Model in getattr(model, '__bases__'):
                ctx[attr] = model
        return ctx

    @app.route('/')
    def index():
        return redirect(url_for('apifairy.docs'))

    return app
