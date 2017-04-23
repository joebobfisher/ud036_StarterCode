"""media.py is licensed under the same terms as python 2.7."""

# needed for Movie.show_trailer()
import webbrowser

class Movie():
    """Movie provides a way to store movie-related information.
    
    Attributes:
        VALID_RATINGS: a dict of allowed ratings strings for movies
            (PG, R, etc.), each which points to an image for that rating.
    """

    # Allowed ratings that we might need to use later.
    VALID_RATINGS = {"G": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/RATED_G.svg/1200px-RATED_G.svg.png",  # NOQA
                     "PG": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/RATED_PG.svg/1200px-RATED_PG.svg.png",  # NOQA
                     "PG-13": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/RATED_PG-13.svg/1200px-RATED_PG-13.svg.png",  # NOQA
                     "R": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/RATED_R.svg/1200px-RATED_R.svg.png"}  # NOQA

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube_url,
                 rating):
        """Creates a Movie object.

        Args:
            movie_title: A string containing the title of the movie.
            movie_storyline: A string containing a one-sentence summary or
                tagline.
            poster_image: A link to an image file that can be used for the
                movie's poster.
            trailer_youtube_url: A link to the movie's trailer on youtube.
            rating: A string containing the movie's MPAA rating.
        """
        self.title                  = movie_title
        self.storyline              = movie_storyline
        self.poster_image_url       = poster_image
        self.trailer_youtube_url    = trailer_youtube_url
        self.rating                 = rating
        
        # If the user passed us an invalid rating, default to "R".
        # Yes, this is harsh, but better than defaulting to "G"...
        try:
            self.rating_image_url = Movie.VALID_RATINGS[rating]
        except KeyError:
            self.rating           = "R"
            self.rating_image_url = Movie.VALID_RATINGS["R"]

    def show_trailer(self):
        """Shows the trailer listed in the Movie object."""
        webbrowser.open(self.trailer_youtube_url)
