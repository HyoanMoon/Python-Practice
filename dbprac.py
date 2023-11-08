from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.qoukjqr.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

all_users = list(db.users.find({},{'_id':False}))