
class Movie
  def initialize(movie_title, movie_storyline, poster_image, trailer_youtube_url)
    @movie_title = movie_title
    @movie_storyline = movie_storyline
    @poster_image = poster_image
    @trailer_youtube_url = trailer_youtube_url
  end

  def movie_title
   puts @movie_title
  end

  def movie_storyline
    puts @movie_storyline
  end

  def poster_image
    puts @poster_image
  end

  def trailer_youtube_url
    puts @poster_image
  end

  def show_trailer
    system("open '#{@trailer_youtube_url}'")
  end
end