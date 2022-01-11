import pygame
import random
pygame.font.init()

#screen variables
WIDTH,HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FLIPPING GAME USING PYGAME MODULE ! ")
FPS = 60

#font varaibles
NUMBER_FONT = pygame.font.SysFont("Arial Black",40)

#color variables
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)

#game varaibles
tiles = list(range(32))*2
state = {'mark' : None}
show = [True]*64
random.shuffle(tiles)

def Numbering(x,y):
	for count in range(63,-1,-1):
		if (count % 8)*75<x<(count % 8 + 1)*75 and (count//8)*75<y<(count //8 +1)*75:
			return count

def darw_grid():
	rows = 8
	gap = WIDTH//rows
	for i in range(63,-1,-1):
		if show[i]:
			pygame.draw.rect(WIN,GREEN,(gap*(i%8),gap*(i//8),gap-1,gap-1),1)
		else:
			pygame.draw.rect(WIN,BLUE,(gap*(i%8),gap*(i//8),gap,gap))

def reset():
	global show,tiles
	tiles = list(range(32))*2
	state = {'mark' : None}
	show.clear()
	show = [True]*64
	random.shuffle(tiles)

def redraw():
	WIN.fill(BLACK)
	darw_grid()


def main():
	global show
	run = True
	clock = pygame.time.Clock()
	while run :
		clock.tick(FPS)
		redraw()
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mark = state['mark']
				m_x,m_y = pygame.mouse.get_pos()
				spot = Numbering(m_x,m_y)
				if spot != None:
					if mark is None or mark == spot or tiles[mark] != tiles[spot]:
						state['mark'] = spot
					else:
						show[spot] = False
						show [mark] = False
						state['mark'] = None
			mark = state['mark']
		if mark is not None and show[mark]:
			x,y = (mark % 8)*75,(mark // 8)*75
			text = NUMBER_FONT.render(str(tiles[mark]),1,WHITE)
			WIN.blit(text,(x+10,y+10))
		

		if show.count(False) == 64:
			WIN.fill(BLACK)
			text = NUMBER_FONT.render("YOU WON!",1,WHITE)
			WIN.blit(text,(WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
			pygame.display.update()
			pygame.time.delay(1500)
			reset()
		
		pygame.display.update()
	pygame.quit()

if __name__ == '__main__':
	main()
