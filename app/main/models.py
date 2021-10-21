from datetime import datetime

from app import mongodb

#message objects for mongodb
class eMessage(mongodb.Document):
    date_posted = mongodb.StringField()
    name = mongodb.StringField()
    content = mongodb.StringField()

#instance objects for mongodb
#so far, we only support one instance -- all clients log into
#one session
class eInstance(mongodb.Document):
    chat_enabled = mongodb.BooleanField(default=True)
    homepage_title = mongodb.StringField(default='Chat Application')
    homepage_hex_color = mongodb.StringField(default='ffd0cc')
    media_file = mongodb.StringField(default='default.jpg')
    media_file_is_default = mongodb.BooleanField(default=True)
    media_is_video = mongodb.BooleanField(default=False)
    page_views = mongodb.IntField(default=0)

#create the first (and only) instance and save it in mongodb
if eInstance.objects().first() is None:
    eInstance().save()
