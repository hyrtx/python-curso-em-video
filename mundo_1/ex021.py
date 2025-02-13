'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame
import requests
import io

# URL de um áudio online
url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# Baixa o áudio e carrega em memória
response = requests.get(url)
audio = io.BytesIO(response.content)

# Inicializa pygame e o mixer
pygame.mixer.init()
pygame.init()

# Carrega e toca a música
pygame.mixer.music.load(audio)
pygame.mixer.music.play()

input("Pressione Enter para sair...")