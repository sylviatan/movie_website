#this is to import the webbrowser module from the python library
import webbrowser
class Movie:#name of a class movie
    def __init__(self,title,storyline,poster_image,trailer_youtube_url):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube_url

    def Show_Trailer(self):
         webbrowser.open(self.trailer_youtube_url)