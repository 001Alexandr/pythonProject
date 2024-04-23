class Human:
    _name: str
    __location: str
    age: int

    def __init__(self, v_name='Ivan'):
        self._name = v_name
        self.__location = 'Moscow'
        self.age = 30

    def get_name(self):
        return self._name

    def get_location(self):
        return f'name: {self._name}, location : {self.__location}'

    def set_location(self, location):
        self.__location = location

class Children(Human):

    def __init__(self, v_name='Ivan'):
        super().__init__(v_name)
        self.age = 8

class Buss:
    __children: list
    def __init__(self, children: list):
        self.__children = children

    def add_children(self, children: list):
        self.__children = self.__children + children

    def remove_children(self, children: list):
        for one_children in children:
            if one_children in self.__children:
                self.__children.remove(one_children)

    def print_location_children(self):
        for one_children in self.__children:
            print(one_children.get_location())

    def go_to_new_location(self, new_location):
        for one_children in self.__children:
            one_children.set_location(new_location)

ch1 = Children('Vasia')
ch2 = Children('Petia')
ch3 = Children()
ch4 = Children('Popik')

# print(ch1.get_location())
# print(ch2.get_location())
# print(ch3.get_location())

print('-----------------------')

one_buss = Buss([ch1, ch2, ch3])

one_buss.print_location_children()
print('-----------------------')
one_buss.go_to_new_location('Orenburg')
one_buss.print_location_children()
one_buss.add_children([ch4])
print('-----------------------')
one_buss.remove_children([ch1])
one_buss.print_location_children()





