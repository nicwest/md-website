import os
import re
import datetime
import markdown
from app import app

class Post(object):
    slug = None
    title = None
    path = None
    summary = None
    date = None
    content = None
    tags = None
    base_path = None
    
    def __init__(self, slug, title, path, summary, date, tags=''):
        self.slug = slug
        self.title = title
        self.path = path
        self.summary = summary
        self.date = date
        self.tag_string = tags
        self.base_path = os.path.join(app.config['BASEDIR'], 'app', 'static', 'posts',
                            self.path)

    def make_html(self):
        self.content = markdown.markdown(
            open(self.base_path).read(), extensions=['fenced_code', 'headerid'])

    @property
    def tags(self):
        return self.tag_string.lower().split(', ')

    @property
    def clean_tags(self):
        tags = self.tags
        return [(x.replace('*', ''), re.sub('[^a-z0-9-]', '-', x.replace('*', ''))) for x in tags]

    @property
    def datetime (self):
        return datetime.datetime.strptime(self.date, '%Y-%m-%d %H:%M')

#post list
posts = [
    #Post('test', 'Test Post Please Ignore', 'test.md', '',
    #     '2014-06-05 20:48', tags='test, **things'),
    Post('hello-world', 'Hello World', 'hello-world.md', 'first horrible post',
         '2014-06-07 17:54', tags='blog, me, **vim'),
    Post('highlight-pullrequest', 'Highlight.js Pull Request',
         'highlight-pullrequest.md',
         'A pull request to highlight.js and plans about pull requests in general',
         '2014-06-09 11:22', tags='highlight.js, **pull request, blog'),
    Post('leader-key', 'Leader Key', 'leader-key.md', 'Leader key as spacebar' +
         ' and why I use it for everything', '2014-06-18 00:38', tags='**vim'),
    Post('vim-filter-list-by-list', 'Vim: filter list by list',
         'vim-filter-list-by-list.md', 'How to filter a list by a list in vim',
         '2014-07-06 01:41', tags='**vim, **pull request'),
    ]

posts.sort(key=lambda x: x.date, reverse=True)

slugs = {}
tags = {}
for post in posts:
    slugs[post.slug] = post
    for tag in post.tags:
        strong = False
        if tag.startswith('**'):
            strong = True
            tag = tag[2:]
        link=re.sub(r'[^0-9a-z]', '-', tag)
        if link not in tags:
            tags[link] = {'strong': False, 'name': tag, 'posts': []}
        if post not in tags[link]:
            tags[link]['posts'].append(post)
        if strong:
            tags[link]['strong'] = True

