# ----------------------------------------------------
# ----------------------------------------------------

# MONGODB BASIC - Connection, Databases, Collections,
#                   Insert one/many

# ----------------------------------------------------
# ----------------------------------------------------

# pymongo or mongoengine can be
# used as connectors
import pymongo as mdb

# mongodb connection
client = mdb.MongoClient(host='127.0.0.1', port=27017)
# print(client)

# print databases present in mongodb at present
print(f'\n Databases List : {client.list_database_names()}')

# ----------------------------------------------------

# using database if exists
# creating (virtually) if doesn't exist
# not created until data goes into it
demodb = 'demodb'
db = client[demodb]
# using demodb database

# print collections present in database
print(f'\n Collections in {demodb} : {db.list_collection_names()}')

# ----------------------------------------------------

# using collection if exists
# creating (virtually) if it doesn't exist
# not created until data goes into it
# collections= tables (MySQL)
collection = db['democol']
# using democol collection

# ----------------------------------------------------

# sample data to be inserted
data = {"first_name": "Gawain",
        "last_name": "Foynes",
        "email": "gfoynes0@statcounter.com",
        "gender": "Male"
        }

# insert one document in collection
# document= record/row (MySQL)
ins_one_data = collection.insert_one(data)
# if _id not in dictionary mongodb assigns
# unique id to document (record/row)

print(f'\n Data to be inserted : {data}')
print('\n Inserted Successfully')
print(f'\n Inserted Document ID : {ins_one_data.inserted_id}')
# id for inserted document

# ----------------------------------------------------

# sample data to be inserted
# list of dictionaries
data = [
    {
        "first_name": "Gaven",
        "last_name": "Nichol",
        "email": "gnichol1@vinaora.com",
        "gender": "Male"
    },
    {
        "first_name": "Winona",
        "last_name": "Colebourne",
        "email": "wcolebourne2@google.ru",
        "gender": "Female"
    },
    {
        "first_name": "Roanne",
        "last_name": "Oldale",
        "email": "roldale3@nba.com",
        "gender": "Female"}
]

# insert multiple document in collection
ins_many_data = collection.insert_many(data)
# if _id not in dictionary mongodb assigns
# unique id to document (record/row)

print(f'\n Data to be inserted : {data}')
print('\n Inserted Successfully')
print(f'\n Inserted Document ID : {ins_many_data.inserted_ids}')
# ids for inserted documents
