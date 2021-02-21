import socketio

# create a Socket.IO server
sio = socketio.AsyncServer()

# wrap with a WSGI application
app = socketio.WSGIApp(sio)

