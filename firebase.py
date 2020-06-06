import pyrebase
#you will get apiKey etc fom your googleservices.json file
#authDomain usually your projectId.firebaseapp.com
config={
        "apiKey":"put your api key",
        "databaseURL": "put your url",
        "projectId":"put your project id",
        "storageBucket":"put your storageBucket",
        "authDomain":"put your authDomain usually projectId.firebaseapp.com"
        }

firebase=pyrebase.initialize_app(config)

storage=firebase.storage()

storage.child("put firebase storage location eg:images/name1.jpg").put("put your local image folder C:/Users/dell/Pictures/download.jpg")
a=storage.child("eg/name1.jpg").get_url(None) #you will get Image URL
print(a)
#for real time database
#push image url and name to realtime db
db=firebase.database()
data={"name":"ab","image":a}
db.child("eg").push(data)
print("done")
