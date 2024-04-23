import datetime as d

class Soldat:
    name: str
    age: int


    def __init__(self, v_name='Oleg', v_age=18, o_date = d.date(year=1111, month=1, day=1)):
        self.age = v_age
        self.name = v_name
        self.date = o_date

    #def Value_error(self):

    def see_info(self):
        return f'Имя: {self.name}, Возраст: {self.age}, ДР: {self.date}'
    # def remowe_sold(self, sold: str):
    #     for i in

class Rota:
    def __init__(self, rota: list, v_number = 0):
        self.rota = rota
        self.number = v_number

    def add_rota(self):
        n = [input(f'Как зовут солдата которого добавляем? ')]
        a = [input(f'Сколько лет солдату? ')]


    def auto_add_rota(self, rota: list):
        self.rota = self.rota + rota
    def remove_rota(self, rota: list):
        for one_sold in rota:
            if one_sold in self.rota:
                self.rota.remove(one_sold)
    def see_rota(self):
        a=1
        for i in self.rota:
            print(f' Рота №{self.number}, Солдат №{a}, {i.see_info()}')
            a = a + 1
        print(f'Колличество людей в роте - {a-1}')
class Polk:
    def __init__(self, polk: list, v_namber = 0):
        self.polk = polk
        self.number = v_namber
    def add_polk(self, polk: list):
        self.polk = self.polk + polk

    def remove_polk(self, polk: list):
        for one_sold in polk:
            if one_sold in self.polk:
                self.polk.remove(one_sold)
    def see_polk(self):
        print(f'В полку состоят роты')
        for i in self.polk:
            i.see_rota()








