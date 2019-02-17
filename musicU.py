import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from twilio.rest import Client

#http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
#https://www.twilio.com/docs/usage/api/applications#list-post-example-1
#https://www.twilio.com/docs/voice/api/call

UPLOAD_FOLDER = '/mnt/c/Users/leevi/Desktop/HopHack/Uploaded'
ALLOWED_EXTENSIONS = set(['mid', 'mp3'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

account_sid = 'ACb75b16da0e62787332c5b307f41a0aba'
auth_token = 'a2548b83c329dc1034a8bf898ba592d0'
client = Client(account_sid, auth_token)

def call_you(target_p, twiML): 
    call = client.calls.create(
                            application_sid=twiML,
                            to=target_p,
                            from_='+14438427407'
                        )
    #print(call.sid)

#Create new TwiML with the target audio filename
def new_app(filename):
    application = client.applications \
                        .create(
                             voice_method='GET',
                             voice_url='https://cfa32cb4.ngrok.io/' + filename,
                             friendly_name=filename
                         )
    #print(application.sid)
    return application.sid

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'MIDI1' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file1 = request.files['MIDI1']
        file2 = request.files['MIDI2']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file1.filename == '' and file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file1 and allowed_file(file1.filename) and \
                file2 and allowed_file(file2.filename):
            file1name = secure_filename(file1.filename)
            file2name = secure_filename(file2.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1name))
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2name))
            TwiML = new_app(file1name)
            mobileNum = request.form['mobileNum']
            #call_you(mobileNum, TwiML)
            return redirect(url_for('upload_file',
                                    filename=file1name))
    return '''
    <!DOCTYPE html>
    <html lang="en-US">
    <head>
    <title>music.U</title>
    <head profile="http://www.w3.org/2005/10/profile">
        <link rel="icon" type="image/png" href="LogoVecBlackICO.ico">
        </link>

    <style>

    body {
        background-color:black;
        }

    h1 {
        border: 7px solid Purple;
        padding: 30px;
        text-align:center;
        font-family: courier;
        <!-- Text Stuff font-size: 40px;
        color: magenta; -->
        }

    p {
        color: white;
        text-align:center;
        font-family: courier;
        }

    .button {
        background-color: #38023B; <!--Middle Red Purple-->
        border: 3px white;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display:center-block;
        font-size: 12px;
        font-family: courier;
        margin: 30px;
        padding: 40px 60px;
        }

    #button1 {
        background-color: #3B4387;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display:center-block;
        font-size: 12px;
        font-family: courier;
        margin: 30px;
        padding: 40px 60px;
        }
        
    #button2 {
        background-color: #961D4E;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display:center-block;
        font-size: 12px;
        font-family: courier;
        margin: 30px;
        padding: 40px 60px;
        }

    #button3 {
        background-color: #792359;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display:center-block;
        font-size: 12px;
        font-family: courier;
        margin: 30px;
        padding: 40px 60px;
        }

    #button4 {
        background-color: #D10080;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display:center-block;
        font-size: 12px;
        font-family: courier;
        margin: 30px;
        padding: 40px 60px;
        }

    .buttonHolder {
        text-align: center;
        }

    #homeButton {
        background-color: black;
        padding: 1px;
        }

    a:link, a:visited {
        color: white;
        background-color: magenta;
        text-decoration: none;
        text-align: center;
        padding: 15px 25px;
        display: center-block;
        justify-content: center;
        font-family: courier;
        }

    a:hover, a:active {
        color: white;
        background-color: blue;
        text-decoration-line: underline;
        text-align: center;
        display: center-block;
        justify-content: center;
        font-family: courier;
        }

    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        }

    <!--Left
    .left {
        display: block;
        margin-left: 0%;
        margin-right: 100%;
        }
    -->

    <!--Right
    .right {
        display: block;
        margin-left: 100%;
        margin-right: 0%;
        }-->

    .footer {
      position: fixed;
      left: 0;
      bottom: 0;
      width: 100%;
      background-color:#1D1F26;
      color: white;
      text-align: center;
        }

    .uploadWrapper {
        position: relative;
        overflow: hidden;
        display: inline-block;
        }
        
    .uploadWrapper input[type=file] {
        font-size: 100px;
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
        }

    .bigButt {
        border: 2px white;
        color: white;
        background-color: magenta;
        padding: 8px 20px;
        border-radius: 8px;
        font-size: 20px;
        font-family: courier;
        text-align: center;
        }

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <meta name="description" content="Create your own melody by blending two different songs!">
    <meta name="keywords" content="music,composing,generator,compose">
    <meta name="author" content="Hannah Kiesel, Shawn Kiesel, Vincent Lee, Katie Luo">

    </style>
    </head>

    <body>

    <h1>

    <a href="index.html" id="homeButton";>
    <img src="/static/Banner.png" alt="Banner" style="width:1150px;height:140px;" class:"center">
    </a>

    <img src="/static/MusicNote.png" alt="Music Note Icon" style="float:right;width:118px;height:152px;">
    <img src="/static/MusicNote.png" alt="Music Note Icon" style="float:left;width:118px;height:152px;">

    </h1>

    <hr>

    <img src="/static/LogoVecBlack.png" alt="Comp Icon" style="Width:218px;height:200px;" class="center">

    <p>Choose 2 .MIDI files from your computer... <br><br>
    and <strong>music.U</strong> will create a NEW song based on your choices!</p>


    <div class="buttonHolder";>

    <!-- Buttons
    <button id="button1">Chopin - Nocturne, Op. 9 No. 2</button>
    <button id="button2">Bach - F&uuml;r Elise</button>
    <button id="button3">Tchaikovsky - Swan Lake</button>
    <button id="button4">Haydn - Symphony No. 94</button> -->

    <br><br>


    <form method=post enctype=multipart/form-data>
        <div class="uploadWrapper;">
            <button class="bigButt">Upload 1st .MIDI!</button>
            <input required type="file" name=MIDI1>
            </input>
        </div>

        <br><br>

        <div class="uploadWrapper;">
            <button class="bigButt">Upload 2nd .MIDI!</button>
            <input type="file" name="MIDI2">
            </input>
        </div>

        <br><br>

        <p>Once you've uploaded 2 .MIDIs... <br><br>
        Enter a mobile number to send your new song to,<br><br>
        and click <strong>"Compose"</strong> to begin!</p>

        <br>
        Mobile Number: <br>
        <input required type="text" name="mobileNum"> <br><br>
       <input type="submit" value=Upload>
    </form>

    <br><br>

    <!-- Colored button
    <a href="generate.html" target="_blank">Compose</a> -->

    </div>

    <br><br><br><br>

    <div class="footer">
    <p style="font-size:80%"> &copy; Hannah Kiesel, Shawn Kiesel, Vincent Lee, Katie Luo </p>
    </div>

    </body>
    </html>
        '''







    '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


