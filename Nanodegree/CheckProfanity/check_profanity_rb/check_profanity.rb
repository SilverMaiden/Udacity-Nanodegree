require 'net/http'
require 'json'


def read_text()
  movie_quotes = File.read('/Volumes/Macintosh HD/Users/SilverMaiden/Downloads/movie_quotes.txt')
  check_profanity(movie_quotes)

end

def check_profanity(text_to_check)
  query = "select *"
  url = "http://www.purgomalum.com/service/containsprofanity?text=" + text_to_check
  response = Net::HTTP.get_response(URI.parse(url))
  output = response.body
  if output == "true"
    puts "Profanity Alert!!!"
  elsif output == "false"
    puts "No Profanity Detected."
  else
    puts "Could Not Properly Check Document."
  end

end

read_text