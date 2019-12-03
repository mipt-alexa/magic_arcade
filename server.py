import BattleField_class as bf
import connection as con
FIELD_WIDTH = 10
FIELD_HEIGHT = 10
battle_filed = bf.BattleField(FIELD_WIDTH, FIELD_HEIGHT, 0)
for i in range(FIELD_HEIGHT):
    for j in range(FIELD_WIDTH):
        if battle_filed.field[i][j].type == "Cell":
            s = str(i)+' '+str(j) + ' ' + "grey"
            con.write_messages("server", s)






