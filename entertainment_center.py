import fresh_tomatoes
import media

""" 
This is the file responsible for initializing the Movie Class
with the necessary data.
It fills up the Movie Class with some dummy data to be shown in the 
browser.
"""

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", 
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://www.foxmovies.com/movies/avatar/download-poster/251",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock", "Storyline", 
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

another_avatar = media.Movie("Avatar", "A marine on an alien planet",
                             "http://www.foxmovies.com/movies/avatar/download-poster/251",
                             "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

toy_story_2 = media.Movie("Toy Story", "A story of a boy and his toys that come to life", 
                          "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                          "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar_2 = media.Movie("Avatar", "A marine on an alien planet",
                       "http://www.foxmovies.com/movies/avatar/download-poster/251",
                       "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


movies = [toy_story, avatar, school_of_rock, another_avatar, toy_story_2, avatar_2]
fresh_tomatoes.open_movies_page(movies)
