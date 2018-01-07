import socket
from wifi import Cell, Scheme

#lista de sites que tentarei me conectar para ver se a net funciona
confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

def check_host():
   '''Retorna verdadeiro ou falso para a coneção com a internet'''
   global confiaveis
   for host in confiaveis:
	 a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 a.settimeout(.5)
	 try:
	   b=a.connect_ex((host, 80))
	   if b==0: #ok, conectado
		 return True
	 except:
	   pass
	 a.close()
   return False

def listar_wifis():
	'''Retorna uma lista com os nomes das redes ao alcance.'''
	redes=[]
	cells = Cell.all('wlp2s0')
	for cell in cells:
		redes.append(cell.ssid)
	return redes

while True:
	redes = listar_wifis()
	print('Escolha a sua rede.')
	for i in range(len(redes)):
		print('{}.{}'.format(i, redes[i]))
	
	try:	
		my_rede = int(input('Rede:'))
		my_rede = redes[my_rede]
	except (ValueError, IndexError):
		print('Opção inválida.')
		continue
	
	break




while True:
	funcionando = check_host()
	
	
