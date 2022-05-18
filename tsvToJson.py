import json


def jsonmaker(input_file, output_file):
    print("Serializing " + input_file + "...")
    file = open(input_file, "r", encoding="utf-8")
    chunk = open(output_file, "w", encoding="utf-8")
    chunk.write("[\n")

    headers = file.readline().strip().split()

    line = file.readline()
    dict1 = {}
    for column, data in zip(headers, line.split("\t")):

        # Convert each row into dictionary with keys as titles
        nested = ["primaryProfession", "knownForTitles", "genres", "characters"]

        if "\\N" in data:
            dict1[column] = None
        elif any(x in column for x in nested):
            dict1[column] = data.strip().split(",")
        else:
            dict1[column] = data.strip()

    # and dump into file.
    chunk.write(json.dumps(dict1, indent=4))

    for line in file:
        dict = {}
        for column, data in zip(headers, line.split("\t")):

            # Convert each row into dictionary with keys as titles
            nested = ["primaryProfession", "knownForTitles", "genres", "characters"]

            if "\\N" in data:
                dict[column] = None
            elif any(x in column for x in nested):
                dict[column] = data.strip().split(",")
            else:
                dict[column] = data.strip()

        # we will use strip to remove '\n'.

        # we will append all the individual dictionaires into list
        # and dump into file.
        chunk.write("," + json.dumps(dict, indent=4))
    chunk.write("\n]")
    chunk.close()
    file.close()


# Driver Code
def run():

    input_filename = [
        "name.basics.tsv",
        "title.basics.tsv",
        "title.principals.tsv",
        "title.ratings.tsv",
    ]
    for filename in input_filename:
        output_filename = filename.replace("tsv", "json")
        jsonmaker(filename, output_filename)
