#! /usr/bin/env python
# -*- coding: utf-8 -*-
import Spell_classes as sp
spell_book = []
for i in range(10):
    spell_book.append(None)
spell_book[1] = sp.AttackDirectSpell('fireball', 50, 10, 20, 0, 'Both')
spell_book[2] = sp.AttackDirectSpell('lighting sphere', 50, 8, 10, 40, 'Mage')
spell_book[3] = sp.DefendDirectSpell('wall', 30, 10, 30)