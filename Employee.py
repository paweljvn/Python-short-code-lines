class Employee(object):


    annual rise == 0.05


    def __init__ (self, imie, stanowisko, pensja):

        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja

        @classmethod
        def ustaw_podwyzke(cls, wartosc):
            if cls.annual_rise + wartosc < cls.annual_rise < cls.annual_rise * 1.1:
                cls.annuaL_rise = wartosc

            else:
                cls.roczna_podwyzka = cls.roczna_podwyzka * 1.08


if pesel ok
    create employee


@staticmethod
def sprawdz_pesel (pesel):
    if len (pesel) != 11:
        return False
    return True