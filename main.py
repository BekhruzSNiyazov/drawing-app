import pygame

pygame.init()
pygame.font.init()

width = 800
height = 650
thick = 7

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Drawing App by Bekhruz S. Niyazov")

icon = pygame.image.load("paintbrush.png")
eraser = pygame.image.load("eraser.png")

pygame.display.set_icon(icon)

win.fill((255, 255, 255))

def redrawWindow(pos):
	global win, colors, color, thick

	pygame.draw.rect(win, (255, 0, 0), (10, height-40, 30, 30))
	pygame.draw.rect(win, (0, 255, 0), (50, height-40, 30, 30))
	pygame.draw.rect(win, (0, 0, 255), (90, height-40, 30, 30))
	pygame.draw.rect(win, (0, 0, 0), (130, height-40, 30, 30))
	win.blit(eraser, (width-50, height-40))

	if color:
		if color == "red":
			pygame.draw.rect(win, (255, 255, 255), (10, height-40, 30, 30), 4)
			pygame.draw.rect(win, (255, 255, 255), (width-50, height-40, 32, 32), 4)
			pygame.draw.rect(win, (0, 255, 0), (50, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 255), (90, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 0), (130, height-40, 30, 30), 2)
		if color == "green":
			pygame.draw.rect(win, (255, 255, 255), (50, height-40, 30, 30), 4)
			pygame.draw.rect(win, (255, 255, 255), (width-50, height-40, 32, 32), 4)
			pygame.draw.rect(win, (255, 0, 0), (10, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 255), (90, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 0), (130, height-40, 30, 30), 2)
		if color == "blue":
			pygame.draw.rect(win, (255, 255, 255), (90, height-40, 30, 30), 4)
			pygame.draw.rect(win, (255, 255, 255), (width-50, height-40, 32, 32), 4)
			pygame.draw.rect(win, (255, 0, 0), (10, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 255, 0), (50, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 0), (130, height-40, 30, 30), 2)
		if color == "black":
			pygame.draw.rect(win, (255, 255, 255), (130, height-40, 30, 30), 4)
			pygame.draw.rect(win, (255, 255, 255), (width-50, height-40, 32, 32), 4)
			pygame.draw.rect(win, (255, 0, 0), (10, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 255, 0), (50, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 255), (90, height-40, 30, 30), 2)
		if color == "eraser":
			pygame.draw.rect(win, (0, 0, 0), (width-50, height-40, 32, 32), 4)
			pygame.draw.rect(win, (0, 0, 0), (130, height-40, 30, 30), 4)	
			pygame.draw.rect(win, (255, 0, 0), (10, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 255, 0), (50, height-40, 30, 30), 2)
			pygame.draw.rect(win, (0, 0, 255), (90, height-40, 30, 30), 2)
	try:
		if pos[1] < height-40:
			if color:
				c = None
				if color == "red": c = (255, 0, 0)
				if color == "green": c = (0, 255, 0)
				if color == "blue": c = (0, 0, 255)
				if color == "black": c = (0, 0, 0)
				if color == "eraser": c = (255, 255, 255)
				x = pos[0]
				y = pos[1]
				if c == (255, 255, 255):
					pygame.draw.circle(win, c, (x, y), 80)
				else:
					pygame.draw.circle(win, c, (x, y), thick)
	except: pass

	pygame.display.update()

colors = {
	"red": {"x0": 10, "y0": 610, "x1": 40, "y1": 640 },
	"green": {"x0": 50, "y0": 610, "x1": 80, "y1": 640 },
	"blue": {"x0": 90, "y0": 610, "x1": 120, "y1": 640 },
	"black": {"x0": 130, "y0": 610, "x1": 160, "y1": 640 },
	"eraser": {"x0": 750, "y0": 610, "x1": 782, "y1": 640}
}

color = None

while True:
	pos = None
	if pygame.event.get(pygame.QUIT):
		break

	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		break

	if pygame.mouse.get_pressed()[0]:
		pos = pygame.mouse.get_pos()
		
		for c in colors:
			if pos[0] >= colors[c]["x0"] and pos[0] <= colors[c]["x1"] and pos[1] >= colors[c]["y0"] and pos[1] <= colors[c]["y1"]:
				color = c

	redrawWindow(pos)

exit()