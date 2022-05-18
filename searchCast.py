def find_id(db):
    nconst_title = []

    col = db["name_basics"]
    correctInput = False
    while (not correctInput):

        user_input = input("Which Cast / Crew Member would you like to search for or go '/back': ").strip()
        if (user_input == '/back'):
            return
        if (len(user_input) != 0):
            correctInput = True
        

    query = {'primaryName': {"$regex": user_input, "$options": 'i'}}
    result = col.find(query)

    num = 0
    for match in result:
        idnum = match['nconst']
        print(f"{num:5}) {match['primaryName']:30} ID :{idnum:15}")
        nconst_title.append(idnum)
        num += 1

    # if cursor empty
    if num == 0:
        # program returns if no results 
        print("No Cast / Crew Found.")
        return

    while(True):
        try:
            user_input = int(input("Enter Index for the Cast/Crew: "))
            nconst = nconst_title[user_input]
        except ValueError:
            print("Incorrect input, Please enter a number. Try again")
        except IndexError:
            print("You have entered the wrong index. Try again")
        except:
            print("Unexpected error. Try again")

        else:
            del nconst_title
            break

    
# printing profession
    query = {'nconst': {"$eq": nconst}}
    result = col.find_one(query)
    print("\n")
    print(f"{'ID':10} {'Name':20} ")
    print(f"{result['nconst']:10} {result['primaryName']:20}")
    print("\nProfessions: ",end=" ")
    for item in result['primaryProfession']:
        print(item.upper(),end="  ")
    print("\n")

    return nconst

def print_all_info(nconst,db):

    # get jobs , title and characters
    col = db["title_principals"]
    query = { 'nconst': { '$eq': nconst } } 
    result = col.find(query)
    for member in result:
        # just incase we print duplicate , we can uncomment to show its not duplicate
        # print(member['_id']) 

        character = member['characters']
        movie_num = member['tconst']
        job= member['job']

        # print movie name
        query = {'tconst': movie_num}
        col = db["title_basics"]
        movie_title = col.find_one(query)

        # cleaning characters
        if character is None: 
            character = 'Plays No charcters'
        else:
            character = character[0].split('"')[1]
        # cleaning jobs
        if job is None: 
            job = 'None'

        # printing all info
        print(f"\n{'Movie ID':10}  |{'Title':30}  |{'JOB':10}  |{'Character Played':25}\n")
        print(f"{movie_num:10}  |{movie_title['primaryTitle'][0:25]:30}  |{job:10}  |{character:25}\n")

    return


def search_cast_members(db):
    idnum = find_id(db)
    print_all_info(idnum,db)
    return