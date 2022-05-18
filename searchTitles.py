def search_movie_titles(db):
    col = db["title_basics"]
    user_input = input("Titles:")  # this is for the first search function
    tconst_title = []  # list index or count or index result
    num = 0
    user_input = user_input.split()

    for inputs in user_input:  # for every keyword, for loop resset query, run everything underneath
        query = {'primaryTitle': {"$regex": inputs, "$options": 'i'}}  # regex to search, options=case insensitive
        result = col.find(query)  # delete find_one for just find instead and uncomment the for loop underneath
        for match in result:  # insert after variable result
            num += 1
            print(num, match)
            tconst_title.append(match['tconst'])
        if(num == 0):
            print("No results found.")
            return
        try:
            int(input)  # see if input is an integer,    need to change all "user_input" back into just input
        except:
            pass
        else:
            query = {'startYear': {"$eq": inputs}}
            results = col.find(query)  # replace find_one for find and use the for loop underneath
            for match in results:  # insert after variable result
                num += 1
                print(num, match)
                tconst_title.append(match['tconst'])

        correctInput = False
        while (not correctInput):
            try:
                title_num = input("Enter the number of a movie title you would like to know more about or go 'back': ")
                title_num = int(title_num)
                correctInput = True
            except:
                if (title_num == 'back'):
                    return
        
        index = title_num - 1
        movie_tconst = tconst_title[index]

        ratings = db["title_ratings"]  # search for averageRating and numVotes of a movie title
        query = {'tconst': movie_tconst}
        rating = ratings.find_one(query)
        avg_rating = str(rating['averageRating'])
        numVotes = str(rating['numVotes'])
        print("The average rating is: " + avg_rating + " and the number of votes is: " + numVotes + ".")

        cast = db["title_principals"]
        pi = db["name_basics"]
        query = {'tconst': movie_tconst}
        crew = cast.find(query)

        for member in crew:
            nconst = member['nconst']
            character = member['characters']
            query = {'nconst': nconst}
            person = pi.find_one(query)
            name = person['primaryName']
            if (character != None):  # when a cast does play a character
                print(name, "plays as", character[0])
            else:
                print(name)