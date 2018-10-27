class Animal(object):

    def __init__(self, name):
        self.name = name

        # empty object


    def move(self):
        print(f' {self.name} moved')



class Horse(Animal):
    def __init__ (self, name, color):

        super().__init__(name)

    def move(self):
        print (f'Horse {self.name} run')

    def jump(self, how_high):
        if how_high > 5:
            print(f'Horse {self.name} jumped high')
        else:
            print (f'Horse {self.name} jumped low')



class Donkey(Animal):

    def __init__(self, stubborn, owner, hungry):
        self.hungry = hungry
        self.owner = owner
        self.stubborn
        super().__init__('unknown')

    def move(self):
        if self.stubborn > 8:
            print('Donkey is stubborn. won\'t move')

        else:
            print('Donkey moved a bit')

class Mule(Horse, Donkey):
    def __init__(self, name, owner):
        super().__init__(name, color)



#if __name__ == '__main__':

    #print (Mule.__mro__)
    #e_mule = Mule('Stefan', 'czarny')
    #print (e_mule.name)
