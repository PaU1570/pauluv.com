import functools
import frontmatter
import markdown2
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, current_app
)

from markupsafe import escape

bp = Blueprint('blog', __name__, url_prefix='/blog')

def load_post(post_category, post_title):
    abs_path = current_app.root_path
    with open('{0}/content/{1}/{2}/{2}.md'.format(abs_path, escape(post_category), escape(post_title)), 'r') as file:
        post = frontmatter.load(file)

    # replace relative image paths with correct paths
    fig_path = '/content/{}/{}/'.format(escape(post_category), escape(post_title))
    post_content = post.content.replace('<img src="', f'<img class="img-fluid mx-auto d-block" src="{fig_path}')

    post_content_html = markdown2.markdown(post_content)

    return post.metadata, post_content_html

def get_all_posts():
    ''' Returns a list of tuples(category, title, metadata, html_content) with all the posts sorted from most recent to oldest. '''
    content_path = current_app.root_path + '/content'
    posts = []
    for category in os.listdir(content_path):
        if os.path.isdir(os.path.join(content_path, category)):
            for post in os.listdir(os.path.join(content_path, category)):
                if os.path.isdir(os.path.join(content_path, category, post)):
                    metadata, html_content = load_post(category, post)

                    # Extract only the first paragraph
                    start_index = html_content.find('<p>')
                    end_index = html_content.find('</p>')

                    # Extract the first paragraph
                    first_paragraph = html_content[start_index + 3: end_index]
                    posts.append((category, post, metadata, first_paragraph))

    # sort by date
    posts.sort(key = lambda x: x[2]['date'], reverse = True)

    return posts


@bp.route('/')
def index():
    posts = get_all_posts()
    return render_template('blog/blog.html', posts = posts)

@bp.route('/<post_category>/<post_title>')
def show_post(post_category, post_title):
    # Read the .md file content
    post_metadata, post_content_html = load_post(escape(post_category), escape(post_title))
    return render_template('blog/post.html', post_metadata = post_metadata, post_content_html = post_content_html)