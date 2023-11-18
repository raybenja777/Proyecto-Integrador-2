#P.###################
#....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################..

nombre = input('Ingrese su nombre')

print('Bienvenido al jueguito del laberinto', (nombre))


import keyboard
from pynput import keyboard as kb

def pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))

with kb.Listener(pulsa) as escuchador:
	escuchador.join()
	if escuchador == keyboard.key.up:
		False
	





    

	
	



		



    
	

