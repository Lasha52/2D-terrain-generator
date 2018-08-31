import pygame 
import numpy as np
import random
import matplotlib.pyplot as plt

WIDTH= 640
HEIGHT = 480
def lerp(arr,danayofi):
	narr = [0]*len(arr)
	step = int(((len(arr)-1)/danayofi))
	j = 0
	
	for k in range(1,len(arr)):
		# for j in range(0,danayofi):
		if(k%step==0 and j!= danayofi-1):
			j+=1
		narr[k] = arr[j*step]+(k-j*step)*(arr[(j+1)*step]-arr[j*step])/step
	return narr
def plot(arr,screen):
	for i in range(0, len(arr)):
		pygame.draw.rect(screen,(222,184,135),(i,700-arr[i],1,arr[i]))
		pygame.display.update()
def addarray(arr1,arr2):
	arr3 =  [0]*len(arr1)
	for i in range(0,len(arr1)):
		arr3[i] = arr1[i]+arr2[i]
	return arr3
def Smultarray (num,arr1):
	arr3 =  [0]*len(arr1)
	for i in range(0,len(arr1)):
		arr3[i] = num*arr1[i]
	return arr3
def PerliNoise(datasize,randrange,octcount):
	seed = [0]*datasize
	noise = [0]*datasize
	octave = [0]*datasize
	# for i in range(0,2000):
	# 	seed[random.randint(0,datasize-1)]+=1
	for i in range(0, len(seed)):
		seed[i] = random.randint(0,randrange)
	for i in range(1,octcount):
		# print (seed[0])
		octave = lerp(seed,i)
		noise = addarray(noise,Smultarray(1/i,octave))
	return noise
noise = PerliNoise(WIDTH,HEIGHT,300)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
windowclose = False
while not windowclose:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			windowclose = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				noise = PerliNoise(WIDTH,300,9)
				screen.fill((0,0,0))
				
	plot(noise,screen)
# noise.remove(0)
# plt.plot(noise)
# plt.show()