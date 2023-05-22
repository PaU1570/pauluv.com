import functools
import frontmatter
import markdown2
import os
import math

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from markupsafe import escape

from . import get_paths
PATHS = get_paths()

bp = Blueprint('blog', __name__, url_prefix='/<lang_code>/blog')

def load_post(post_category, post_title):
    post_path = '{0}/{1}/{2}'.format(PATHS['CONTENT_PATH'], escape(post_category), escape(post_title))
    matches = []
    available_in_lang = True
    for file in os.listdir(post_path):
        if file.endswith('_{}.md'.format(g.lang_code)):
            matches.append(os.path.join(post_path, file))

    # fall back to english
    if len(matches) == 0:
        available_in_lang = False
        for file in os.listdir(post_path):
            if file.endswith('_en.md'):
                matches.append(os.path.join(post_path, file))

    # there should only be one md file per languge per post
    filename = matches[0]

    with open(filename, 'r') as file:
        post = frontmatter.load(file)

    # replace relative image paths with correct paths
    fig_path = url_for('serve_content', filename='{}/{}'.format(escape(post_category), escape(post_title)))
    post_content = post.content.replace('<img src="', f'<img class="img-fluid mx-auto d-block" src="{fig_path}/')

    post_content_html = markdown2.markdown(post_content)

    return post.metadata, post_content_html, available_in_lang

def get_all_posts():
    ''' Returns a list of tuples(category, title, metadata, html_content) with all the posts sorted from most recent to oldest. '''
    content_path = PATHS['CONTENT_PATH']
    posts = []
    for category in os.listdir(content_path):
        if os.path.isdir(os.path.join(content_path, category)):
            for post in os.listdir(os.path.join(content_path, category)):
                if os.path.isdir(os.path.join(content_path, category, post)):
                    metadata, html_content, available_in_lang = load_post(category, post)

                    # Extract only the first paragraph
                    start_index = html_content.find('<p>')
                    end_index = html_content.find('</p>')

                    # Extract the first paragraph
                    first_paragraph = html_content[start_index + 3: end_index]
                    posts.append((category, post, metadata, first_paragraph, available_in_lang))

    # sort by date
    posts.sort(key = lambda x: x[2]['date'], reverse = True)

    return posts

@bp.route('/')
@bp.route('/page/<int:page_num>')
def index(page_num = 1):
    posts = get_all_posts()
    n = len(posts)
    n_perpage = 4
    n_pages = math.ceil(n/n_perpage)

    if page_num > n_pages:
        return redirect(url_for('blog.index', page_num=n_pages))
    if page_num < 1:
        return redirect(url_for('blog.index'))

    # calculate indeces for first and last posts to show
    start = (page_num - 1)*n_perpage
    end = page_num*n_perpage
    if end > n:
        end = n

    g.url_args = {'page_num': page_num}
    return render_template('blog/blog.html', posts = posts, n_pages = n_pages, n_perpage = n_perpage, current_page = page_num, start = start, end = end)

@bp.route('/<post_category>/<post_title>')
def show_post(post_category, post_title):
    # Read the .md file content
    post_metadata, post_content_html, available_in_lang = load_post(escape(post_category), escape(post_title))
    g.url_args = {'post_category': escape(post_category), 'post_title': escape(post_title)}
    return render_template('blog/post.html', metadata = post_metadata, post_content_html = post_content_html, available_in_lang = available_in_lang)