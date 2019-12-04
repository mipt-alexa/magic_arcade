import BattleField_class as bf
import Mage_class as mg
import connection as con
import Cells_classes as c
FIELD_WIDTH = 10
FIELD_HEIGHT = 10
battle_filed = bf.BattleField(FIELD_WIDTH, FIELD_HEIGHT, 0)

for i in range(FIELD_HEIGHT):
    for j in range(FIELD_WIDTH):
        if battle_filed.field[i][j].type == 'Cell':
            s = 'obj ' + str(i) + ' ' + str(j) + ' ' + 'grey'
            con.write_message("server", s)
mage = mg.Mage(0, 0)
s = 'obj ' + str(0) + ' ' + str(0) + ' ' + 'red'
con.write_message("server", s)







