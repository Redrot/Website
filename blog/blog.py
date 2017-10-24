from blog.db import get_db
from datetime import datetime
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from blog import app

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select * from posts order by id desc')
    posts = cur.fetchall()
    return render_template('index.html', posts=posts)


@app.route('/math')
def math():
    db = get_db()
    cur = db.execute('select * from posts where type="math" order by id desc')
    posts = cur.fetchall()
    return render_template('math.html', posts=posts)


@app.route('/music')
def music():
    db = get_db()
    cur = db.execute('select * from posts where type="music" order by id desc')
    posts = cur.fetchall()
    return render_template('math.html', posts=posts)


@app.route('/other')
def other():
    db = get_db()
    cur = db.execute('select * from posts where type="other" order by id desc')
    posts = cur.fetchall()
    return render_template('math.html', posts=posts)


@app.route('/about')
def about():
    db = get_db()
    cur = db.execute('select * from posts where type="music" order by id desc')
    posts = cur.fetchall()
    return render_template('math.html', posts=posts)


@app.template_filter('strftime')
def _jinja2_filter_datetime(date):
    parsed = datetime.strptime(date, '%Y-%m-%d')
    return parsed.strftime('%b %d, %Y')
