import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = BLACK
eraser_on = False

TOOL_PEN = "pen"
TOOL_RECT = "rect"
TOOL_CIRCLE = "circle"
TOOL_ERASER = "eraser"
tool = TOOL_PEN

clock = pygame.time.Clock()

screen.fill(WHITE)

button_font = pygame.font.SysFont(None, 24)
tool_buttons = {
    TOOL_PEN: pygame.Rect(10, 10, 60, 30),
    TOOL_RECT: pygame.Rect(80, 10, 60, 30),
    TOOL_CIRCLE: pygame.Rect(150, 10, 60, 30),
    TOOL_ERASER: pygame.Rect(220, 10, 60, 30),
}
color_buttons = {
    (255, 0, 0): pygame.Rect(300, 10, 30, 30),
    (0, 255, 0): pygame.Rect(340, 10, 30, 30),
    (0, 0, 255): pygame.Rect(380, 10, 30, 30),
    (0, 0, 0): pygame.Rect(420, 10, 30, 30),
}

drawing = False
start_pos = (0, 0)

def draw_ui():
    for t, rect in tool_buttons.items():
        pygame.draw.rect(screen, (200, 200, 200), rect)
        label = button_font.render(t.capitalize(), True, BLACK)
        screen.blit(label, (rect.x + 5, rect.y + 5))
    for c, rect in color_buttons.items():
        pygame.draw.rect(screen, c, rect)

draw_ui()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for t, rect in tool_buttons.items():
                if rect.collidepoint(pos):
                    tool = t
                    eraser_on = (tool == TOOL_ERASER)
                    break
            for c, rect in color_buttons.items():
                if rect.collidepoint(pos):
                    color = c
                    eraser_on = False
                    tool = TOOL_PEN
                    break
            else:
                drawing = True
                start_pos = pos
                if tool == TOOL_PEN or tool == TOOL_ERASER:
                    pygame.draw.circle(screen, WHITE if eraser_on else color, pos, 5)

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if drawing:
                if tool == TOOL_RECT:
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                       abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)
                elif tool == TOOL_CIRCLE:
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius = max(abs(start_pos[0] - end_pos[0]) // 2, abs(start_pos[1] - end_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, radius, 2)
            drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == TOOL_PEN or tool == TOOL_ERASER:
                pygame.draw.circle(screen, WHITE if eraser_on else color, event.pos, 5)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
