import fresh_tomatoes
import media

"""This program will open a web page consisting of
movie tiles. On clilcking a tile, trailer of that
movie will be played.
9 instances of class Movie are created
and details of the movies are send as arguments
while creating the instances.
Details are - movie name, poster image url, and
trailer url.
"""

# Creating 9 instances of the class Movie
toy_story = media.Movie(
    "Toy Story",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" , # noqa
    "https://www.youtube.com/watch?v=vwyZH85NQC4") # noqa 
avatar = media.Movie(
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # noqa
    "http://www.youtube.com/watch?v=-9ceBgWV8io") # noqa
dangal = media.Movie(
    "Dangal",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg", # noqa
    "https://www.youtube.com/watch?v=x_7YlGv9u1g") # noqa
pk = media.Movie(
    "PK",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQSSaD2bSPOgmgsn4-09dF2l8mHbuvHhJxbkL7rvD1uEpAxKnLX", # noqa
    "https://www.youtube.com/watch?v=0cziEi0rWmc") # noqa
inception = media.Movie(
    "Inception",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=8hP9D6kZseM") # noqa
the_dark_knight = media.Movie(
    "The Dark Knight",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", # noqa
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q") # noqa
the_matrix = media.Movie(
    "The Matrix",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", # noqa
    "https://www.youtube.com/watch?v=m8e-FF8MsqU") # noqa
terminator_genisys = media.Movie(
    "Terminator Genisys",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG", # noqa
    "https://www.youtube.com/watch?v=62E4FJTwSuc")# noqa
the_avengers = media.Movie(
    "The Avengers",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", # noqa
    "https://www.youtube.com/watch?v=eOrNdBpGMv8") # noqa

# Creating a list of movies                      
movies=[toy_story,avatar,dangal,pk,inception,the_dark_knight,
        the_matrix,terminator_genisys,the_avengers]
# Opening a web page consting of movies in the list
fresh_tomatoes.open_movies_page(movies)
