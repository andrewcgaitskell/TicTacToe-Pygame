gunicorn -k flask_sockets.worker route_decorator:app
