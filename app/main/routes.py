from flask import current_app, render_template, url_for, flash, redirect, request

import os
import secrets

from app import mongodb
from . import main
from .models import eInstance, eMessage

@main.route("/")
def home_page():
    instance = eInstance.objects().first()
    image_file = url_for('static', filename=f'media/{instance.media_file}')
    emessages = eMessage.objects().all()
    room_name = 'home'
    return render_template('home.html', title=instance.homepage_title, image_file=image_file, views=instance.page_views,
                           is_video = instance.media_is_video, chat_enabled = instance.chat_enabled, room=room_name,
                           messages=emessages, color=instance.homepage_hex_color,
                           is_default=instance.media_file_is_default)
