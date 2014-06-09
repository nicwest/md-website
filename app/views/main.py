import os
from urlparse import urljoin
from flask import Flask, render_template, Response, request, url_for
from flask import send_from_directory
from werkzeug.contrib.atom import AtomFeed
from app import app, cache, posts


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@cache.cached(timeout=50)
@app.route('/')
def index():
    return render_template('index.html', posts=posts.posts)

@app.route('/cv/')
def cv_display_temp():
    return render_template('temp_cv.html')

@cache.cached(timeout=50)
@app.route('/<slug>')
def view_post(slug):
    if slug in posts.slugs:
        post = posts.slugs[slug]
        post.make_html()
        return render_template('post.html', post=post)
    return render_template('404.html')

@cache.cached(timeout=50)
@app.route('/<slug>/md')
def view_markdown(slug):
    if slug in posts.slugs:
        post = posts.slugs[slug]
        content = open(post.base_path, 'r').read()
        return Response(content, mimetype="text/x-markdown")

@cache.cached(timeout=50)
@app.route('/recent.atom')
def view_atom():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root, author='Nic West')
    for post in posts.posts:
        post.make_html()
        feed.add(post.title, post.content,
                 content_type='html',
                 url=urljoin(request.url_root, url_for('view_post', slug=post.slug)),
                 updated=post.datetime,
                 published=post.datetime)
    resp = feed.get_response()
    return resp

@cache.cached(timeout=50)
@app.route('/tags/')
def view_tags():
    tags = [(x, y) for x, y in posts.tags.iteritems()]
    tags.sort(key=lambda x: x[0])
    return render_template('tags.html', tags=tags)

@cache.cached(timeout=50)
@app.route('/tags/<tag>')
def view_tag(tag):
    return render_template('index.html', posts=posts.tags[tag]['posts'])
