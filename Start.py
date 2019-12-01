import Server
import Main_2_players
import Main_1_player

"""
Отвечает за запуск игры
"""

select_regime()
def select_regime():
    print('Выберете режим: 1- игра на 2 людей (2), 2- игра на одного с ботом (1)')
    answer = input()
    print('Какова ширина поля (ввести целое число >1)')
    width = input()
    print('Какова длина поля (ввести целое число >1)')
    height = input()
    if answer == '2':
        Main_2_players.initialization(Server.starting_connection())
        Server.start_to_paint(width, height) 
        #TODO
    if answer == '1':
        Main_1_player.initialization(width, height)
        #TODO
    