import sqlite3
import markdown2
from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from blog import app

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def seed_db():
    db = get_db()
    with app.open_resource('seeds.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')


@app.cli.command('seeddb')
def seeddb_command():
    seed_db()
    print('Seeded the database.')


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


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
