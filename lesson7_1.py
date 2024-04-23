class Human:
    age: int
    __name: str
    __location: str


    def __init__(self, v_name='Kolia'):
        self.age = 30
        self.__name = v_name
        self.__location = 'Moscow'
    def get_location(self):
        return f'name: {self.__name}, location: {self.__location}'
    def set_location(self, location):
        self.__location = location



class Children(Human):
    def __init__(self, v_name='Glasha'):
        super().__init__(v_name)
        self.age = 8

o_ch1 = Children('Tom')
o_ch2 = Children('Alice')
o_ch3 = Children('Bob')


###ДОДЕЛАТЬ!!!!!
class Buss:
    __chil: list
    def __init__(self, chil: list):
        self.__chil = chil

    def add_chil(self):
        a = input('Как зовут ребенка которого добавляем? -')
        ch = Children(a)
        ###Как проверить текущую локацию детей и добавить сюда????
        self.__chil.append(ch)
    ###Удаление не фунциклирует
    def del_chil(self, ch: list):
        #a = str(input('Как зовут ребенка которого убираем? -'))
        for ch in self.__chil:
            self.__chil.remove(ch)


    def see_info(self):
        for i in self.__chil:
            print(f'Дети в автобусе {i.get_location()}')

    def go_to_new_location(self, location: str):
        for i in self.__chil:
            i.set_location(location)

    def mesto(self):
        # key = self.chil
        a=1
        d1 = dict.fromkeys(self.__chil, a+1)

        # for key in self.chil:
        #     d1[key] += 1

        for i in self.__chil:
            d1[i] += 1
        print(d1)

o_buss1 = Buss([o_ch1, o_ch2, o_ch3])
# o_buss1.see_info()
# print('______________________')
o_buss1.go_to_new_location('YpeNroi')
o_buss1.see_info()
print('______________________')
o_buss1.del_chil(o_ch1)
o_buss1.see_info()