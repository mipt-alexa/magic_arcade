#! /usr/bin/env python
# -*- coding: utf-8 -*-
import Spell_classes as sp
"""
AttackDirectSpell params: name, energy, menu_image_id, sound, spell_range, health_damage, energy_damage, destination
DefendDirectSpell params: name, energy, menu_image_id, sound,  spell_range, obstacle_health
"""
spell_book = []
for i in range(4):
    spell_book.append(None)
spell_book[1] = sp.AttackDirectSpell('fireball', 50, 'fireball', 'fire1', 20, 20, 0, 'Both')
spell_book[2] = sp.AttackDirectSpell('ice spike', 50, 'ice spike', 'energy', 8, 10, 40, 'Mage')
spell_book[3] = sp.DefendDirectSpell('wall', 30, 'wall spell', 'stone', 10, 30)