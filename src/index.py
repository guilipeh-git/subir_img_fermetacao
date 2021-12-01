#flask==2.0.2
#pip install opencv-python==4.5.4.60
import os
from flask import Flask, render_template as rt,url_for,request,send_from_directory,redirect
import cv2 as cv
import circles
app = Flask(__name__)

@app.route("/")
def index():

    return rt("index.html")
 

@app.route("/return", methods=["POST","GET"])
def returnMsg():
    file = request.files.get("file")
    print(file.filename)
    resp = lambda x :file.filename.lower().find(x)
    Eimg = (resp(".jpg")*resp(".png")*resp(".jpeg")) 
    
    if(Eimg != -1):
        file.save(os.path.join("src/static/imagens_salvas",file.filename))
        print(f"src/static/imagens_salvas/{file.filename}")
        circles.circles(f"src/static/imagens_salvas/{file.filename}")
        

    return redirect(url_for("index"))
app.run(debug=True, port=80)
