import os

from flask import Flask, render_template, send_from_directory

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Route for the custom "content" folder
    @app.route('/content/<path:filename>')
    def serve_content(filename):
        return send_from_directory('content', filename)

    # home page
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/gallery')
    def gallery():
        return render_template('gallery.html')

    from . import blog
    app.register_blueprint(blog.bp)
    
    return app