class Zwierz (object):
    def __init__(self, nazwa,):
        self.nazwa = nazwa


    def ruszaj (self):
        print (f'Zwierz {self.nazwa} ruszył się.')


class Czlowiek(Zwierz):

    def __init__(self, imie, wiek):
        super (). __init__(imie, 'kręgowiec')
        # Zwierz. __init__(self, imie)
        self.imie = imie
        self.wiek = wiek

        def ruszaj (self):
            print (f' {self.nazwa} idzie.')

class Student(Czlowiek):
    def __init__ (self, imie, nr_indeksu):
    super ().__init__ (imie, None)
    self.nr_indeksu = nr_indeksu




