uwsgi --master --http :5006 --http-websockets --gevent 100 --wsgi server:app
