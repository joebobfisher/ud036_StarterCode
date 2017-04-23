"""entertainment-center.py is licensed under the same terms as python 2.7."""

# Module from Udacity that acts as the front-end.
import fresh_tomatoes

# YOUR class (media.py)
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "http://www.youtube.com/watch?v=vwyZH85NQC4",
                        "G")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     "PG-13")

rogue_one = media.Movie("Rogue One: A Star Wars Story",
                        "The Rebel Alliance makes a risky move to steal the " +
                        "plans for the Death Star, setting up the epic saga " +
                        "to follow.",
                        "http://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # NOQA
                        "http://www.youtube.com/watch?v=DLzxrzFCyOs",
                        "PG-13")

movies = [toy_story, avatar, rogue_one]

fresh_tomatoes.open_movies_page(movies)
