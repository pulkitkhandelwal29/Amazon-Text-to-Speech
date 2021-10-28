from flask import Flask, request, render_template,url_for
from flask_cors import cross_origin
import boto3

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/sound", methods = ["GET", "POST"])
@cross_origin()
def sound():
    if request.method == "POST":
        text = request.form['texttospeech']    
        gender = request.form['gender']
        polly = boto3.client(service_name='polly',region_name='us-east-1')  
        if gender == "male":
             response = polly.synthesize_speech(OutputFormat='mp3', VoiceId='Brian',Text=text)
        else:
             response = polly.synthesize_speech(OutputFormat='mp3', VoiceId='Joanna',Text=text)
        file = open('static/audio/speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()
    return render_template("index.html",conversion="Your Text has been converted to speech...")


if __name__ == "__main__":
    app.run(debug=True)
