#creating a movie list containing single tuples
#include movie title, directors name
#release year

movie_list = [
    ("title: ", "jugle fairy"),
    ("director: ", "Ronald"),
    ("release year: ","2003")

]

movie_title = input("enter a movie title: ");
directors_name = input("enter directors name: ");
release_year = input("enter the release year: ");

new_turple = [
    ("title: ",movie_title),
    ("director: ", directors_name),
    ("released: ", release_year),
]

print(new_turple );

print(f'the movie {movie_title} was released in {release_year}\n'),
print(f'{movie_title}, {release_year}')

print(movie_list.append(new_turple));