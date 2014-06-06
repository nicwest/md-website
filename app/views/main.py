import os
from flask import Flask, render_template, Response
#from feedgen.feed import FeedGenerator
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

@app.route('/rss/')
def view_rss(slug):
    fg = FeedGenerator()
    fg.id('http://www.nic-west.com/')
    fg.title('things')
    fg.author( {'name':'Nic West','email':'nope@nada.com'} )
    fg.link( href='http://www.nic-west.com/rss/', rel='self' )
    fg.language('en')
    rssfeed  = fg.rss_str(pretty=True)
    return Response(rssfeed, mimetype="application/rss+xml")

@app.route('/tags/')
def view_tags():
    return render_template('tags.html', tags=posts.tags.keys())

@app.route('/tags/<tag>')
def view_tag(tag):
    return render_template('index.html', posts=posts.tags[tag]['posts'])
