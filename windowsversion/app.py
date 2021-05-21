#PythonSerious 2021




import sys, datetime, json, re
from flask import Flask, request, abort, jsonify, render_template, send_file
import os
import json
import time

html = """
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Music Controller</title>
<script class="jsbin" src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<style>
  body {
  font-family: sans-serif;
  background-color: #222;
}

.file-upload {
  background-color: #222;
  width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.file-upload-btn {
  width: 100%;
  margin: 0;
  color: #fff;
  background: #1FB264;
  border: none;
  padding: 50px;
  border-radius: 4px;
  border-bottom: 4px solid #15824B;
  outline: none;
  text-transform: uppercase;
  font-weight: 700;
}

.file-upload-btn inputbut{
  height: 100%;
  background-color: #222;
}

.file-upload-btn:hover {
  background: #1AA059;
  color: #ffffff;
  transition: all .2s ease;
  cursor: pointer;
}

.file-upload-btn:active {
  border: 0;
  transition: all .2s ease;
}

.file-upload-content {
  display: none;
  text-align: center;
}

.file-upload-input {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  outline: none;
  opacity: 0;
  cursor: pointer;
}

.image-upload-wrap {
  margin-top: 20px;
  border: 4px dashed #1FB264;
  position: relative;
}

.image-dropping,
.image-upload-wrap:hover {
  background-color: #1FB264;
  border: 4px dashed #ffffff;
}

.image-title-wrap {
  padding: 0 15px 15px 15px;
  color: #222;
}

.drag-text {
  text-align: center;
}

.drag-text h3 {
  font-weight: 100;
  text-transform: uppercase;
  color: #15824B;
  padding: 60px 0;
}

.file-upload-image {
  max-height: 200px;
  max-width: 200px;
  margin: auto;
  padding: 20px;
}

.remove-image {
  width: 200px;
  margin: 0;
  color: #fff;
  background: #cd4535;
  border: none;
  padding: 10px;
  border-radius: 4px;
  border-bottom: 4px solid #b02818;
  transition: all .2s ease;
  outline: none;
  text-transform: uppercase;
  font-weight: 700;
}

.remove-image:hover {
  background: #c13b2a;
  color: #ffffff;
  transition: all .2s ease;
  cursor: pointer;
}

.remove-image:active {
  border: 0;
  transition: all .2s ease;
}
</style>
<div class="file-upload">
  <form class=file-upload-btn action = "http://IPHERE:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input class= "inputbut"  type = "file" name = "file" accept="audio/*" multiple />
         <input class="submit" onclick="window.location.href = 'http://IPHERE:5000/uploaded';" type = "submit"  />
      </form>   

  
</div>
"""


def changepage():
   html = """
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Music Controller</title>
<script class="jsbin" src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<style>
  body {
  font-family: sans-serif;
  background-color: #222;
}

.file-upload {
  background-color: #222;
  width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.file-upload-btn {
  width: 100%;
  margin: 0;
  color: #fff;
  background: #1FB264;
  border: none;
  padding: 50px;
  border-radius: 4px;
  border-bottom: 4px solid #15824B;
  outline: none;
  text-transform: uppercase;
  font-weight: 700;
}

.file-upload-btn inputbut{
  height: 100%;
  background-color: #222;
}

.file-upload-btn:hover {
  background: #1AA059;
  color: #ffffff;
  transition: all .2s ease;
  cursor: pointer;
}

.file-upload-btn:active {
  border: 0;
  transition: all .2s ease;
}

.file-upload-content {
  display: none;
  text-align: center;
}

.file-upload-input {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  outline: none;
  opacity: 0;
  cursor: pointer;
}

.image-upload-wrap {
  margin-top: 20px;
  border: 4px dashed #1FB264;
  position: relative;
}

.image-dropping,
.image-upload-wrap:hover {
  background-color: #1FB264;
  border: 4px dashed #ffffff;
}

.image-title-wrap {
  padding: 0 15px 15px 15px;
  color: #222;
}

.drag-text {
  text-align: center;
}

.drag-text h3 {
  font-weight: 100;
  text-transform: uppercase;
  color: #15824B;
  padding: 60px 0;
}

.file-upload-image {
  max-height: 200px;
  max-width: 200px;
  margin: auto;
  padding: 20px;
}

.remove-image {
  width: 200px;
  margin: 0;
  color: #fff;
  background: #cd4535;
  border: none;
  padding: 10px;
  border-radius: 4px;
  border-bottom: 4px solid #b02818;
  transition: all .2s ease;
  outline: none;
  text-transform: uppercase;
  font-weight: 700;
}

.remove-image:hover {
  background: #c13b2a;
  color: #ffffff;
  transition: all .2s ease;
  cursor: pointer;
}

.remove-image:active {
  border: 0;
  transition: all .2s ease;
}
</style>
<div class="file-upload">
  <div class=file-upload-btn>
      <h2>Queue Completed!</h2>
  </div>  
         
  

  
</div>
   """
   return html



app = Flask(__name__)
@app.route('/uploaded')
def uploaded():

   return changepage()

@app.route('/upload')
def upload():

   return html

@app.route('/sample')
def sample():

   return send_file('/home/ubuntu/speakerapi/Celine.mp3', attachment_filename='Celine.mp3')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      a = request.files['file']
      f = request.files.getlist('file')
      print(f)

      if len(f) > 1:
         for X in f:
            X.save(f"tempstorage/{X.filename}")
            os.system(f"ffplay -nodisp -volume 100 -autoexit -loglevel quiet tempstorage/{X.filename}")
            os.remove(f"tempstorage/{X.filename}")
      else:
         a.save(f"play.mp3")
         os.system(f"ffplay -nodisp -volume 100 -autoexit -loglevel quiet play.mp3")
         os.remove(f"play.mp3")
   return changepage()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
