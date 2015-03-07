import fresh_tomatoes

class Movie:
    trailer_youtube_url = ''
    title = '' 
    poster_image_url = ''
    notables = []
    def __init__(self, trailer_youtube_url, title, poster_image_url, notables):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
        self.notables = notables

# Create expected list for fresh_tomatoes.py::open_movies_page        
movie_list = [];

movie_list.append(Movie('https://www.youtube.com/watch?v=B16Bo47KS2g',
                        'Guardians of the Galaxy',
                        'http://www.blackfilm.com/read/wp-content/uploads/2014/06/Guardians-of-the-Galaxy-poster-Star-Lord.jpg',
                        ['Chris Pratt', 'Zoe Saldana']));
movie_list.append(Movie('https://www.youtube.com/watch?v=T50_qHEOahQ',
                        'The Last Samurai',
                        'http://cdn.traileraddict.com/content/warner-bros-pictures/lastsamurai.jpg',
                        ['Tom Cruise', 'Ken Watanabe']));
movie_list.append(Movie('https://www.youtube.com/watch?v=M3YVTgTl-F0',
                        'Big Fish',
                        'https://www.movieposter.com/posters/archive/main/15/MPW-7681',
                        ['Ewan McGregor']));
movie_list.append(Movie('https://www.youtube.com/watch?v=Shjcd1xqEng',
                        'Moulin Rouge',
                        'http://www.4barewalls.co.uk/wp-content/uploads/600full-moulin-rouge-poster.jpg',
                        ['Ewan McGregor','Nicole Kidman','Jim Broadbent']));
movie_list.append(Movie('https://www.youtube.com/watch?v=kAMUv22y1og',
                        'The Book of Eli',
                        'http://screencrave.com/wp-content/uploads/2009/11/book-of-eli-poster-25-11-09-kc.jpg',
                        ['Denzel Washington', 'Mila Kunis']));
movie_list.append(Movie('https://www.youtube.com/watch?v=enJYNuWBJ9g',
                        'Troy',
                        'https://www.movieposter.com/posters/archive/main/19/MPW-9840',
                        ['Brad Pitt', 'Sean Bean', 'Orlando Bloom', 'Eric Bana']));

# Pass Movie list to HTML-generating Python script
fresh_tomatoes.open_movies_page(movie_list);
