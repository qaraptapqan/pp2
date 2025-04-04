import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MUSIC_FOLDER = os.path.dirname(os.path.abspath(__file__))

playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
if not playlist:
    print("No music files found!")
    exit()

current_track = 0
font = pygame.font.Font(None, 36)

def play_music(track=None):
    global current_track
    if track is None:
        file = "tuma-bryunetka.mp3"
        if file not in playlist:
            print(f"File {file} not found in directory!")
            return
    else:
        current_track = track
        file = playlist[current_track]
    
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, file))
    pygame.mixer.music.play()
    print(f"Playing: {file}")

play_music()

running = True
paused = False
while running:
    screen.fill(WHITE)
    text = font.render(f"Playing: {playlist[current_track]}", True, BLACK)
    screen.blit(text, (20, 50))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Resumed")
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
                print("Stopped")
            elif event.key == pygame.K_n:  
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)
            elif event.key == pygame.K_p:  
                current_track = (current_track - 1) % len(playlist)
                play_music(current_track)

pygame.quit()
