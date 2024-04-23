from datetime import date

import util.util1 as u


o_v1 = u.Soldat('Вася', 23, date(2003, 3, 25))
o_v2 = u.Soldat('Димон')
print(o_v2.see_info())
o_v3 = u.Soldat('Саня', 25)
o_v4 = u.Soldat('Сява', 29)
o_v5 = u.Soldat('Лёха', 26)
print(o_v4.see_info())
print('________________________')
rota1 = u.Rota([o_v1, o_v2],1)
rota2 = u.Rota([o_v3, o_v4, o_v5],2)
rota1.see_rota()
rota2.see_rota()
# print('________________________')
# rota1.remove_rota([o_v1])
# rota1.see_rota()
# print('________________________')
# rota1.auto_add_rota([o_v1])
# rota1.see_rota()
print('________________________')
p1 = u.Polk([rota1, rota2])
p1.see_polk()
rota2.remove_rota([o_v5])
p1.see_polk()
p1.remove_polk([rota2])
p1.see_polk()

#rota1 = ['']




