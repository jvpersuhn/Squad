import sys
sys.path.append('C:/Users/900143/Desktop/Squad')
from controller.sgbd_controller import SGBD, SGBD_controller
from controller.squad_controller import Squad, SquadController

sc = SquadController()

s = sc.select_all()

for i in s:
    print(i)
    