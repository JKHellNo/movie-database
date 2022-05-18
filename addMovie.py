def add_movie(db):
    dict = {}

    col = db["title_basics"]
    correctInput = False 
    while (not correctInput):
        id = input("Enter a unique id or /back: ").strip()
        if id == '/back':
            return
        if len(id) != 0:
            correctInput = True

    unique = True
    for match in col.find({"tconst": id}):
        unique = False
        print("This id is already associated with another movie:\n", match)
    if unique:  # enter in information for each column
        dict["tconst"] = id
        dict["titleType"] = "movie"
        title = ""
        while len(title) == 0:
            title = input("Enter title: ")

        dict["primaryTitle"] = title
        dict["originalTitle"] = dict["primaryTitle"]
        dict["isAdult"] = None
        entered = False
        while not entered:
            try:  # lmao because the toJson function keeps them as strings lol
                dict["startYear"] = str(int(input("Enter start year: ").split()[0]))
                entered = True
            except:
                print("Please enter a number.")
        dict["endYear"] = None
        entered = False
        while not entered:
            try:
                dict["runtimeMinutes"] = str(int(input("Enter runtime: ").split()[0]))
                entered = True
            except:
                print("Please enter a number.")

        dict["genres"] = input("Enter genres: ").split()

        ans = input("Do you want to add this movie? Y/N: ")
        if ans.upper() == "Y":
            col.insert_one(dict)
