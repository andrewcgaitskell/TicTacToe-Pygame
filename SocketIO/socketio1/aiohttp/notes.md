https://docs.aiohttp.org/en/v0.18.2/web.html

source /home/andrew_gaitskell/Games/env/bin/activate

cd /home/andrew_gaitskell/Games/TicTacToe-Pygame/SocketIO/socketio1/aiohttp


    start_server = websockets.serve(hello, host="127.0.0.1", port=5011)

    def application(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(start_server)
            loop.run_forever()
        except:
            print(f"All Over")
