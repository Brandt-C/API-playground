import requests as r
from random import randrange


# utility for segmenting large character lists in episode/location classes
def divider(arr, num):
    for x in range(0, len(arr), num):
        yield arr[x:x + num]

# basic setup for the character class that will be used throughout the page
class Char:
    def __init__(self, name, status, species, gender, origin, image, id):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.image = image
        self.id = id

# setup for loading/storing characters
class CharDict:
    def __init__(self):
        self.chars = {}
    
    # method for api call to add a single character
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

    # method for getting a single random character, called everytime the page loads
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

    # method for calling up to 20 characters with one api call
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

# establishing the attributes of the episode itself and associated characters
class Episode:
    def __init__(self):
        self.name = None
        self.air_date = None
        self.episode = None
        self.chars_list = []
        self.chars = None

    # api call to get/collate data for an episode
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
    # utility for viewing aspects of the class, used mostly for testing        
    def view_ep(self):
        print(f'{self.name}, {self.air_date}, \n{self.chars_list}, \n{self.chars}')

# establishing attributes and characters for building out a location
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
    
# created a class to deal with changing the text of the bio section on landing page
class Bio():
    def __init__(self):
        self.nt = {'xs' : "Brandt work computer",
            'tldr' : "Brandt likes building funcitonal things with tech!",
            'l' : "Brandt enjoys the functional aspect of creating things on and off of the web that benefit the end user.  He really likes working with APIs (hence the title on your tab at the top here).  This space serves as his playground to show some of what he can do!",
            'xl' : "Brandt enjoys the functional aspect of creating things on and off of the web that benefit the end user.  He really likes working with APIs (hence the title on your tab at the top here).  This space serves as his playground to show some of what he can do! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            }
        self.t = {'xs' : "Brandt builds full-s",
            "tldr" : "Brandt builds full-stack web applications- like this one!",
            'l' : "Brandt really enjoys the functional aspect of using code to build and create.  This includes sites, apps, software, and some nerdy problem-solving.  He particularly enjoys Python, working with APIs, and being around good people!",
            'xl' : "Brandt really enjoys the functional aspect of using code to build and create.  This includes sites, apps, software, and some nerdy problem-solving.  He particularly enjoys Python, working with APIs, and being around good people!  Here's a bunch of industry buzzwords and technologies that have relevance to him: Python, JavaScript, Bootstrap, Flask, React, DBeaver, SQL, PostgreSQL, Firebase, Jinja, Werkzueg, Psycopg2, SQLAlchemy, Heroku, VS Code, Jupyter notebook, OOP, Pandas, Numpy, Git, HTML, CSS, more.  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. An necis, mi fili, quantilla prudentia mundus regatur. Mi in nulla posuere sollicitudin. Nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum."
        }
    #method allows change or default text to be stored as variable
    def convert(self, tl, l):
        if not tl and l:
            return self.nt['xs']
        elif tl == "I'm NOT techy":
            if l == 'XS':
                return self.nt['xs']
            elif l == 'TL;DR':
                return self.nt['tldr']
            elif l == 'Longer':
                return self.nt['l']
            elif l == 'Really Long':
                return self.nt['xl']
        elif tl == "I'm Techy":
            if l == 'XS':
                return self.t['xs']
            elif l == 'TL;DR':
                return self.t['tldr']
            elif l == 'Longer':
                return self.t['l']
            elif l == 'Really Long':
                return self.t['xl']




