class Human:
    hands: int
    foots: int
    head: int
    eyes: int
    age: int
    sex: int
    name: str


    def __init__(self, v_name='Kolia'):
        self.hands = 2
        self.foots = 2
        self.head = 2
        self.eyes = 2
        self.age = 30
        self.sex = 1
        self.name = v_name

    def voin(self):
        self.hands = self.hands/2
        self.foots = self.foots/2
        self.eyes = self.eyes/2

    def see_info(self):
        print(f'name = {str(self.name)}')
        print(f'hands = {str(self.hands)}')
        print(f'foots = {str(self.foots)}')
        print(f'head = {str(self.head)}')
        print(f'eyes = {str(self.eyes)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')

class Children(Human):
    def __init__(self, v_name='Glasha'):
        super().__init__(v_name)
        self.sex = 0
    def see_info(self):
        super().see_info()
o_ch1 = Children('Tom')
o_ch2 = Children('Alice')
o_ch3 = Children('Bob')



ch1 = [o_ch1.name, o_ch2.name, o_ch3.name]

class Buss:
    def __init__(self):
        self.chil = []

    def add_chil(self):
        a = input('Как зовут ребенка которого добавляем? -')
        self.chil.append(a)

    def del_chil(self):
        a = str(input('Как зовут ребенка которого убираем? -'))
        for i in self.chil:
            if i == a:
                self.chil.remove(i)

    def auto_add_chil(self, list):
        self.chil.extend(list)


    def see_info(self):
        print(f'Дети в автобусе {str(self.chil)}')

    def mesto(self):
        # key = self.chil
        a=1
        d1 = dict.fromkeys(self.chil, a+1)

        # for key in self.chil:
        #     d1[key] += 1

        for i in self.chil:
            d1[i] += 1
        print(d1)

o_buss1 = Buss()
o_buss1.auto_add_chil(ch1)
o_buss1.see_info()
o_buss1.mesto()