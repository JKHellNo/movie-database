def search_genres(db):
    db["title_basics"].create_index("tconst")
    db["title_ratings"].create_index("tconst")
    col = db["title_basics"]
   
    correctInput = False
    while (not correctInput):
        try:
            genre = input("What genre are you looking for or go 'back': ")
            genre = genre.lower().capitalize()
            if (genre == 'Back'):
                return
            if (len(genre) != 0):
                correctInput = True
        except:
            pass
        
    correctInput = False
    while (not correctInput):
        try:
            min_vote = input("Minimum vote count for the genres or go 'back': ")
            min_vote = int(min_vote)
            correctInput = True
        except:
            if (min_vote == 'back'):
                    return

    movies = col.aggregate(
        [
            {"$match": {"genres": genre}},
            {
                "$project": {
                    "_id": 0,
                    "titleType": 0,
                    "originalTitle": 0,
                    "isAdult": 0,
                    "startYear": 0,
                    "endYear": 0,
                    "runtimeMinutes": 0,
                }
            },
            {
                "$lookup": {
                    "from": "title_ratings",
                    "localField": "tconst",
                    "foreignField": "tconst",
                    "as": "ratings",
                }
            },
            {"$unwind": "$ratings"},
            {"$project": {"ratings._id": 0, "ratings.tconst": 0}},
            {"$match": {"$expr": {"$gt": [{"$toInt": "$ratings.numVotes"}, min_vote]}}},
            {"$sort": {"ratings.averageRating": -1}},
        ]
    )

    for movie in movies:
        print(movie)
