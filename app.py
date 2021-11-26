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
    username = os.getenv("PROXY_USER")
    password = os.getenv("PROXY_PASSWORD")
    endpoint = os.getenv("PROXY_ENDPOINT")
    port = os.getenv("PROXY_PORT")

    proxy = (f'http://{username}:{password}@{endpoint}:{port}')

    query = urllib.request.build_opener(urllib.request.ProxyHandler({ 'http': proxy }))

    return query.open(url).read()