# Live chat

Demonstration of a Flask application with live chat functionality.  Comments are added to the page for all connected clients, and the page views automatically updates as well.

- **Live chat:**  Using Javascript, `SocketIO`, and `JQuery`.  All messages are sent to the Python web server, and then broadcast back to all clients.
- **Persistent chat:** all chat messages are saved to an external Mongodb, and are added to the page for any other people joining the chat page.

# How to use
Included is `requirements.txt` to quickly install all dependencies using the command `pip3 install -r requirements.txt`. 

If you don't have pip3, please install first `sudo apt install python3-pip`.

Then, using the Flask development server, simply run `python3 run.py`.  You're set!

This is an adpatation from: https://github.com/MarkMichon1/Flask-Chat-App
