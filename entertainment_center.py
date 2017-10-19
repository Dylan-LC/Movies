import fresh_tomatoes
import media

# Toy Story movie: movie title, storyline, director,
# release date, post image and movie trailer
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that comes to life",
                        "John Lasseter",
                        "November 22, 1995",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")  # NOQA

# Avatar movie: movie title, storyline, director,
# release date, post image and movie trailer
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "James Cameron",
                     "December 18, 2009",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")  # NOQA

# Matrix movie: movie title, storyline, director,
# release date, post image and movie trailer
matrix = media.Movie("Matrix",
                     "The one Neo begin to save the real world",
                     "Lana Wachowski, Lilly Wachowski",
                     "March 31, 1999",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")  # NOQA

# Harry Potter movie: movie title, storyline, director,
# release date, post image and movie trailer
harry_potter = media.Movie("Harry Potter",
                           "The novels chronicle the life of "
                           "a young wizard, Harry Potter, " 
                           "and his friends Hermione Granger and Ron Weasley, " 
                           "all of whom are students at Hogwarts School of "
                           "Witchcraft and Wizardry",
                           "Chris Columbus",
                           "November 14, 2001",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=VyHV0BRtdxo")  # NOQA

# Saving Private Ryan movie: movie title, storyline, director,
# release date, post image and movie trailer
saving_private_ryan = media.Movie("Saving Private Ryan",
                                  "Captain John Miller takes his men behind "
                                  "enemy lines to find Private James Ryan, "
                                  "whose three brothers have "
                                  "been killed in combat",
                                  "Steven Spielberg",
                                  "July 24, 1998",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=zwhP5b4tD6g")  # NOQA

# The Lord of the Rings III movie: movie title, storyline, director,
# release date, post image and movie trailer
the_lord_of_the_rings_iii = media.Movie("The Lord of the Rings: "
                                        "The Return of the King",
                                        "Hobbits Frodo and Sam reach Mordor "
                                        "in their quest to destroy the `one ring', "
                                        "while Aragorn leads the forces of good "
                                        "against Sauron's evil army "
                                        "at the stone city of Minas Tirith",
                                        "Peter Jackson",
                                        "December 17, 2003",
                                        "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=y2rYRu8UW8M")  # NOQA

movies = [toy_story, avatar, matrix, harry_potter, saving_private_ryan, the_lord_of_the_rings_iii]
fresh_tomatoes.open_movies_page(movies)

