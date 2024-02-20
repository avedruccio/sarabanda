import pygame
import pgzrun
from os import listdir
from random import sample
from speech_recognition import Recognizer, Microphone


WIDTH = 1280
HEIGHT = 720

canzonidisp = listdir('music')
canzoni = sample(canzonidisp,14)
print(canzoni)
id_canzone = 0
canzoni_player1 = 0
canzoni_player2 = 0
esatte_player1 = 0
esatte_player2 = 0
chi= (-1000,-1000)
nessuno= (-1000,-1000)
puno= (30,0)
pdue= (718,0)

titolo_canzone1 ='' 
titolo_canzone2 ='' 
testo = 'clicca per iniziare'
testo1 = 'clicca per iniziare'
testo2 = 'clicca per iniziare'
caselle=[]
for n in range(7):
    casella = Actor('neutra')
    casella.pos = 602, 512-n*58
    caselle.append(casella)
for n in range(7):
    casella2 = Actor('neutra')
    casella2.pos = 685, 512-n*58
    caselle.append(casella2)


def convert_speech_to_text():
    recognizer = Recognizer()
    with Microphone() as source:
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language="it-IT")
        return text
def on_mouse_down():
    global id_canzone,testo,testo1,testo2,canzoni_player1,canzoni_player2,esatte_player1,esatte_player2,titolo_canzone1,titolo_canzone2,nessuno,puno,pdue,chi
   

    if music.is_playing(canzoni[id_canzone]):
        sounds.ding.play()
        music.stop()
        chi = nessuno
        testo = convert_speech_to_text()
        
        if testo.lower() == canzoni[id_canzone].rstrip('.mp3'):
            sounds.moseca.play()
            
            if id_canzone % 2 == 0:
                testo1=testo
                caselle[canzoni_player1].image= 'corretta'
                esatte_player1 += 1

            else:
                testo2=testo
                caselle[canzoni_player2+7].image= 'corretta'
                esatte_player2 += 1
        else:
            sounds.no.play()
            if id_canzone % 2 == 0:
                    testo1=testo
                    caselle[canzoni_player1].image= 'errata'
                    titolo_canzone1 = canzoni[id_canzone].rstrip('.mp3')
                    
            else:
                    testo2=testo
                    caselle[canzoni_player2+7].image= 'errata'
                    titolo_canzone2 = canzoni[id_canzone].rstrip('.mp3')
                    
        if id_canzone % 2 == 0:
             canzoni_player1 += 1
        else:
             canzoni_player2 += 1
        id_canzone += 1
        

    else:
        if id_canzone % 2 == 0:
             chi = puno
        else:
             chi = pdue
        testo1= 'ascolta la canzone'
        testo2= 'ascolta la canzone'
        titolo_canzone1=''
        titolo_canzone2=''
        music.play(canzoni[id_canzone])
      
        

def draw():
    screen.surface = pygame.display.set_mode(
        (WIDTH, HEIGHT), pygame.FULLSCREEN)
    
    screen.blit('player', (0,0))
    screen.blit('player', (658,0))
    screen.blit('7x30', (0,0))
    screen.draw.text(testo1, (130,565), fontsize =40)
    screen.draw.text(testo2, (815,565), fontsize =40)
    screen.draw.text(titolo_canzone1, (130,615), fontsize =40)
    screen.draw.text(titolo_canzone2, (815,615), fontsize =40)
    screen.draw.text(str(esatte_player1), (550,565), fontsize =40)
    screen.draw.text(str(esatte_player2), (700,565), fontsize =40)
    screen.blit('giallo', chi)
    

    for casella in caselle:
        casella.draw()




pgzrun.go()


import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: 
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)