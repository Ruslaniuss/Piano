import play
import pygame
pygame.init()
pygame.mixer.init()

play.set_backdrop((100, 233, 77))

text1 = play.new_text(words = "Це - піаніно", x = 0, y = 230)
text2 = play.new_text(words = "Твори музику натискаючи на клафіша", x = 0, y = 180)
keys = []
sounds = []

for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color="white", width = 40, height = 120, x = key_x, y = 0, border_width = 5, border_color = "black")
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + ".ogg")
    sounds.append(sound)
@play.when_program_starts#функція для початку програми
def start():
    pass


@play.repeat_forever#ігровий цикл
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = (55, 144, 29)
            await play.timer(0.3)
            keys[j].color = (130, 265, 109)
play.start_program()