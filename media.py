import webbrowser

class Movie():
  """
  This is the main class responsible to hold the data of each
  Movie trailer, title, storyline, poster, trailer url
  """
  def __init__(self, movie_title, movie_storyline, poster_image,
              trailer_youtube):
    """ the init function responsible for initializing the data
    of each movie 
    """
    self.title = movie_title
    self.movie_storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self):
    """
    this function is called to open a web browser with the trailer
    url as the page content
    """
    webbrowser.open(self.trailer_youtube_url)

