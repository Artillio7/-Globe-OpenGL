import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy

def read_texture(filename):
    """
    Lit un fichier image et le convertit en format textID lisible par OpenGL
    """
    # Ouvre l'image et la convertit en données utilisables par OpenGL
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = glGenTextures(1)  # Génère un identifiant unique pour la texture
    glBindTexture(GL_TEXTURE_2D, textID)  # Lie la texture avec son identifiant
    # Configure le mode de stockage et de traitement des textures
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    # Associe les données de l'image à la texture
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return textID  # Retourne l'identifiant de la texture

def main():
    pygame.init()  # Initialise Pygame
    display = (400, 400)  # Définit la taille de la fenêtre
    # Crée une fenêtre avec support OpenGL
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('PyOpenGLobe')  # Définit le titre de la fenêtre
    pygame.key.set_repeat(1, 10)  # Permet la répétition des touches
    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)  # Perspective de la caméra
    glTranslatef(0.0, 0.0, -5)  # Position initiale de la caméra
    lastPosX = 0  # Position précédente de la souris en X
    lastPosY = 0  # Position précédente de la souris en Y
    texture = read_texture('world.jpg')  # Lit et prépare la texture

    while True:  # Boucle principale
        for event in pygame.event.get():  # Traite les événements
            if event.type == pygame.QUIT:  # Quitter proprement
                pygame.quit()
                quit()

            # Rotation avec les flèches du clavier
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(1, 0, -1, 0)
                if event.key == pygame.K_UP:
                    glRotatef(1, -1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(1, 1, 0, 0)

            # Zoom avec la molette de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Molette vers le haut
                    glScaled(1.05, 1.05, 1.05)
                if event.button == 5:  # Molette vers le bas
                    glScaled(0.95, 0.95, 0.95)

            # Rotation avec le clic et glisser de la souris
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                dx = x - lastPosX
                dy = y - lastPosY
                mouseState = pygame.mouse.get_pressed()
                if mouseState[0]:
                    modelView = (GLfloat * 16)()
                    mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)
                    # Combine la rotation des axes X et Y
                    temp = (GLfloat * 3)()
                    temp[0] = modelView[0]*dy + modelView[1]*dx
                    temp[1] = modelView[4]*dy + modelView[5]*dx
                    temp[2] = modelView[8]*dy + modelView[9]*dx
                    norm_xy = math.sqrt(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2])
                    glRotatef(math.sqrt(dx*dx+dy*dy), temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)

                lastPosX = x
                lastPosY = y

        # Crée une sphère et applique la texture
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        qobj = gluNewQuadric()
        gluQuadricTexture(qobj, GL_TRUE)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)
        gluSphere(qobj, 1, 50, 50)  # Dessine la sphère
        gluDeleteQuadric(qobj)
        glDisable(GL_TEXTURE_2D)

        pygame.display.flip()  # Met à jour l'affichage
        pygame.time.wait(10)  # Petite pause pour ne pas surcharger le processeur

main()  # Exécute la fonction principale
