import random
import pygame


pygame.font.init()

#VAR
X,Y = 1200, 600
objet = {}



fenetre = pygame.display.set_mode((X, Y))

img = pygame.image.load("test/2.png")
img2 = pygame.image.load("test/1.jpg")



def add_objet(x, y, w, h, path):
	ide = len(objet)
	objet[ide] = {"x": x, "y": y, "w": w, "h": h}
	objet[ide]["img"] = pygame.image.load(path)


def update_screen(x, y, size):
	for a in objet.keys():
		if x <= objet[a]["x"]+objet[a]["w"] < x+size and y <= objet[a]["y"] <= y+size:
			fenetre.blit(objet[a]["img"], (objet[a]["x"]-x, 0))

add_objet(100, 100, 50, 50, "test/2.png")
add_objet(700, 500, 5, 5, "test/1.jpg")



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
					update_screen(125, 50, 300)
	pygame.display.update()

pygame.quit()