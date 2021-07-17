import random
import pygame


pygame.font.init()

#VAR
screen_w, screen_h = 1200, 600
relative_x, relative_y, relative_w, relative_h = 0, 0, screen_w, screen_h
objet = {}



fenetre = pygame.display.set_mode((screen_w, screen_h))

img = pygame.image.load("test/2.png")
img2 = pygame.image.load("test/1.jpg")



def add_objet(x, y, w, h, path):
	ide = len(objet)
	objet[ide] = {"x": x, "y": y, "w": w, "h": h}
	img = pygame.image.load(path)
	objet[ide]["img"] = pygame.transform.scale(img, (w, h))


def update_screen(x, y, w, h):
	global relative_x, relative_y
	print("X : " + str(relative_x) + " Y : " + str(relative_y))
	relative_x, relative_y = x, y
	fenetre.fill("black")
	for a in objet.keys():
		if x <= objet[a]["x"]+objet[a]["w"] <= x+w and y <= objet[a]["y"]+objet[a]["h"] <= y+h:
			fenetre.blit(objet[a]["img"], (objet[a]["x"]-x, objet[a]["y"]-y))


add_objet(100, 100, 200, 100, "test/2.png")
add_objet(700, 500, 5, 5, "test/1.jpg")


last_pos = 0, 0
run = True
while run:

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					print("hey")
					X += -100
					Y += -50
					new = pygame.transform.smoothscale(fenetre, (X, Y))
					fenetre.fill("black")
					fenetre.blit(new, (0, 0))
				elif event.key == pygame.K_x:
					print("hey")
					X += 100
					Y += 50
					new = pygame.transform.smoothscale(fenetre, (X, Y))
					fenetre.fill("black")
					fenetre.blit(new, (0, 0))
				elif event.key == pygame.K_a:
					update_screen(100, 100, 200)

			if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
				ax = pygame.mouse.get_pos()[0]-last_pos[0]
				ay = pygame.mouse.get_pos()[1]-last_pos[1]
				print("aX : " + str(ax) + " aY : " + str(ay))
				update_screen(relative_x-ax, relative_y-ay, relative_w, relative_h)


	last_pos = pygame.mouse.get_pos()
	pygame.display.update()

pygame.quit()