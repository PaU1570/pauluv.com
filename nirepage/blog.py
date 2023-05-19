import functools
import markdown

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from markupsafe import escape

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/')
def index():
    return render_template('blog/blog.html')


@bp.route('/<post_category>/<post_title>')
def show_post(post_category, post_title):
    # Read the .md file content
    with open('example.md', 'r') as file:
        md_content = file.read()

    return render_template('blog/post.html', category = post_category, title = post_title)