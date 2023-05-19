import functools
import frontmatter
import markdown2

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, current_app
)

from markupsafe import escape

bp = Blueprint('blog', __name__, url_prefix='/blog')

# Route for the custom "content" folder
@bp.route('/content/<path:filename>')
def post_image(filename):
    return send_from_directory('content', filename)


@bp.route('/')
def index():
    return render_template('blog/blog.html')


@bp.route('/<post_category>/<post_title>')
def show_post(post_category, post_title):
    # Read the .md file content
    abs_path = current_app.root_path
    with open('{0}/content/{1}/{2}/{2}.md'.format(abs_path, escape(post_category), escape(post_title)), 'r') as file:
        post = frontmatter.load(file)

    # replace relative image paths with correct paths
    fig_path = '/content/{}/{}/'.format(escape(post_category), escape(post_title))
    post_content = post.content.replace('<img src="', f'<img class="img-fluid mx-auto d-block" src="{fig_path}')

    post_content_html = markdown2.markdown(post_content)
    return render_template('blog/post.html', post_metadata = post.metadata, post_content_html = post_content_html)