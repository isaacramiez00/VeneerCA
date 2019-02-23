#Veneer Project
#Credits to Code Academy

class Art:
    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium
        self.owner = owner

    def __repr__(self):
        return '%s. %s. %s. %s. %s, %s' % (self.artist, self.title, 
        self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
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

    def sell_artwork(self, artwork, price):
        #price is in USD Millions
        if artwork.owner == self:
            new_listing = Listing(artwork.title, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)
            

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '%s. %s' % (self.art, self.price)



moma = Client("The MOMA", "New York", True)
edytta = Client("Edytta Halpirt", "Private Collection", False)
veneer = Marketplace()
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
edytta.sell_artwork(girl_with_mandolin, 6)


#executes repr() method and added owner argument
#print(girl_with_mandolin)

#executes none rn, since we have nothing, therefore good
#print(veneer.show_listing())

#executes repr() method
# print(moma, edytta)

#returns none; fix
#print(veneer.show_listing())

#moma.buy_artwork(girl_with_mandolin)

#print(girl_with_mandolin)