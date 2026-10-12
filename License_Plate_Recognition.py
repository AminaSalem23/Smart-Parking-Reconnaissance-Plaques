#Libraries
import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
from ultrason import distance as dst
import pyrebase
#initialiser les paramètre de caméra
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 30
#initialiser la base de donnée avec la configuration
config = {
"apiKey": "AIzaSyBJuBybYOoxrlweSw05TkT0PLLpd9Hyn44",
"authDomain": "matricule-93889.firebaseapp.com",
"databaseURL": "https://matricule-93889-defaultrtdb.firebaseio.com",
"projectId": "matricule-93889",
"storageBucket": "matricule-93889.appspot.com",
"messagingSenderId": "862010294517",
"appId": "1:862010294517:web:ff734fc6111de988a105bc"
};
firebase = pyrebase.initialize_app(config)
print("initialized")
storage = firebase.storage()
database = firebase.database()
print("finished initialization")
while True:
rawCapture = PiRGBArray(camera, size=(640,480))
for frame in camera.capture_continuous(rawCapture,
format="bgr", use_video_port=True):
image = frame.array
cv2.imshow("Frame", image) #aficher l’image capturée dans
l’écran
key = cv2.waitKey(1) & 0xFF
rawCapture.truncate(0)
if dst1 <= 15:
text = pytesseract.image_to_string(image)
#faire le traitement d’image
#la fonction (image_to_string) renvoi la sortie non modifiees sous
forme du #chaine a partir du tesseract OCR
# enregistriment des données
print("started registering")
identificateur = int(list(database.get().val())[-1][-1])
print(identificateur)
identificateur+=1
data = {"matricule "+str(identificateur): text}
# mis à jour la base de donnée sans supprimer la
derniere valeur
database.update(data)
print("registered data : "+text)
break
cv2.destroyAllWindows()