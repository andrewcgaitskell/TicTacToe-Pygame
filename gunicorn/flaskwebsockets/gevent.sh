uwsgi --master --socket 0.0.0.0:5008 --http-websockets --gevent 100 --wsgi server:app
