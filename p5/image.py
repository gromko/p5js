# IMAGE
def loadPixels(image):
    return pygame.PixelArray(image)

def updatePixels(pixels):
    pixels.close()
    
def loadImage(path):
    return pygame.image.load(path)

def image(img, x, y):
    if (backgroundSurf):
        backgroundSurf.blit(img, (x, y))