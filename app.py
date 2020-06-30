from flask import Flask,jsonify,request
from dankcli import *
from meme_gen import *
from firebase_upload_download import *
import os
import imageio
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

app=Flask(__name__)

@app.route('/dankcli-meme',methods=['GET','POST'])
def dankcli():
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

@app.route('/meme-gen',methods=['GET','POST'])
def mem_gen():
	url = request.json['URL']
	top_text = request.json['TOP']
	bottom_text = request.json['BOTTOM']
	name = url.split("?")[0]
	name = name[-8:]
	converted_img = generate_meme(url,top_text,bottom_text)
	local_path = os.path.join(dir_path,converted_img)
	upload("/.Generated/"+name,local_path)
	link = get_url("/.Generated/"+name)
	return link

if __name__=='__main__':
	app.run(debug = True, port = 8000)



