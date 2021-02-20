uwsgi --master --socket 0.0.0.0:5006 --http-websockets --gevent 100 --wsgi server:app
