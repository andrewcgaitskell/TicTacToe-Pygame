uwsgi --master --http 0.0.0.0:5008 --http-websockets --gevent 100 --wsgi server:app
