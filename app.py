import os
import urllib.request
from flask import Flask, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)


@app.route('/')
def get_content():
    url = request.args.get('url', None)
    if not url:
        return "Running"
    username = os.getenv("PROXYLAND_USER")
    password = os.getenv("PROXYLAND_PASSWORD")

    proxy = ('http://%s:%s@server.proxyland.io:9090' % (username, password))

    query = urllib.request.build_opener(urllib.request.ProxyHandler({ 'http': proxy }))

    return query.open(url).read()