import random

class People:
    def __init__(self, eyeColor, skinColor, hairColor):
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.hairColor = skinColor
class EuropeanPeople(People):
    def __init__(self, country):
        People.__init__(self, 'blue', 'white', 'blond')
        self.country = country

    def goodAtArtSport(self):
        print('%s good at Art and Sport!' % self.country)

    def __str__(self):
        return "%s people have %s eye, %s skin, %s hair" % (self.country, self.eyeColor, self.skinColor, self.hairColor)

class AsianPeople(People):
    def __init__(self, country):
        People.__init__(self, 'black', 'yellow', 'black')
        self.country = country

    def goodAtMath(self):
        print('%s good at Math!' % self.country)

    def __str__(self):
        return "%s people have %s eye, %s skin, %s hair" % (self.country, self.eyeColor, self.skinColor, self.hairColor)


swedishPeople = EuropeanPeople('Sweden')
print(swedishPeople)

japanesePeople = AsianPeople('Japanese')
print(japanesePeople)

class EuroAsianPeople(EuropeanPeople, AsianPeople):
    def __init__(self, motherCountry, fatherCountry):
        self.country = "%s - %s" % (motherCountry, fatherCountry)
        self.eyeColor = random.choice(['blue', 'black', 'dark blue'])
        self.skinColor = random.choice(['pink', 'white', 'yellow'])
        self.hairColor = random.choice(['blond', 'black', 'red'])

japaneseSwedish = EuroAsianPeople('Japanese', 'Swedish')

print(japaneseSwedish)


