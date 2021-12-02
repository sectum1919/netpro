from flask import Flask, render_template, Response, send_from_directory, session, redirect
#import cv2

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/stream/<string:file_name>')
def stream(file_name):
    session['livepath'] = file_name
    print("session",session['livepath'])
    return render_template('live.html', livepath=session['livepath'])

@app.route('/hls/<string:file_name>')
def hls(file_name):
    session['hls_livepath'] = file_name
    print("session",session['hls_livepath'])
    return render_template('hls.html', hls_livepath=session['hls_livepath'])

@app.route('/dash/<string:file_name>')
def dash(file_name):
    session['dash_livepath'] = file_name
    print("session",session['dash_livepath'])
    return render_template('dash.html', dash_livepath=session['dash_livepath'])

# @app.route('/hls/<string:file_name>')
# def hls(file_name):
#     video_dir = '/home/homepages/netpro/m3u8File/'
#     return redirect(directory=video_dir, filename=file_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=12060,debug=True)
