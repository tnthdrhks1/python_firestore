import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase-h2e.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'user').document(u'rasp')

for i in range(10):
    doc_ref.update({u'weight{0}'.format(i) : "{0}".format(i)})
