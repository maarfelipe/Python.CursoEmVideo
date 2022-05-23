"""Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame                                  #Para instalar um módulo, basta escrever o nome dele após um comando de importação
pygame.init()                                  #Comando do módulo para que ele inicie
pygame.mixer.music.load('ex021.mp3')           #Comando para carregar o áudio mp3 escolhido através de seu nome
pygame.event.music.play()                      #Comando para começar a tocar
pygame.event.wait()                            #O código vai esperar a música tocar e depois para
"""