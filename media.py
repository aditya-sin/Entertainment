import webbrowser

""" Project 1: Movie Website
    Date Started:25/12/2016
    Date Completed: 29/12/2016
    Submissted by: Aditya Singh
"""

""" Description: This file creates the Class Movie which
    is used to create multiple
    instances of movies having following attributes:
    1. Name of the movie - title
    2. URL of the poster - poster_image_url
    3. URL of the trailer - trailer_youtube_url
"""

class Movie():
    
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function to open trailer of the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
