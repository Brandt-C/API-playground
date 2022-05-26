import requests as r
from random import randrange



class Char:
    def __init__(self, name, status, species, gender, origin, image, id):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.image = image
        self.id = id

class CharDict:
    def __init__(self):
        self.chars = {}
    
    def add_1_char(self, id):
        response = r.get('https://rickandmortyapi.com/api/character/' + str(id) + "/")
        if response.status_code == 200:
            data = response.json()
        name = data['name']
        status = data['status']
        species = data['species']
        gender = data['gender']
        origin = data['origin']['name']
        image = data['image']
        id = data['id']
        new_char = Char(name, status, species, gender, origin, image, id)
        self.chars[id] = new_char    

    def add_rand_char(self):
        x = randrange(1, 826)
        response = r.get('https://rickandmortyapi.com/api/character/' + str(x) + "/")
        if response.status_code == 200:
            data = response.json()
        name = data['name']
        status = data['status']
        species = data['species']
        gender = data['gender']
        origin = data['origin']['name']
        image = data['image']
        id = data['id']
        new_char = Char(name, status, species, gender, origin, image, id)
        self.chars[id] = new_char 

    def add_mult_char(self, arr):
        response = r.get('https://rickandmortyapi.com/api/character/' + str(arr))
        if response.status_code == 200:
            data = response.json()
        for x in range(len(arr)):
            name = data[x]['name']
            status = data[x]['status']
            species = data[x]['species']
            gender = data[x]['gender']
            origin = data[x]['origin']['name']
            image = data[x]['image']
            id = data[x]['id']
            new_char = Char(name, status, species, gender, origin, image, id)
            self.chars[id] = new_char 
    
class Episode:
    def __init__(self, name, air_date, episode):
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.chars = {}

class EpisodeBuilder:
    def __init__(self):
        self.eps = {}

    def load_ep(self, ep):
        response = r.get('https://rickandmortyapi.com/api/episode/' + str(ep))
        if response.status_code == 200:
            data = response.json()
        name = data['name']
        air_date = data['air_date']
        episode = data['episode']
        chars = {}
        for c in data['characters']:
            chars[int(c[42::])] = None
        new_epi = Episode(name, air_date, episode)
        new_epi.chars = chars
        self.eps[ep] = new_epi
        
    def view_eps(self):
        for e in self.eps.values():
            print(f'{e.name}, {e.air_date}, \n{e.chars.keys()}')
    
    def load_ep_chars(self, arr):
        if len(arr) <= 20:
            pass







    




        