import os
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
        return self.tag_string.lower().split(' ')

#post list
posts = [
    Post('troll', 'fuubar lol', 'troll.md', 'I like camel', '2014-06-05 21:15',
         tags='test something'),
    Post('test', 'Test Post Please Ignore', 'test.md',
         'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod' +
         'tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At' +
         'vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,' +
         'no sea takimata sanctus est Lorem ipsum dolor sit amet.',
         '2014-06-05 20:48', tags='test things'),
]

posts.sort(key=lambda x: x.date, reverse=True)

slugs = {x.slug: x for x in posts}
tags = {}
for post in posts:
    for tag in post.tags:
        if tag not in tags:
            tags[tag] = {'strong': False, 'posts': []}
        if post not in tags[tag]:
            tags[tag]['posts'].append(post)
        
