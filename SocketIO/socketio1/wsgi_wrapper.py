from aiohttp import web
from aiohttp_wsgi import WSGIHandler
from foobar import application

wsgi_handler = WSGIHandler(application)

def init_func(argv):
    app = web.Application()
    app.router.add_get("/", index_handler)
    app.router.add_route("*", "/{path_info:.*}", wsgi_handler)
    return app
    
web.run_app(app)
