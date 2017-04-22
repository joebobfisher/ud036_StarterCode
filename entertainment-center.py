"""entertainment-center.py is licensed under the same terms as python 2.7."""

# Class from Udacity that acts as the front-end.
import fresh_tomatoes

# YOUR class (media.py)
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)
