import BattleField_class as bf
import Mage_class as mg
import connection as con
import tkinter as tk
import time
from Spell_book import spell_book
from random import choice



root = tk.Tk()
DT = 50


def read_message(conn):
    list_of_messages = con.read_message(conn)
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
        self.battle_field = bf.BattleField(field_width, field_height, self.id_giver)
        self.mage1 = mg.Mage(0, 0, self.id_giver.new_id())
        self.mage1.image_id = 'mage1'
        self.action_state = 'walk'
        self.mage2 = mg.Mage(field_height - 1, field_width - 1, self.id_giver.new_id())
        self.mage2.image_id = 'mage2'
        self.game_status = 'none'

    def initialise_game(self):
        start_connection = con.start_connection_server()
        self.conn_1 = start_connection[0]
        self.conn_2 = start_connection[1]
        for i in range(self.field_height):
            for j in range(self.field_width):
                if self.battle_field.field[i][j].type == 'Cell':
                    message = 'obj ' + str(self.battle_field.field[i][j].client_id) + ' ' + str(j) + ' ' + str(i) + ' ' \
                              + self.battle_field.field[i][j].image_id
                    con.write_message_server(self.conn_1, self.conn_2, message)
        message = 'obj ' + str(self.mage1.client_id) + ' ' + str(self.mage1.x) + ' ' + str(self.mage1.y) + ' ' + \
                  self.mage1.image_id
        con.write_message_server(self.conn_1, self.conn_2, message)
        message = 'obj ' + str(self.mage2.client_id) + ' ' + str(self.mage2.x) + ' ' + str(self.mage2.y) + ' ' + \
                  self.mage2.image_id
        con.write_message_server(self.conn_1, self.conn_2, message)
        self.game_status = choice(['player1_turn', 'player2_turn'])
        if self.game_status == 'player2_turn':
            message = 'set_turn ' + 'player2'          
        else:
            message = 'set_turn ' + 'player1'
        con.write_message_server(self.conn_1, self.conn_2, message)
        """
        Заготовка для сообщения об определении стороны клиенту
        con.write_side_of_client(conn_1, 1)
        con.write_side_of_client(conn_2, 2)
        """

        
    def attack(self, turn, spell, click_x, click_y):
        if turn == 'player1':
            spell_target = None
            if click_x == self.mage2.x and click_y == self.mage2.y:
                spell_target = self.mage2
            if self.battle_field.obstacles[click_y][click_x] is not None:
                spell_target = self.battle_field.obstacles[click_y][click_x]
            if self.battle_field.obstacles[click_y][click_x] is not None:
                spell_target = self.battle_field.obstacles[click_y][click_x]
            if spell_target is not None and spell_target.type == 'Mage':
                print(self.battle_field.obstacles)
                if self.mage1.check_spell(spell, self.battle_field.obstacles, spell_target, self.mage2):
                    self.mage1.cast_spell(spell)
                    self.mage2.catch_spell(spell)
                    message = 'set_health ' + 'player2 ' + str(self.mage2.health)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    if self.mage2.health <= 0:
                        message = 'del ' + str(self.mage2.client_id)
                        con.write_message_server(self.conn_1, self.conn_2, message)
                        message = 'end_game player1'
                        con.write_message_server(self.conn_1, self.conn_2, message)
                        self.game_status = 'end_game'
            elif spell_target is not None and spell_target.type == 'Obstacle':
                if self.mage1.check_spell(spell, self.battle_field.obstacles, spell_target):
                    self.mage1.cast_spell(spell)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    is_broken = self.battle_field.obstacles[click_y][click_x].take_damage(spell.health_damage)
                    if is_broken:
                        message = 'del ' + str(self.battle_field.obstacles[click_y][click_x].client_id)
                        con.write_message_server(self.conn_1, self.conn_2, message)
                        self.battle_field.delete_obstacle(click_x, click_y)

        if turn == 'player2':
            spell_target = None
            if click_x == self.mage1.x and click_y == self.mage1.y:
                spell_target = self.mage1
            if self.battle_field.obstacles[click_y][click_x] is not None:
                spell_target = self.battle_field.obstacles[click_y][click_x]
            if spell_target is not None and spell_target.type == 'Mage':
                if self.mage2.check_spell(spell, self.battle_field.obstacles, spell_target, self.mage1):
                    print("@")
                    self.mage2.cast_spell(spell)
                    self.mage1.catch_spell(spell)
                    print(self.mage1.health)
                    message = 'set_health ' + 'player1 ' + str(self.mage1.health)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    if self.mage1.health <= 0:
                        message = 'del ' + str(self.mage1.client_id)
                        con.write_message_server(self.conn_1, self.conn_2, message)
                        message = 'end_game player2'
                        con.write_message_server(self.conn_1, self.conn_2, message)
                        self.game_status = 'end_game'
            elif spell_target is not None and spell_target.type == 'Obstacle':
                if self.mage2.check_spell(spell, self.battle_field.obstacles, spell_target):
                    self.mage2.cast_spell(spell)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    is_broken = self.battle_field.obstacles[click_y][click_x].take_damage(spell.health_damage)
                    if is_broken:
                        message = 'del ' + str(self.battle_field.obstacles[click_y][click_x].client_id)
                        con.write_message_server(self.conn_1, self.conn_2, message)
                        self.battle_field.delete_obstacle(click_x, click_y)

    def defend(self, turn, spell, click_x, click_y):
        print("defend")
        if turn == 'player1':
            if self.mage1.check_spell(spell, self.battle_field.obstacles, self.battle_field.field[click_y][click_x],
                                      self.mage2):
                self.mage1.cast_spell(spell)
                message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                con.write_message_server(self.conn_1, self.conn_2, message)
                self.battle_field.create_obstacle(click_x, click_y, self.id_giver, spell.obstacle_health)
                print(self.battle_field.obstacles[click_y][click_x])
                message = 'obj ' + str(self.battle_field.obstacles[click_y][click_x].client_id) + ' ' + str(click_x) + \
                          ' ' + str(click_y) + ' ' + self.battle_field.obstacles[click_y][click_x].image_id
                con.write_message_server(self.conn_1, self.conn_2, message)
        elif turn == 'player2':
            if self.mage2.check_spell(spell, self.battle_field.obstacles, self.battle_field.field[click_y][click_x],
                                      self.mage2):
                self.mage2.cast_spell(spell)
                message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                con.write_message_server(self.conn_1, self.conn_2, message)
                self.battle_field.create_obstacle(click_x, click_y, self.id_giver, spell.obstacle_health)
                print(self.battle_field.obstacles[click_y][click_x])
                message = 'obj ' + str(self.battle_field.obstacles[click_y][click_x].client_id) + ' ' + str(click_x) + \
                          ' ' + str(click_y) + ' ' + self.battle_field.obstacles[click_y][click_x].image_id
                print(message)
                con.write_message_server(self.conn_1, self.conn_2, message)

    def process_click_message(self, turn, splitted_message): 
        click_x = int(splitted_message[1])
        click_y = int(splitted_message[2])
        if self.action_state == 'walk':
            if turn == 'player1':
                if self.mage1.check_move(click_x, click_y, self.battle_field.obstacles, self.mage2):
                    self.mage1.move(click_x - self.mage1.x, click_y - self.mage1.y)
                    message = 'obj ' + str(self.mage1.client_id) + ' ' + str(self.mage1.x) + ' ' + str(self.mage1.y) \
                              + ' ' + self.mage1.image_id
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'animate ' + str(self.mage1.client_id) + ' ' + str(self.mage1.x) + ' ' + str(
                        self.mage1.y) + ' ' + str(500)
                    con.write_message_server(self.conn_1, self.conn_2, message)
            if turn == 'player2':
                if self.mage2.check_move(click_x, click_y, self.battle_field.obstacles, self.mage1):
                    self.mage2.move(click_x - self.mage2.x, click_y - self.mage2.y)
                    message = 'obj ' + str(self.mage2.client_id) + ' ' + str(self.mage2.x) + ' ' + str(self.mage2.y) \
                              + ' ' + self.mage2.image_id
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    message = 'animate ' + str(self.mage2.client_id) + ' ' + str(self.mage2.x) + ' ' + str(
                        self.mage2.y) + ' ' + str(500)
                    con.write_message_server(self.conn_1, self.conn_2, message)
        if self.action_state[:2] == 'sp':
            spell_number = int((self.action_state.split())[1])
            spell = spell_book[spell_number]
            if spell.spell_type == 'attack_directed':
                self.attack(turn, spell, click_x, click_y)
            elif spell.spell_type == 'defend_directed':
                self.defend(turn, spell, click_x, click_y)

    def process_key_message(self, turn, splitted_message):
        if len(splitted_message) > 1:
            if splitted_message[1] == '0':
                self.action_state = 'walk'
                message = 'del_range_circle'
                con.write_message_server(self.conn_1, self.conn_2, message)
                message = 'set_action ' + '0'
                con.write_message_server(self.conn_1, self.conn_2, message)
            elif splitted_message[1] == 't':
                message = 'del_range_circle'
                con.write_message_server(self.conn_1, self.conn_2, message)
                self.action_state = 'walk'
                if self.game_status == 'player1_turn':
                    self.game_status = 'player2_turn'
                    message = 'set_turn ' + 'player2'
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    self.mage1.energy = min(self.mage1.energy + 80, mg.BASIC_ENERGY)
                    message = 'set_energy ' + 'player1 ' + str(self.mage1.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
                elif self.game_status == 'player2_turn':
                    self.game_status = 'player1_turn'
                    message = 'set_turn ' + 'player1'
                    con.write_message_server(self.conn_1, self.conn_2, message)
                    self.mage2.energy = min(self.mage2.energy + 80, mg.BASIC_ENERGY)
                    message = 'set_energy ' + 'player2 ' + str(self.mage2.energy)
                    con.write_message_server(self.conn_1, self.conn_2, message)
            elif ord(splitted_message[1][0]) - ord('0') >= 1 and ord(splitted_message[1][0]) - ord('0') <= 9:
                message = 'del_range_circle'
                con.write_message_server(self.conn_1, self.conn_2, message)
                self.action_state = 'spell ' + str(splitted_message[1])
                spell_number = int((self.action_state.split())[1])
                spell = spell_book[spell_number]
                message = 'set_action ' + str(spell_number)
                con.write_message('server', message)
                if spell.spell_type == 'attack_directed' or spell.spell_type == 'defend_directed':
                    if turn == 'player1':
                        message = 'draw_range_circle ' + str(self.mage1.x) + ' ' + str(self.mage1.y) + ' ' + str(
                            spell.spell_range)
                        con.write_message_server(self.conn_1, self.conn_2, message)
                    elif turn == 'player2':
                        message = 'draw_range_circle ' + str(self.mage2.x) + ' ' + str(self.mage2.y) + ' ' + str(
                            spell.spell_range)
                        con.write_message_server(self.conn_1, self.conn_2, message)

    def update(self):
        message_client_1 = read_message(self.conn_1)
        message_client_2 = read_message(self.conn_2)
        splitted_message__client_1 = message_client_1.split()
        splitted_message__client_2 = message_client_2.split()
        if self.game_status == 'player1_turn':
            if message_client_1 == '':
                pass
            elif splitted_message__client_1[0] == 'click':
                self.process_click_message('player1', splitted_message__client_1)
            elif splitted_message__client_1[0] == 'key':
                self.process_key_message('player1', splitted_message__client_1)
        elif self.game_status == 'player2_turn':
            if message_client_2 == '':
                pass
            elif splitted_message__client_2[0] == 'click':
                self.process_click_message('player2', splitted_message__client_2)
            elif splitted_message__client_2[0] == 'key':
                self.process_key_message('player2', splitted_message__client_2)
        root.after(DT, self.update)


game = GameApp(15, 15)
game.initialise_game()
game.update()
root.mainloop()
