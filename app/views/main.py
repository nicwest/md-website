import os
from urlparse import urljoin
from flask import Flask, render_template, Response, request, url_for
from werkzeug.contrib.atom import AtomFeed
from app import app
from app import posts

@app.route('/')
def index():
    return render_template('index.html', posts=posts.posts)

@app.route('/cv/')
def cv_display_temp():
    return render_template('temp_cv.html')

@app.route('/<slug>')
def view_post(slug):
    if slug in posts.slugs:
        post = posts.slugs[slug]
        post.make_html()
        return render_template('post.html', post=post)
    return render_template('404.html')

@app.route('/<slug>/md')
def view_markdown(slug):
    if slug in posts.slugs:
        post = posts.slugs[slug]
        content = open(post.base_path, 'r').read()
        return Response(content, mimetype="text/x-markdown")

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

@app.route('/tags/')
def view_tags():
    tags = [x for x in posts.tags.iteritems()]
    tags.sort(key=lambda x: x[0])
    return render_template('tags.html', tags=posts.tags.iteritems())

@app.route('/tags/<tag>')
def view_tag(tag):
    return render_template('index.html', posts=posts.tags[tag]['posts'])
