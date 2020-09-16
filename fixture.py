import json 


out_file = "imdb_out.json"

def create_fixture(file_name):
    pk = 1
    final_fixture = []
    with open(file_name) as data:
        python_file_obj=json.load(data)
    for movie in python_file_obj:    
        movie_model = {'model':'videora.movie', 'pk':pk}
        orig_dict = {'99popularity':'popularity', 'director':'director','imdb_score':'imdb_rating','name':'name','genre':'genre'}
        movie_model['fields'] = dict((orig_dict[key], (str(value)[1:-1] if type(value) == list else value)) for (key, value) in movie.items())
        final_fixture.append(movie_model)
        pk+=1
    with open(out_file, "w") as data:
        json.dump(final_fixture, data)
    print ('Fixture created Sucessfully...')
    return out_file


