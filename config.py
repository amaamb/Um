#-*- coding: utf-8 -*-
#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED=True
SECRET_KEY='development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'umapp.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
#mail server settings
MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME='peppecomng'
MAIL_PASSWORD='H3in3ken'
#administrator
ADMINS=['peppecomng@gmail.com','amachefe@outlook.com']
POSTS_PER_PAGE=3
WHOOSH_BASE=os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS=50

# available language
LANGUAGES = {
    'en': 'English',
    'es': 'Espanol'
}
MS_TRANSLATOR_CLIENT_ID = ''
MS_TRANSLATOR_CLIENT_SECRET = ''
