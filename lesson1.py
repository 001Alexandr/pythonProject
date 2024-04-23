# list_1 = [1,2,3,'a','q','red']
# list_2 = [1,2,3,4,5, 'a', 'q', 'b', 'c', 'reaqtre']
# for a in list_2:
#     if len(str(a)) > 5:
#         print(a)

# list_sum = list_1 + list_2
# list_unique = []
# for i in list_sum:
#     if i not in list_unique:
#         list_unique.append(i)
#
# d1 = {
#     1: 'abc',
#     2: 98,
#     'qrew': 23
# }
#
# d2 = {
#     'ew': 124,
#     'ewqr': 'qqq'
# }
#
# d1['nes'] = d2
# #
# # print(d1)
# # print(d1.get('nes').get('ew'))
#
# print(d1.keys())
# print(d1.values())

# def s(name, lastname, otch='Александрович'):
#     return f'surname is {name}, last name is {lastname}, otchextvo is {otch}'
# print(s('Петр','Сидоров'))
# def a():
#     return f'Красавчик, жи есть!'
#
# for i in [1,2,3,'a','q','red']:
#     print(i)
#     if i == 'a':
#         print(a())
#         break
#

# def s(list):
#     while len(list) != 0:
#         for a in list:
#             print(a)
#     return a

# sch = len(l1)
# #while sch != 0:
# for i in range(lenght):
#     for a in range(0, lenght-i-1):
#         if l1[a] > l1[i]:
#             temp1=l1[a]
#             #temp2=l1[i]
#             l1[a]=l1[a+1]
#             l1[a+1]=temp1
#             print(l1)
#     #sch= sch-1
#     #print(sch)
#
# print(l1)
###__________________________________
###СОРТИРОВКА ПУЗЫРЬКОМ
# l1 = [4, 2, 6, 1, 5, 3, 7, 9, 8]
# lenght = len(l1)
#
# def sort(array):
#     for i in range(lenght):
#         print(i)
#         for j in range(0, lenght-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#     return array
#
# print(sort(l1))
###__________________________________

# class Human:
#     hands: int
#     foots: int
#     head: int
#     eyes: int
#     age: int
#     sex: int
#     name: str
#
#
#     def __init__(self, v_name='Kolia'):
#         self.hands = 2
#         self.foots = 2
#         self.head = 2
#         self.eyes = 2
#         self.age = 30
#         self.sex = 1
#         self.name = v_name
#
#     def voin(self):
#         self.hands = self.hands/2
#         self.foots = self.foots/2
#         self.eyes = self.eyes/2
#
#     def see_info(self):
#         print(f'name = {str(self.name)}')
#         print(f'hands = {str(self.hands)}')
#         print(f'foots = {str(self.foots)}')
#         print(f'head = {str(self.head)}')
#         print(f'eyes = {str(self.eyes)}')
#         print(f'age = {str(self.age)}')
#         print(f'sex = {str(self.sex)}')
#
# class Woman(Human):
#     def __init__(self, v_name='Glasha'):
#         super().__init__(v_name)
#         self.sex = 0
#     def see_info(self):
#         super().see_info()
#
#
# # o_vasia = Human('Vasia')
# #
# # o_vasia.voin()
# # o_vasia.see_info()
#
# # o_masha = Woman('Masha')
# # o_masha.see_info()
#
# class Animal:
#     head: int
#     paws: int
#     mustache: int
#     tail: int
#     name: str
#     def __init__(self, v_paws, v_name):
#         self.head = 1
#         self.mustache = 20
#         self.tail = 1
#         self.paws = v_paws
#         self.name = v_name
#
#     def see_info(self):
#         print(f'name - {str(self.name)}')
#         print(f'head - {str(self.head)}')
#         print(f'paws - {str(self.paws)}')
#         print(f'mustache - {str(self.mustache)}')
#         print(f'tail - {str(self.tail)}')
# # o_kot1 = Animal(4, 'Vasilii')
# # o_kot1.see_info()

ch1 = ['Tom', 'Alice', 'Robert']
class Buss:
    def __init__(self):
        self.chil = []

    def add_chil(self):
        sch = int(input('Сколько детей добавляем?'))
        while sch != 0:

            a = input('Как зовут ребенка которого добавляем? -')
            self.chil.append(a)
            sch=sch-1

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

        #for i in self.chil:
        #    d1[]
        print(d1)



o_buss1 = Buss()
o_buss1.add_chil()
o_buss1.see_info()


