def add_cast(db):
    dict = {}

    title_basics = db["title_basics"]
    name_basics = db["name_basics"]
    title_principals = db["title_principals"]

    # find if exists in basics
    nid = input("Enter a person id: ")
    foundp = False
    for match in name_basics.find({"nconst": nid}):
        foundp = True
        print("Found", match)
    if not foundp:
        print("Person Id does not exist.")
        return

    # find if exists in title
    tid = input("Enter a title id: ")
    foundt = False
    for match in title_basics.find({"tconst": tid}):
        foundt = True
        print("Found", match)
    if not foundt:
        print("Person Id does not exist.")
        return

    if foundt and foundp:
        dict["tconst"] = tid
        for x in title_principals.aggregate(
            [
                {"$match": {"tconst": tid}},
                {"$project": {"ordering": {"$toInt": "$ordering"}}},
                {"$sort": {"ordering": -1}},
                {"$limit": 1},
            ]
        ):
            dict["ordering"] = str(x["ordering"] + 1)
        dict["nconst"] = nid
        category = ''
        while len(category) == 0:
            category = input("Enter a category: ").strip()
        dict["category"] = category

        dict["job"] = None
        dict["characters"] = None

        ans = input("Do you want to add this principle? Y/N: ")
        if ans.upper() == "Y":
            title_principals.insert_one(dict)
