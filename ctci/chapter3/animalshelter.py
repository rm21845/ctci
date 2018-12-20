"""Solution to 3.6: Animal Shelter."""


class Animal(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalShelter():
    
    def __init__(self):
        self._cat = list()
        self._dog = list()
        self._number = 0

    def enqueue(self, animal):
        if isinstance(animal, Animal):
            self._number += 1
            if isinstance(animal, Cat):
                self._cat.append((animal, self._number))
            else:
                self._dog.append((animal, self._number))
        else:
            raise ValueError('Must be a Cat or Dog.')

    def dequeue(self):
        if self._cat[0][1] < self._dog[0][1]:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()

    def dequeue_cat(self):
        return self._cat.pop(0)[0]

    def dequeue_dog(self):
        return self._dog.pop(0)[0]

