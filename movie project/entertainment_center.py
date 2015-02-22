import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)
# webbrowser.open(toy_story.poster_image_url)
avatar = media.Movie("Avatar",
                     "A marina on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
ddlj = media.Movie("dilwale dulhania le jayenge",
                   "love",
                   "http://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                   "https://www.youtube.com/watch?v=c25GKl5VNeY")
#print(ddlj.title)
#ddlj.show_trailer()

movies = [toy_story,avatar,ddlj]                     
fresh_tomatoes.open_movies_page(movies)
