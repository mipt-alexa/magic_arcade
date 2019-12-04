import BattleField_class as bf
import Mage_class as mg
import connection as con
import tkinter as tk
root = tk.Tk()


def catch_message():
    message = con.read_message('client')
    return message


class GameApp:
    def __init__(self, field_width, field_height):
        self.field_width = field_width
        self.field_height = field_height
        self.battle_filed = bf.BattleField(field_width, field_height, 0)
        self.mage1 = mg.Mage(0, 0)
        self.action_state = 'walk'
        self.mage2 = mg.Mage(field_height-1, field_width-1)
        self.game_status = 'none'

    def initialise_game(self):
        for i in range(self.field_height):
            for j in range(self.field_width):
                if self.battle_filed.field[i][j].type == 'Cell':
                    message = 'obj ' + str(i) + ' ' + str(j) + ' ' + 'grey'
                    con.write_message("server", message)
        message = 'obj ' + str(self.mage1.x) + ' ' + str(self.mage1.y) + ' ' + 'red'
        con.write_message('server', message)
        message = 'obj ' + str(self.mage2.x) + ' ' + str(self.mage2.y) + ' ' + 'red'
        con.write_message('server', message)
        self.game_status = 'player1_turn'

    def update(self):
        message_list = catch_message()
        for message in message_list:
            if message != '':
                splitted_message = message.split()
                if self.game_status == 'player1_turn':
                    if splitted_message[0] == 'click':
                        click_x = int(splitted_message[1])
                        click_y = int(splitted_message[2])
                        if self.action_state == 'walk':
                            if self.mage1.check_move(click_x, click_y):
                                self.mage1.move(click_x - self.mage1.x, click_y - self.mage1.y)
                                self.game_status = 'player2_turn'
                    if splitted_message[0] == 'key':
                        key_number = int(splitted_message[1])
                        self.action_state = 'spell' + str(key_number)

                elif self.game_status == 'player2_turn':
                    splitted_message = message.split()
                    if splitted_message[0] == 'click':
                        click_x = int(splitted_message[1])
                        click_y = int(splitted_message[2])
                        if self.action_state == 'walk':
                            if self.mage2.check_move(click_x, click_y):
                                self.mage2.move(click_x - self.mage2.x, click_y - self.mage2.y)
                                self.game_status = 'player1_turn'
                    if splitted_message[0] == 'key':
                        key_number = int(splitted_message[1])
                        self.action_state = 'spell'+str(key_number)
        root.after(10, self.update)


game = GameApp(10, 10)
game.initialise_game()
game.update()
root.mainloop()








