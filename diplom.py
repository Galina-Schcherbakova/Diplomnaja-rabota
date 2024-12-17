from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = 'your_secret_key'
google_bp = make_google_blueprint(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix='/google_login')

@app.route('/')
def index():
    return 'Welcome to the OAuth example!'

@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/plus/v1/people/me')
    assert resp.ok, resp.text
    return f'You are logged in as: {resp.json()["displayName"]}'

if __name__ == '__main__':
    app.run(debug=True)
