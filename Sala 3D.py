from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global angulo, fAspect,anguloX,anguloY

anguloX=0; anguloY=0;

class SalaJogos:
    r=0.0;g=0.0; b=0.0;

def chao(): 
    glColor3f(1.0, 1.8, 1.2);
    glPushMatrix();
    glTranslated(0.5, 0.2, 0.3);
    glScaled(3.5, 0.2, 3.0);
    glutSolidCube(1.0);
    glPopMatrix();

def paredeFundo(): 
    glColor3f(1.8, 1.8, 1.4);
    glPushMatrix();
    glTranslated(0.5, 1.10, -1.2);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(3.49, 0.03, 2.0);
    glutSolidCube(1.0);
    glPopMatrix();

def paredeFrente(): 
    glColor3f(1.8, 1.8, 1.4);
    glPushMatrix();
    glTranslated(-1.24, 1.10, 0.3);
    glRotated(90.0, 0.0, 1.0, 0.0);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(3.01, 0.03, 2.0);
    glutSolidCube(1.0);
    glPopMatrix();

def bancada():
    glColor3f(0.60, 0.40, 0.10);

    glPushMatrix();
    glTranslated(0.5, 1.0, -1.03);
    glScaled(1.1, 0.06, 0.18);
    glutSolidCube(2.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.5, 0.5, -1.03);
    glScaled(1.1, 0.06, 0.18);
    glutSolidCube(2.0);
    glPopMatrix();

def PS5():

    glColor3f(1.2,1.2,1.1);

    glPushMatrix();
    glTranslated(1.3, 1.2, -1.03);
    glScaled(0.07, 0.25, 0.17);
    glutSolidCube(2.0);
    glPopMatrix();

    glColor3f(0.0, 0.0, 0.0); 

    glPushMatrix();
    glTranslated(1.3, 1.1, -0.94);
    glScaled(0.05, 0.3, 0.17);
    glutSolidCube(1.0);
    glPopMatrix();
 
    glPushMatrix();
    glTranslated(1.3, 1.33, -1.036);
    glScaled(0.082, 0.3, 0.354);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(1.36, 1.1, -0.94);
    glScaled(0.01, 0.3, 0.17);
    glutSolidCube(1.0);
    glPopMatrix();

def Xbox():
    glColor3f(1.2,1.2,1.1);

    glPushMatrix();
    glTranslated(-0.3, 1.2, -1.03);
    glScaled(0.07, 0.25, 0.17);
    glutSolidCube(2.0);
    glPopMatrix();

    glColor3f(0,0,0)
