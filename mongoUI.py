import pymongo
import loadJson
import tsvToJson
import searchTitles
import searchGenres
import searchCast
import addMovie
import addCast

port = int(input("port: "))
client = pymongo.MongoClient("localhost", port)
db = client["291db"]


def phase1(db):
    tsvToJson.run()
    loadJson.collectionmaker(db)


def displayMenu(menu):
    print("Options 1-5 or 'exit': ")
    for key in menu:
        print(str(key) + ": " + menu[key].__name__)


def main():
    exitStatus = False
    phaseStatus = 0

    menu = {
        1: searchTitles.search_movie_titles,
        2: searchGenres.search_genres,
        3: searchCast.search_cast_members,
        4: addMovie.add_movie,
        5: addCast.add_cast
    }

    while not exitStatus:
        try:
            phaseStatus = input("Run phase 1 or 2 or 'exit': ").split()[0]
        except:
            pass
        if phaseStatus == "exit":
            exitStatus = True
            break

        if phaseStatus == "1":
            phase1(db)
            phaseStatus = "2"

        while phaseStatus == "2":

            displayMenu(menu)
            command = None
            try:
                command = input("> ").split()[0]
                menu[int(command)](db)
            except Exception as e:
                if command == None:
                    pass
                elif command == "exit":
                    exitStatus = True
                    break
                else:
                    print(e)
    client.close()

if __name__ == "__main__":
    main()
