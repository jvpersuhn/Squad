import sys
sys.path.append('C:/Users/900143/Desktop/Squad')
from controller.sgbd_controller import SGBD, SGBD_controller
from controller.squad_controller import Squad, SquadController

s = Squad(0,'aaaa','aaa',3)
s.sgbd = 1
s.linguagemBack = 1
s.linguagemFront = 1

print(s)

sc = SquadController()

sc.insert(s)