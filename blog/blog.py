from blog.db import get_db
from datetime import datetime
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from blog import app


@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select * from posts')
    posts = cur.fetchall()
    return render_template('index.html', posts=posts)

# @app.route('/create')
# def create():
#     return render_template('create.html', date=str(datetime.date(datetime.now())))
#
# @app.route('/create', methods=['POST'])
# def create_entry():
#     db = get_db()
#     db.execute(
#         'insert into posts (title, short_title, content, created_at, updated_at) \
#         values (?, ?, ?, date(\'now\'), date(\'now\'))',
#         [request.form['title'], request.form['title'], request.form['content']])
#     db.commit()
#     return redirect(url_for('index'))
#
#


@app.template_filter('strftime')
def _jinja2_filter_datetime(date):
    parsed = datetime.strptime(date, '%Y-%m-%d')
    return parsed.strftime('%b %d, %Y')
