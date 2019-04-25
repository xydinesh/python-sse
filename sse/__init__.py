from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # existing code omitted
    from . import server
    app.register_blueprint(server.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/datetime', endpoint='sse_datetime')

    return app
