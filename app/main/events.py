from flask_socketio import emit, send
from datetime import datetime
import json

from app.main.models import eInstance, eMessage
from .. import socketio, mongodb


@socketio.on('message')
def handle_message(msg):
    #get message sent from client(s)
    name = msg['name']
    content = msg['message']
    now = datetime.now().strftime('%A %I:%M:%S %p').lstrip("0").replace(" 0", " ")
    
    #put received message into database
    emessage_object = eMessage(name=name, content=content, date_posted=now)
    emessage_object.save()

    #broadcast received message to all clients
    json_data = {
        'name' : name,
        'content' : content,
        'date' : now
    }
    send({'json_data' : json_data}, broadcast=True)

@socketio.on('connected')
def handle_connection():
    #a new client joined; update page view; broadcast to all clients
    einst = eInstance.objects().first()
    einst.page_views += 1
    einst.update(page_views = einst.page_views)
    emit('page_view_increase', {'page_views' : einst.page_views}, broadcast=True)
