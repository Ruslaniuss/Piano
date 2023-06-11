import play
import pygame
pygame.init()
pygame.mixer.init()
#встаноовлення кольроу фону
play.set_backdrop((100, 233, 77))
#створення текстових спрайтів
text1 = play.new_text(words = "Це - піаніно", x = 0, y = 230)
text2 = play.new_text(words = "Твори музику натискаючи на клафіша", x = 0, y = 180)

piano_on = play.new_circle(color = "black", x = -180, y = -100, radius = 10, border_color = "black", border_width = 3)
piano_txt = play.new_text(words = " Piano", x = -145, y = -100, font_size = 25)

fluite_on = play.new_circle(color = "black", x = 120, y = -100, radius = 10, border_color = "black", border_width = 3)
fluite_txt = play.new_text(words = " Fluite", x = 155, y = -100, font_size = 25)

guitar_on = play.new_circle(color = "black", x = -80, y = -100, radius = 10, border_color = "black", border_width = 3)
guitar_txt = play.new_text(words = " Guitar", x = -45, y = -100, font_size = 25)

violin_on = play.new_circle(color = "black", x = 20, y = -100, radius = 10, border_color = "black", border_width = 3)
violin_txt = play.new_text(words = " Violin", x = 55, y = -100, font_size = 25)

#список клавіш
keys = []
#список звуків
sounds = []

for s in range(4):
    sounds.append([])
for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color="white", width = 40, height = 120, x = key_x, y = 0, border_width = 5, border_color = "black")
    keys.append(key)
    sound = pygame.mixer.Sound("f" + str(i + 1) + ".ogg")
    sounds.append(sound)
    sound = pygame.mixer.Sound("f" + str(i + 1) + ".ogg")
    sounds.append(sound)
    sound = pygame.mixer.Sound("g" + str(i + 1) + ".ogg")
    sounds.append(sound)
    sound = pygame.mixer.Sound("v" + str(i + 1) + ".ogg")
    sounds.append(sound)

get_instrument = 0


@play.when_program_starts#функція для початку програми
def start():
    pass

@piano_on.when_clicked
def piano_on():
    global get_instrument
    get_instrument = 0
    piano_on.color = "black"
    fluite_on.color = "white"
    guitar_on.color = "white"
    violin_on.color = "white"

@fluite_on.when_clicked
def fluite_on():
    global get_instrument
    get_instrument = 1
    piano_on.color = "white"
    fluite_on.color = "black"
    guitar_on.color = "white"
    violin_on.color = "white"

@guitar_on.when_clicked
def guitar_on():
    global get_instrument
    get_instrument = 2
    piano_on.color = "white"
    fluite_on.color = "white"
    guitar_on.color = "black"
    violin_on.color = "white"

@violin_on.when_clicked
def violin_on():
    global get_instrument
    get_instrument = 3
    piano_on.color = "white"
    fluite_on.color = "white"
    guitar_on.color = "white"
    violin_on.color = "black"
#ігровий цикл для перевірки натискання на клавішу
@play.repeat_forever
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = (55, 144, 29)
            await play.timer(0.3)
            keys[j].color = (255, 255, 255)
play.start_program()