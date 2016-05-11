import boto3
import os
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
  return render_template('upload_form.html', uploadButtonName="send")
app.debug = True


@app.route("/upload", methods=['POST'])
def upload():
  files = request.files
  for f in files.getlist('file'):
    #filename = f.filename
    #updir = '/home/ec2-user/upload-web-interface/upload'
    #f.save(os.path.join(updir, filename))
    uploadS3(f)
  return jsonify()



def uploadS3(file):
  bucket_name='166665-angel'
  s3 = boto3.resource('s3')
  bucket = s3.Bucket(bucket_name)
  bucket.put_object(Key=file.filename, Body=file)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

