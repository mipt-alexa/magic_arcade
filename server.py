import BattleField_class as bf
import Mage_class as mg
import connection as con
import tkinter as tk
import time
from Spell_book import spell_book

root = tk.Tk()
DT = 10


def read_message():
    list_of_messages = con.read_message('server')
    return list_of_messages


class IdGiver:
    def __init__(self):
        self.id_list = [0]

    def new_id(self):
        self.id_list.append((self.id_list[len(self.id_list) - 1] + 1) % 1000000)
        return self.id_list[len(self.id_list) - 1]


class GameApp:
    def __init__(self, field_width, field_height):
        self.id_giver = IdGiver()
        self.field_width = field_width
        self.field_height = field_height
        self.battle_filed = bf.BattleField(field_width, field_height, self.id_giver)
        self.mage1 = mg.Mage(0, 0, self.id_giver.new_id())
        self.action_state = 'walk'
        self.mage2 = mg.Mage(field_height - 1, field_width - 1, self.id_giver.new_id())
        self.game_status = 'none'

    def initialise_game(self):
        for i in range(self.field_height):
            for j in range(self.field_width):
                if self.battle_filed.field[i][j].type == 'Cell':
                    message = 'obj ' + str(self.battle_filed.field[i][j].client_id) + ' ' + str(i) + ' ' + str(j) + ' ' + 'grey'
                    con.write_message("server", message)
        message = 'obj ' + str(self.mage1.client_id) + ' ' + str(self.mage1.x) + ' ' + str(self.mage1.y) + ' ' + 'red'
        con.write_message('server', message)
        message = 'obj ' + str(self.mage2.client_id) + ' ' + str(self.mage2.x) + ' ' + str(self.mage2.y) + ' ' + 'red'
        con.write_message('server', message)
        self.game_status = 'player1_turn'
        message = 'set_turn ' + 'player1'
        con.write_message('server', message)


    def process_click_message(self, turn, splitted_message):
        click_x = int(splitted_message[1])
        click_y = int(splitted_message[2])
        if self.action_state == 'walk':
            if turn == 'player1':
                if self.mage1.check_move(click_x, click_y):
                    self.mage1.move(click_x - self.mage1.x, click_y - self.mage1.y)
                    message = 'obj ' + str(self.mage1.client_id) + ' ' + str(self.mage1.x) + ' ' + str(self.mage1.y) + ' ' + 'red'
                    con.write_message('server', message)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message('server', message)
            if turn == 'player2':
                if self.mage2.check_move(click_x, click_y):
                    self.mage2.move(click_x - self.mage2.x, click_y - self.mage2.y)
                    message = 'obj ' + str(self.mage2.client_id) + ' ' + str(self.mage2.x) + ' ' + str(self.mage2.y) + ' ' + 'red'
                    con.write_message('server', message)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message('server', message)
        if self.action_state[:2] == 'sp':
            spell_number = int((self.action_state.split())[1])
            spell = spell_book[spell_number]
            if turn == 'player1':
                spell_target = None
                if click_x == self.mage2.x and click_y == self.mage2.y:
                    spell_target = self.mage2
                if self.battle_filed.obstacles[click_y][click_x] is not None:
                    spell_target = self.battle_filed.obstacles[click_y][click_x]
                if spell_target is not None:
                    print(self.mage1.check_spell(spell, self.battle_filed.obstacles, spell_target))
                    if self.mage1.check_spell(spell, self.battle_filed.obstacles, spell_target):
                        print("@")
                        self.mage1.cast_spell(spell)
                        self.mage2.catch_spell(spell)
                        print(self.mage2.health)
                        message = 'set_health ' + 'player2 ' + str(self.mage2.health)
                        con.write_message('server', message)
                        message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                        con.write_message('server', message)
                        message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                        con.write_message('server', message)
                else:
                    print("WRONGCELL")
            if turn == 'player2':
                if True or self.mage2.check_spell(spell, self.battle_filed.obstacles):
                    print("@")
                    self.mage2.cast_spell(spell)
                    self.mage1.catch_spell(spell)
                    print(self.mage1.health)
                    message = 'set_health ' + 'player1 ' + str(self.mage1.health)
                    con.write_message('server', message)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message('server', message)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message('server', message)

    def process_key_message(self, splitted_message):
        if splitted_message[1] == '0':
            self.action_state = 'walk'
        elif splitted_message[1] == 't':
            if self.game_status == 'player1_turn':
                self.game_status = 'player2_turn'
                message = 'set_turn ' + 'player2'
                con.write_message('server', message)
                self.mage1.energy = min(self.mage1.energy + 80, mg.BASIC_ENERGY)
                message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                con.write_message('server', message)
            elif self.game_status == 'player2_turn':
                self.game_status = 'player1_turn'
                message = 'set_turn ' + 'player1'
                con.write_message('server', message)
                self.mage2.energy = min(self.mage2.energy + 80, mg.BASIC_ENERGY)
                message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                con.write_message('server', message)
        else:
            self.action_state = 'spell ' + str(splitted_message[1])

    def update(self):
        message_list = read_message()
        for message in message_list:
            print(message)
            if message == '':
                continue
            splitted_message = message.split()
            if self.game_status == 'player1_turn':
                if splitted_message[0] == 'click':
                    self.process_click_message('player1', splitted_message)
                if splitted_message[0] == 'key':
                    self.process_key_message(splitted_message)

            elif self.game_status == 'player2_turn':
                splitted_message = message.split()
                if splitted_message[0] == 'click':
                    self.process_click_message('player2', splitted_message)
                if splitted_message[0] == 'key':
                    self.process_key_message(splitted_message)
        root.after(DT, self.update)


game = GameApp(10, 10)
game.initialise_game()
game.update()
root.mainloop()
