from flask import Flask,jsonify,request
from dankcli import *
from firebase_upload_download import *
import os
import imageio
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def sketch():
	url = request.json['URL']
	text = request.json['Text']
	name = url.split("?")[0]
	name = name[-8:-4]
	img = imageio.imread(url)
	plt.imsave("Input.jpg",img)
	converted_img = meme("Input.jpg",text,name)
	upload("/.Generated/"+name+".png",name+".png")
	link = get_url("/.Generated/"+name+".png")
	return link


if __name__=='__main__':
	app.run(debug = True, port = 8000)



