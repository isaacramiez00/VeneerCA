#Veneer Project
#Credits to Code Academy

class Art:
    def __init__(self, artist, title, year, medium):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium

    def __repr__(self):
        return """{artist}. "{title}". {year}, {medium}.""".format(artist=self.artist,
        title=self.title, year=self.year, medium=self.medium)

class Marketplace:
    def __init__(self, listings):
        #listings = []
        self.listings = listings

    def add_listing(self, new_listing):
        self.new_listing = []
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.expired_listing = []
        self.listings.remove(expired_listing)
        
    def show_listing(self):
        for i in self.listings:
            return i

class Client:
    def __init__(self, name, location, is_museum):
        #person
        self.name = name
        #name of the location of the museum or "Private Collection" 
        # if the client is a collector.
        self.location = location
        #boolean value
        #museum = True
        #collector = False
        self.is_museum = is_museum

    def __repr__(self):
        return "{name}; {location}; {is_museum}.".format(name=self.name,
        location=self.location, is_museum=self.is_museum)


moma = Client("The MOMA", "New York", True)
edytta = Client("Edytta Halpirt", "Private Collection", False)
veneer = Marketplace([])
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas")

#executes repr() method
#print(girl_with_mandolin)

#executes none rn, since we have nothing, therefore good
#print(veneer.show_listing())

#executes repr() method
# print(moma, edytta)