movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def imdb_higher(movie):
    if(movie['imdb']>5.5):
        print("The film '{}' is decent".format(movie['name']))
    else:
        print("The film '{}' is garbage".format(movie['name']))

imdb_higher(movies[4])

def imdb_list(movies):
    higher_list=[]
    for i in range(0, len(movies)):
        if movies[i]['imdb'] > 5.5:
            higher_list.append(movies[i]['name'])
    print(higher_list)


imdb_list(movies)

def category_check(movies, category):
    category_list = []
    for i in range(0, len(movies)):
        if movies[i]['category'] == category:
            category_list.append(movies[i]['name'])
    if len(category_list) != 0:
        print(category_list)
    else: print("No such category.")

category_check(movies, 'Thriller')

def avg_imdb(movies):
    avg_score = 0
    tot_movies = len(movies)
    for i in movies:
        avg_score = avg_score + i['imdb']
    avg_score = avg_score / tot_movies
    print("The average IMDB ranking for this movie list is {}".format(avg_score))

avg_imdb(movies)

def avg_category(movies, category):
    category_list = []
    for i in range(0, len(movies)):
        if movies[i]['category'] == category:
            category_list.append(movies[i]['imdb'])
    if len(category_list) != 0:
        sum = 0
        for i in range(0, len(category_list)):
            sum += category_list[i]
        avg = sum / int(len(category_list))
        print("The average IMDB ranking for {} category list is {}".format(category, avg))
    else: print("No such category.")


avg_category(movies, 'Thriller')