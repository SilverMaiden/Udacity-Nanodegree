require './media'

toy_story = Movie.new("Toy Story", "A story of a boy and his toys that come to life.",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = Movie.new("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

atomic_blonde = Movie.new("Atomic Blonde",
                            "Superspies",
                            "https://upload.wikimedia.org/wikipedia/en/b/b5/Atomic_Blonde_poster.jpg",
                            "https://www.youtube.com/watch?v=yIUube1pSC0")


atomic_blonde.movie_title
avatar.poster_image
toy_story.movie_storyline
#atomic_blonde.show_trailer
