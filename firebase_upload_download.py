import pyrebase
config = {
	"apiKey": "AIzaSyC1UXihvuI2vdkapG7Uy80LOd16K6YUcrc",
    "authDomain": "meme-generator-cfdc0.firebaseapp.com",
    "databaseURL": "https://meme-generator-cfdc0.firebaseio.com",
    "projectId": "meme-generator-cfdc0",
    "storageBucket": "meme-generator-cfdc0.appspot.com",
    "messagingSenderId": "937239795623",
    "appId": "1:937239795623:web:955bee20c96239dd268882",
    "measurementId": "G-YJR2HVJBBX"
    }

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def upload(path_on_cloud,path_local):
	storage.child(path_on_cloud).put(path_local)

def download(path_on_cloud,path_local):
	storage.child(path_on_cloud).download(path_local)

def get_url(path_on_cloud):
	return storage.child(path_on_cloud).get_url(None)