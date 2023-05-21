import os
import datetime
import json

from flask import Flask, render_template, send_from_directory, g, request, current_app

def load_translation(lang_code):
    lang_file = current_app.root_path + '/static/translations/{}.json'.format(lang_code)
    # Fall back to english as default
    if not os.path.isfile(lang_file):
        lang_file = current_app.root_path + '/static/translations/en.json'

    with open(lang_file) as f:
        translation = json.load(f)

    return translation



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

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

    # Localization
    @app.url_defaults
    def add_language_code(endpoint, values):
        if 'lang_code' in values or not g.lang_code:
            return
        if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
            values['lang_code'] = g.lang_code

    @app.url_value_preprocessor
    def pull_lang_code(endpoint, values):
        g.lang_code = values.pop('lang_code', None)
        if g.lang_code not in ['en', 'es', 'eus']:
            g.lang_code = 'en'
        g.t = load_translation(g.lang_code)

    # Route for the custom "content" folder
    @app.route('/content/<path:filename>')
    def serve_content(filename):
        return send_from_directory('content', filename)

    # Pages
    @app.route('/')
    @app.route('/<lang_code>/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    @app.route('/<lang_code>/about')
    def about():
        now = datetime.datetime.now()
        age = now.year - 2000
        return render_template('about.html', age = age)

    @app.route('/gallery')
    @app.route('/<lang_code>/gallery')
    def gallery():
        return render_template('gallery.html')

    from . import blog
    app.register_blueprint(blog.bp)
    
    return app