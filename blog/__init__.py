import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'blog.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password'
))
app.config.from_envvar('SAM_BLOG_SETTINGS', silent=True)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

import blog.blog
import blog.db
