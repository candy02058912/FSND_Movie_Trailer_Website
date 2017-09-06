import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

piglets_big_movie = media.Movie("Piglet's Big Movie",
                                "When Piglet comes up missing his Hundred Acre Wood friends use Piglet's own Book of Memories to find him, discovering along the way just how big a role he's played in their lives.",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Piglets_big_movie_teaser.jpg/220px-Piglets_big_movie_teaser.jpg",
                                "https://www.youtube.com/watch?v=wgbU7gfpxTw")

snowman = media.Movie("Snowman",
                      "Detective Harry Hole investigates the disappearance of a woman whose pink scarf is found wrapped around an ominous-looking snowman.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDg1NjYyMTEyOF5BMl5BanBnXkFtZTgwNzY4MDMyMzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=BF2Ksrxu_QY")

winnie_the_pooh = media.Movie("Winnie the Pooh",
                              "While searching for honey, Pooh and his friends embark on an adventure to find Eeyore's missing tail and rescue Christopher Robin from an unknown monster called, The Backson.",
                              "https://upload.wikimedia.org/wikipedia/en/e/e2/Winnie_the_Pooh_Poster.jpg",
                              "https://www.youtube.com/watch?v=hRT86ZggCEk")

the_tigger_movie = media.Movie("The Tigger Movie",
                               "Tigger goes looking through the hundred-acre-wood to find his family.",
                               "https://upload.wikimedia.org/wikipedia/en/1/13/The_Tigger_Movie_film.jpg",
                               "https://www.youtube.com/watch?v=Lssr92pk_9I")

poohs_heffalump_movie = media.Movie("Pooh's Heffalump Movie",
                                    "A heffalump is heard trumpeting in the hundred acre woods. Winnie the Pooh, Tigger, and Piglet are scared and rush to Rabbit's house for advice.",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Poohs_heffalump_movie.jpg/220px-Poohs_heffalump_movie.jpg",
                                    "https://www.youtube.com/watch?v=eLW2vzKfhMc")

movie_list = [toy_story, snowman, piglets_big_movie, winnie_the_pooh, the_tigger_movie, poohs_heffalump_movie]
fresh_tomatoes.open_movies_page(movie_list)
