import socketio

# create a Socket.IO server
sio = socketio.AsyncServer()

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

