import datetime
import redis
from flask import Flask, Response, redirect, render_template, request, session


app = Flask(__name__)
app.config['SECRET_KEY']="332**GV&T(&)"

r = redis.StrictRedis('localhost', 6379, 0, charset='utf-8', decode_responses=True)

@app.route('/subscrib', methods=['GET','POST'])
def subscrib():
    if request.method == 'POST':
        session['user'] = request.form['user']
        return redirect('/')
    return render_template('subscrib.html')

def event_stream():
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        yield 'data: %s\n\n'%message['data']

@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    user = session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    r.publish('chat', '[%s], %s: %s' %(now.isoformat(), user, message))
    return Response(status=204)

@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype='text/event-stream')

@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/subscrib') 
    return render_template('chat.html', user=session['user'])

if __name__ == "__main__":
    app.run()