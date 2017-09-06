import webbrowser

class Movie():
    """
    Information for making Movie tiles on the webpage.

    Attributes:
        movie_title: A string indicating the movie title.
        movie_storyline: A string indicating the movie storyline.
        poster_img_url: A string with the url for the movie poster.
        trailer_youtube_url: A string with the url for the youtube trailer.    
    """

    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
