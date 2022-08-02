import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://abhijeet:oracle123@cluster0.klhwzkg.mongodb.net/?retryWrites=true&w=majority")
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

# client = pymongo.MongoClient("mongodb+srv://ineuron:<password1>@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)
