from app import web_app, socketio

if __name__ == '__main__':
    socketio.run(web_app, host='0.0.0.0', port=8080)
