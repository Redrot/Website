from blog.db import get_db
from datetime import datetime
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from blog import app

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select * from posts order by id desc limit 5')
    posts = cur.fetchall()
    return render_template('index.html', posts=posts)


@app.route('/math')
def math():
    return render_template('math.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/other')
def other():
    return render_template('other.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.template_filter('strftime')
def _jinja2_filter_datetime(date):
    parsed = datetime.strptime(date, '%Y-%m-%d')
    return parsed.strftime('%b %d, %Y')
