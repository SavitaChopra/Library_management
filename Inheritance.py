#single inheritance
class happy():
    def one(self):
        print('hello')

class joy(happy):
    def two(self):
        print('bye')

j=joy()
j.one()
j.two()

#multilevel inheritance
class happy():
    def one(self):
        print('hello')

class smile(happy):
    def three(self):
        print('world')

class joy(smile):
    def two(self):
        print('bye')

j=joy()
j.one()
j.three()
j.two()

#multiple inheritance
class happy():
    def one(self):
        print('hello')

class smile():
    def three(self):
        print('world')

class joy(smile,happy):
    def two(self):
        print('bye')

j=joy()
j.one()
j.three()
j.two()

#hierarchical inheritance
class happy():
    def one(self):
        print('hello')

class smile(happy):
    def three(self):
        print('world')

class joy(happy):
    def two(self):
        print('bye')

j=joy()
j.one()
j.two()
s=smile()
s.three()
s.one()

#hybrid inheritance
class happy():
    def one(self):
        print('hello')

class smile(happy):
    def three(self):
        print('world')

class toy(happy):
    def four(self):
        print('queen')

class joy(smile,toy):
    def two(self):
        print('bye')

j=joy()
j.one()
j.three()
j.two()
j.four()

#multipath inheritance
class happy():
    def one(self):
        print('hello')

class smile(happy):
    def three(self):
        print('world')

class toy(happy):
    def four(self):
        print('queen')

class joy(smile,toy):
    def two(self):
        print('bye')

j=joy()
j.one()
j.three()
j.two()
j.four()