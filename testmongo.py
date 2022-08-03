import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://userid:password@clustername.clustercode.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "mail": "sudhanshu@email.com",
    "surname": "kumar"
}
db1 = client['testmongo']
coll = db1['test']
coll.insert_one(d)

