import random
import pygame


pygame.font.init()

#VAR
screen_w, screen_h = 1200, 600
global relative_x, relative_y, relative_w, relative_h, relative_zoom
relative_x, relative_y, relative_w, relative_h, relative_zoom = 0, 0, screen_w, screen_h, 1
last_pos = 0, 0
last_zoom = relative_zoom

objet = {}



fenetre = pygame.display.set_mode((screen_w, screen_h))

img = pygame.image.load("test/2.png")
img2 = pygame.image.load("test/1.jpg")



def add_objet(x, y, w, h, path):
	ide = len(objet)
	objet[ide] = {"x": x, "y": y, "w": w, "h": h}
	img = pygame.image.load(path)
	objet[ide]["img"] = pygame.transform.scale(img, (w, h))


def object_resize_image(ide):
	"""
	Opti futur :
	recharger les images (en haute qualité ou mauvaises selon la situation)
	"""
	obj = objet[ide]
	print(relative_zoom)
	obj["img"] = pygame.transform.scale(obj["img"], (int(obj["w"]*1/relative_zoom), int(obj["h"]*1/relative_zoom)))


def update_screen(x=relative_x, y=relative_y, w=relative_w, h=relative_h):
	global relative_x, relative_y, relative_w, relative_h, relative_zoom, last_zoom
	#print("X : " + str(relative_x) + " Y : " + str(relative_y))
	fenetre.fill("black")
	#x, y = x+w*(1-relative_zoom), y+h*(1-relative_zoom)
	w, h = w*relative_zoom, h*relative_zoom
	#pygame.transform.smoothscale(fenetre, (relative_w, relative_h))
	for ide in objet.keys():
		if (x <= objet[ide]["x"] <= x+w or x <= objet[ide]["x"]+objet[ide]["w"] <= x+w) and (y <= objet[ide]["y"]+objet[ide]["h"] <= y+h or y <= objet[ide]["y"] <= y+h):
			if last_zoom != relative_zoom:
				last_zoom = relative_zoom
				object_resize_image(ide)
			fenetre.blit(objet[ide]["img"], (objet[ide]["x"]-x, objet[ide]["y"]-y))
			#print("in")
	relative_x, relative_y, relative_w, relative_h = x, y, w, h


add_objet(100, 100, 300, 300, "test/2.png")
img = pygame.image.load("test/3.png")
fenetre.blit(img, (0, 0))


run = True
while run:

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					print("hey")
				elif event.key == pygame.K_x:
					print("hey")
					X += 100
					Y += 50
					new = pygame.transform.smoothscale(fenetre, (X, Y))
					fenetre.fill("black")
					fenetre.blit(new, (0, 0))
				elif event.key == pygame.K_a:
					relative_zoom *= 0.75
					update_screen()
				elif event.key == pygame.K_z:
					relative_zoom *= 1.25
					update_screen()
				elif event.key == pygame.K_o:
					update_screen(x=0, y=0)

			if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
				ax = pygame.mouse.get_pos()[0]-last_pos[0]
				ay = pygame.mouse.get_pos()[1]-last_pos[1]
				#print("aX : " + str(ax) + " aY : " + str(ay))
				#update_screen(x=relative_x-ax, y=relative_y-ay)
				fenetre.fill("black")
				fenetre.scroll(dx=ax, dy=ay)
				#print("aX : " + str(relative_x) + " aY : " + str(relative_y) + " W : " + str(relative_w) + " H : " + str(relative_h))


	last_pos = pygame.mouse.get_pos()
	pygame.display.update()

pygame.quit()