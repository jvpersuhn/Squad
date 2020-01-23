import sys
sys.path.append('C:/Users/900152/Documents/Dados/Squad')
from controller.sgbd_controller import SGBD, SGBD_controller



sgbd = SGBD_controller()

lista = sgbd.select_all()

for p in lista:
    print(p)