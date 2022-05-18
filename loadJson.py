import pymongo
import json

# "localhost", int(input("port: "))
def collectionmaker(db):

    db.name_basics.drop()
    db.title_basics.drop()
    db.title_principals.drop()
    db.title_ratings.drop()

    name_basics = db["name_basics"]
    title_basics = db["title_basics"]
    title_principals = db["title_principals"]
    title_ratings = db["title_ratings"]

    filenames = [
        "name.basics.json",
        "title.basics.json",
        "title.principals.json",
        "title.ratings.json",
    ]

    for filename in filenames:
        print("loading " + filename + "...")
        with open(filename) as file:
            file_data = json.load(file)
        # lmao no switch statements
        if filename == "name.basics.json":
            name_basics.insert_many(file_data)

        elif filename == "title.basics.json":
            title_basics.insert_many(file_data)

        elif filename == "title.principals.json":
            title_principals.insert_many(file_data)

        elif filename == "title.ratings.json":
            title_ratings.insert_many(file_data)
        file.close()