# Circulo lateral    
    glPushMatrix();
    glTranslated(-0.37, 1.3,- 1.0);
    glRotated(180.0, 1.0, 0.0, 0.0);
    glRotated(90.0, 0.0, 1.0, 0.0);
    glScaled(0.04, 0.04, 0.001);    
    glutSolidSphere(3,10,10);
    glPopMatrix();

    glPushMatrix();
    glTranslated(-0.34, 1.4, -0.86);
    glScaled(0.04, 0.04, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(-0.28, 1.1, -0.86);
    glScaled(0.02, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(-0.28, 1.14, -0.86);
    glScaled(0.01, 0.01, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor(1,1,1);
    glPushMatrix();
    glTranslated(-0.34, 1.4, -0.85);
    glRotated(-45.0, 0.0, 0.0, 1.0);
    glScaled(0.03, 0.005, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(-0.34, 1.4, -0.85);
    glRotated(45.0, 0.0, 0.0, 1.0);
    glScaled(0.03, 0.005, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

def controleVideogame():
#Retangulo base
    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(1.027, 1.1, -1.07);
    glScaled(0.19, 0.06, 0.04);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor3f(0.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(1.02, 1.11, -1.03);
    glScaled(0.12, 0.06, 0.05);
    glutSolidCube(1.0);
    glPopMatrix();

#retangulo direita
    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(1.09, 1.1, -1.01);
    glScaled(0.06, 0.06, 0.10);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor3f(0.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(1.07, 1.11, -1.0);
    glScaled(0.04, 0.061, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

#Botao direita
    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(1.07, 1.14, -1.01);
    glScaled(0.02, 0.01, 0.02);
    glutSolidCube(1.0);
    glPopMatrix();

#Botao direita frente
    glColor3f(0.0, 0.0, 0.0); 
    glPushMatrix();
    glTranslated(1.08, 1.12, -1.08);
    glScaled(0.03, 0.03, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

#retangulo esquerda
    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(0.96, 1.1, -1.01);
    glScaled(0.06, 0.06, 0.10);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor3f(0.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.978, 1.11, -0.99);
    glScaled(0.04, 0.061, 0.07);
    glutSolidCube(1.0);
    glPopMatrix();

#Botao esquerda
    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(0.979, 1.14, -1.01);
    glScaled(0.02, 0.01, 0.02);
    glutSolidCube(1.0);
    glPopMatrix();

#Botao esquerda frente
    glColor3f(0.0, 0.0, 0.0); 
    glPushMatrix();
    glTranslated(0.98, 1.12, -1.08);
    glScaled(0.03, 0.03, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

def controleXbox():
    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(0.1, 1.1, -1.07);
    glScaled(0.19, 0.06, 0.09);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.035, 1.1, -1.0);
    glScaled(0.06, 0.06, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.165, 1.1, -1.0);
    glScaled(0.06, 0.06, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor3f(0,0,0);
    glPushMatrix();
    glTranslated(0.04, 1.128, -1.04);
    glScaled(0.03, 0.01, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.16, 1.128, -1.04);
    glScaled(0.03, 0.01, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.03, 1.128, -1.08);
    glScaled(0.03, 0.01, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.17, 1.128, -1.08);
    glScaled(0.03, 0.01, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.1, 1.128, -1.098);
    glScaled(0.03, 0.01, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

def tv():
    glColor3f(0.0, 0.0, 0.0);

# borda tv
    glPushMatrix();
    glTranslated(0.5, 1.5, -1.19);
    glScaled(1.3, 0.8, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

# fundo da tela
    glColor3f(0.0, 0.0, 142.0);
    glPushMatrix();
    glTranslated(0.5, 1.5, -1.189);
    glScaled(1.2, 0.7, 0.03);
    glutSolidCube(1.0);
    glPopMatrix();

# Escrita P
    glColor3f(35.0, 35.0, 142.0); 
    glPushMatrix();
    glTranslated(0.3, 1.6, -1.1781);
    glScaled(0.1, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.35, 1.553, -1.1781);
    glScaled(0.02, 0.1, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();
    
    glPushMatrix();
    glTranslated(0.3, 1.51, -1.1781);
    glScaled(0.1, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.25, 1.47, -1.1781);
    glScaled(0.02, 0.1, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

# Escrita S
    glPushMatrix();
    glTranslated(0.4, 1.43, -1.1781);
    glScaled(0.1, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();


    glPushMatrix();
    glTranslated(0.46, 1.51, -1.1781);
    glScaled(0.02, 0.17, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.5, 1.6, -1.1781);
    glScaled(0.1, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    #Escrita 5

    glColor3f(35.0, 35.0, 142.0); 
    glPushMatrix();
    glTranslated(0.65, 1.6, -1.1781);
    glScaled(0.12, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.6, 1.553, -1.1781);
    glScaled(0.02, 0.1, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();
    
    glPushMatrix();
    glTranslated(0.65, 1.51, -1.1781);
    glScaled(0.1, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.7, 1.47, -1.1781);
    glScaled(0.02, 0.1, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();


    glPushMatrix();
    glTranslated(0.65, 1.43, -1.1781);
    glScaled(0.12, 0.02, 0.01);
    glutSolidCube(1.0);
    glPopMatrix();

def controleTv():

    glColor3f(0.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.65, 1.1, -1.03);
    glScaled(0.05, 0.02, 0.12);
    glutSolidCube(2.0);
    glPopMatrix();

#Botao Vermelho
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.63, 1.12, -1.1);
    glScaled(0.01, 0.01, 0.01);
    glutSolidCube(2.0);
    glPopMatrix();

#Botao Branco
    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.67, 1.12, -1.1);
    glScaled(0.01, 0.01, 0.01);
    glutSolidCube(2.0);
    glPopMatrix();

# Retangulo 1 branco
    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.65, 1.12, -1.04);
    glScaled(0.03, 0.01, 0.01);
    glutSolidCube(2.0);
    glPopMatrix();

# Retangulo 2 branco
    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.65, 1.12, -1.0);
    glScaled(0.03, 0.01, 0.01);
    glutSolidCube(2.0);
    glPopMatrix();

# Retangulo 3 branco
    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.65, 1.12, -0.96);
    glScaled(0.03, 0.01, 0.01);
    glutSolidCube(2.0);
    glPopMatrix();

def Jogos():
# Jogo 1
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.3, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.3, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 2
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.25, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.25, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 3
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.2, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.2, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 4
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.15, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.15, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 5
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.1, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.1, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 6
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.05, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.05, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 7
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(-0.0, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(-0.0, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 8
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.05, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.05, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 9
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.1, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.1, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 10
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.15, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.15, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 11
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.2, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.2, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 12
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.25, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.25, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 13
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.3, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.3, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 14
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.35, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.35, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 15
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.4, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.4, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 16
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.45, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.45, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 17
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.5, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.5, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 18
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.55, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.55, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 19
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.6, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.6, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 20
    glColor3f(1.0, 0.0, 0.0);
    glPushMatrix();
    glTranslated(0.65, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.65, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 21
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.7, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.7, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 22
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.75, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.75, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 23
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.8, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.8, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 24
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.85, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.85, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 25
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.9, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.9, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 26
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(0.95, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.95, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 27
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(1.0, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(1.0, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 28
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(1.05, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(1.05, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 29
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(1.1, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(1.1, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

# Jogo 30
    glColor3f(0.0, 0.0, 1.0);
    glPushMatrix();
    glTranslated(1.15, 0.71, -1.08);
    glScaled(0.05, 0.6, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(1.15, 0.72, -1.07);
    glScaled(0.06, 0.4, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

def Janela():
    glPushMatrix();
    glColor3f(0.2, 1.15, 1.5);
    glTranslated(-1.24,1.5,0.5);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 1.8, 0.9);
    glutSolidCube(0.8);
    glPopMatrix();

# Divisão do meio da janela vertical
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-1.24, 1.5, 0.5);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.03, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

    # Divisão do meio da janela horizontal
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-1.24, 1.5, 0.5);
    glRotated(180.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.03, 1.45);
    glutSolidCube(1.0);
    glPopMatrix();

# lateral esquerda
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-1.24, 1.5, 1.23);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.03, 0.73);
    glutSolidCube(1.0);
    glPopMatrix();

    # lateral direita
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-1.24, 1.5, -0.23);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.03, 0.73);
    glutSolidCube(1.0);
    glPopMatrix();

    # lateral inferior
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-1.24, 1.15, 0.5);
    glRotated(180.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.03, 1.45);
    glutSolidCube(1.0);
    glPopMatrix();

    # lateral superior
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-1.24, 1.85, 0.50);
    glRotated(180.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.03, 1.45);
    glutSolidCube(1.0);
    glPopMatrix();

def sofa():
    glColor3f(0.60, 0.40, 0.10);

#Pernas traseiras    
    glPushMatrix();
    glTranslated(-1.18, 0.65, 1.75);
    glScaled(0.1, 0.7, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.0, 0.65, 1.75);
    glScaled(0.1, 0.7, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(1.18, 0.65, 1.75);
    glScaled(0.1, 0.7, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(2.2, 0.65, 1.75);
    glScaled(0.1, 0.7, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(-1.18, 0.45, 1.15);
    glScaled(0.1, 0.3, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.0, 0.45, 1.15);
    glScaled(0.1, 0.3, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(1.18, 0.45, 1.15);
    glScaled(0.1, 0.3, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(2.2, 0.45, 1.15);
    glScaled(0.1, 0.3, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

# Pernas frente estendida
    glPushMatrix();
    glTranslated(2.2, 0.45, 0.75);
    glScaled(0.1, 0.3, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();  

    glPushMatrix();
    glTranslated(1.8, 0.45, 0.75);
    glScaled(0.1, 0.3, 0.1);
    glutSolidCube(1.0);
    glPopMatrix(); 

def almofada():
    glPushMatrix();
    glColor3f(1.0, 1.0, 1.0)
    glTranslated(0.24, 0.6, 1.35);
    glScaled(2.93, 0.2, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(1.931, 0.6, 1.15);
    glScaled(0.64, 0.2, 1.1);
    glutSolidCube(1.0);
    glPopMatrix();

    
    #glColor3f(0.0, 0.0, 1.0)
    glPushMatrix();
    glTranslated(0.511, 0.8, 1.65);
    glScaled(3.48, 0.8, 0.2);
    glutSolidCube(1.0);
    glPopMatrix();

def mesaCentro():
    
    glColor3f(0.60, 0.40, 0.10);

#Pernas
    glPushMatrix();
    glTranslated(1.0, 0.4, 0.2);
    glScaled(0.1, 0.4, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.0, 0.4, 0.2);
    glScaled(0.1, 0.4, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(1.0, 0.4, -0.2);
    glScaled(0.1, 0.4, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
    glTranslated(0.0, 0.4, -0.2);
    glScaled(0.1, 0.4, 0.1);
    glutSolidCube(1.0);
    glPopMatrix();

#Tampa mesa
    glPushMatrix();
    glTranslated(0.5, 0.6, 0.0);
    glScaled(1.2, 0.1, 0.5);
    glutSolidCube(1.0);
    glPopMatrix();

    glColor3f(1.2,1.2,1.1);
    glPushMatrix();
    glTranslated(0.5, 0.646, 0.0);
    glScaled(0.7, 0.01, 0.3);
    glutSolidCube(1.0);
    glPopMatrix();

def desenhaPrincipal():
    global anguloX, anguloY,livro
    glRotated(anguloX, 0.0, 1.0, 0.0);
    glRotated(anguloY, 1.0, 0.0, 0.0);
    chao();
    paredeFundo();
    paredeFrente();
    bancada();
    PS5();
    Xbox();
    controleVideogame();
    controleXbox();
    tv();
    controleTv();
    Jogos();
    Janela();
    sofa();
    almofada();
    mesaCentro();
    glFlush();

def iluminacao():
    luzAmbiente = [0.2, 0.2, 0.2, 1]
    luzDifusa = [0.5,0.5,0.5, 1];# "cor"
    luzEspecular = [0.5, 0.5, 0.5, 1];# "brilho"
    posicaoLuz = [0,0,1,0];
    luzAmbiente1 = [0.2, 0.2, 0.2, 1]
    luzDifusa1 = [0.5,0.5,0.5, 1];# "cor"
    luzEspecular1 = [0.5, 0.5, 0.5, 1];# "brilho"
    posicaoLuz1 = [1,0,0,0];
    posicaoLuz2 = [0,1,0,0];
    posicaoLuz3 = [1,1,0,0];	
	
    # Capacidade de brilho do material
    especularidade = [0.5, 0.5, 0.5, 0.0];
    especMaterial = 5;
    glClearColor(0.0, 0.0, 0.0, 1.0);
	
    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH);
    #glShadeModel(GL_FLAT);
	
    # Define a refletância do material
    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade);
	
    #// Define a concentração do brilho
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial);
	
    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente);
	
    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz);
	
	# Define os parâmetros da luz de número 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1);
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1);
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1);
    
	# Define os parâmetros da luz de número 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2);
    
	# Define os parâmetros da luz de número 3
    glLightfv(GL_LIGHT3, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT3, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT3, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT3, GL_POSITION, posicaoLuz3);
    
    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);#Habilita o uso de iluminação
#    glEnable(GL_LIGHT0); # Habilita a luz de número 0
#    glEnable(GL_LIGHT1); # Habilita a luz de número 0
#    glEnable(GL_LIGHT2); # Habilita a luz de número 0
#    glEnable(GL_LIGHT3); # Habilita a luz de número 0
    glEnable(GL_DEPTH_TEST); # Habilita o depth-buffering
    glEnable(GL_NORMALIZE);

def parametrosVisualizacao():
    global fAspect, angulo
	
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    
	# Especifica a projeção perspectiva
    gluPerspective(angulo, fAspect, 0.1, 500);
    #gluPerspective(angulo, 1, 0.5, 50);
    #glOrtho(-1.8, 1.8, -1.8, 2, 0.8, 200.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    # Especifica posição do observador e do alvo
    #gluLookAt(2.00 + anguloX, 1.00 + anguloY, 2.0, 0.0, 0.5, 0.25, 0.0, 1.0, 0.0);
    gluLookAt(5.0, 5.0, 5.0, 0, 1, 0, 0.0, 1.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

def moveCamera(key, x1, y1):
    global anguloX, anguloY
    if (key == GLUT_KEY_UP):
        anguloY -= 1;
    elif (key == GLUT_KEY_DOWN):
        anguloY += 1;
    elif (key == GLUT_KEY_LEFT):
        anguloX -= 1;
    elif (key == GLUT_KEY_RIGHT):
        anguloX += 1;

    parametrosVisualizacao();
    glutPostRedisplay();

def inicializa():
    global angulo
    iluminacao();
    angulo = 45;

def alteraTamanhoJanela(w, h):
    global fAspect
    if (h == 0): h = 1; # Para previnir uma divisão por zero
    glViewport(0, 0, w, h);# Especifica o tamanho da viewport
    fAspect = w/h;
    parametrosVisualizacao();

def gerenciaMouse(button, state, x, y):
    global angulo
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo < 170):
                angulo+=5;
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo > 10):
                angulo-=5;
    parametrosVisualizacao();
    glutPostRedisplay();

def GerenciaTeclado(key, x, y):
    #print (key)
    if (key==b'0'):
        glEnable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
        glDisable(GL_LIGHT3)
    elif(key==b'1'):
        glEnable(GL_LIGHT1)
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT2)
        glDisable(GL_LIGHT3)
    elif(key==b'2'):
        glEnable(GL_LIGHT2)
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT3)
    elif(key==b'3'):
        glEnable(GL_LIGHT3)
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
    elif(key==b'4'):
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
        glDisable(GL_LIGHT3)
    elif(key==b'5'):
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHT2)
        glEnable(GL_LIGHT3)

    
    parametrosVisualizacao();();
    glutPostRedisplay();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(1024, 768);
    glutCreateWindow(b"Sala de Video Game");
    glutDisplayFunc(desenhaPrincipal);
    glutReshapeFunc(alteraTamanhoJanela);
    glutSpecialFunc(moveCamera);
    glutMouseFunc(gerenciaMouse);
    glutKeyboardFunc(GerenciaTeclado);
    inicializa();
    glutMainLoop();

main()