import socketio

# create a Socket.IO server
sio = socketio.AsyncServer(logger=True, engineio_logger=True)

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app.run()
