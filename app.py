from flask import Flask,jsonify,request
from dankcli import *
from meme_gen import *
from firebase_upload_download import *
import os
import imageio
import matplotlib.pyplot as plt
from ImageClub import *
from random_no import *

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

@app.route('/hconcat',methods=['GET','POST'])
def hconcat():
	n = random_no()
	format_='.jpg'
	name = "Hconcat_"+n+format_
	
	urls = request.json['URL']
	imgs = [imageio.imread(url) for url in urls]
	
	loc=[]
	for idx in range(len(imgs)):
		plt.imsave("Input_hconcat"+n+str(idx)+".jpg",imgs[idx])
		loc.append("Input_hconcat"+n+str(idx)+".jpg")

	converted_img = hconcat_resize_min(loc,name)
	upload("/.Generated/"+name,converted_img)
	link = get_url("/.Generated/"+name)
	return link

#completed
@app.route('/vconcat',methods=['GET','POST'])
def vconcat():
	n = random_no()
	format_='.jpg'
	name = "Vconcat_"+n+format_


	urls = request.json['URL']
	imgs = [imageio.imread(url) for url in urls]
	
	loc=[]
	for idx in range(len(imgs)):
		plt.imsave("Input_vconcat"+n+str(idx)+".jpg",imgs[idx])
		loc.append("Input_vconcat"+n+str(idx)+".jpg")

	converted_img = vconcat_resize_min(loc,name)
	upload("/.Generated/"+name,converted_img)
	link = get_url("/.Generated/"+name)
	return link

if __name__=='__main__':
	app.run(debug = True, port = 8000)



