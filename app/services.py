import requests as r
from random import randrange

def divider(arr, num):
    for x in range(0, len(arr), num):
        yield arr[x:x + num]

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
    def __init__(self):
        self.name = None
        self.air_date = None
        self.episode = None
        self.chars_list = []
        self.chars = None

    def load_ep(self, ep):
        response = r.get('https://rickandmortyapi.com/api/episode/' + str(ep))
        if response.status_code == 200:
            data = response.json()
            self.name = data['name']
            self.air_date = data['air_date']
            self.episode = data['episode']
            chars = []
            for c in data['characters']:
                chars.append(int(c[42::]))
            segmented_char_list = list(divider(chars, 20))
            self.chars_list = segmented_char_list
            epChars = CharDict()
            for x in self.chars_list:
                epChars.add_mult_char(x)
            self.chars = epChars
            
    def view_ep(self):
        print(f'{self.name}, {self.air_date}, \n{self.chars_list}, \n{self.chars}')

class Location:
    def __init__(self):
        self.name = None
        self.type = None
        self.dimension = None
        self.residents_list = []
        self.residents = None

    def load_loc(self, loc):
        response = r.get('https://rickandmortyapi.com/api/location/' + str(loc))
        if response.status_code == 200:
            data = response.json()
            self.name = data['name']
            self.type = data['type']
            self.dimension = data['dimension']
            chars = []
            for c in data['residents']:
                chars.append(int(c[42::]))
            segmented_char_list = list(divider(chars, 20))
            self.residents_list = segmented_char_list
            epChars = CharDict()
            for x in self.residents_list:
                epChars.add_mult_char(x)
            self.residents = epChars
    