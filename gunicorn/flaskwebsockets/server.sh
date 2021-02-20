uwsgi --master --http 0.0.0.0:5008 --http-websockets --wsgi server:app
