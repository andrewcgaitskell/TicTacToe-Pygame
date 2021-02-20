uwsgi --master --http 0.0.0.0:5009 --socket 0.0.0.0:5008 --http-websockets -b 32768 --gevent 100 --wsgi server:app
