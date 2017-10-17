import urllib


def read_text():
    movie_quotes = open("/Volumes/Macintosh HD/Users/SilverMaiden/Downloads/movie_quotes.txt")
    contents_of_file = movie_quotes.read()
    movie_quotes.close()
    check_profanity(contents_of_file)
    #print(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + text_to_check)
    output = connection.read()
    if output == "true":
        print("Profanity Alert!!")
    elif output == "false":
        print("No Profanity Detected.")
    else:
        print("Could Not Scan Document Properly.")

   # print(output)
    connection.close()

read_text()