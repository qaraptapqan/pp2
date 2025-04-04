import pygame
import math

def main():
    pygame.init()
    
    # Create the main screen and a canvas surface to draw on
    screen = pygame.display.set_mode((640, 480))
    canvas = pygame.Surface(screen.get_size())  # A persistent drawing surface
    canvas.fill((0, 0, 0)) 
    clock = pygame.time.Clock()
    
    # Variables
    radius = 15                # Size of brush/eraser/shapes
    mode = 'blue'             
    tool = 'brush'            
    drawing = False           
    points = []                # Stores brush stroke points
    start_pos = (0, 0)        # Starting position for shapes
    
    while True:
        # Check if Ctrl or Alt are being held (for shortcuts like Ctrl+W)
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        # Event loop
        for event in pygame.event.get():
            # Exit conditions
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_w and ctrl_held) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and alt_held) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

            # Tool / Color selection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_l:
                    tool = 'rectangle'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'brush'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key == pygame.K_t:
                    tool = 'right_triangle'
                elif event.key == pygame.K_y:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    tool = 'rhombus'

            # Mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    drawing = True
                    start_pos = event.pos  # Store start position for shapes
                    if tool == 'brush':
                        points.append(event.pos)
                elif event.button == 3:  # Right click to reduce brush size
                    radius = max(1, radius - 1)

            # Mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    color = getColor(mode)
                    
                    if tool == 'circle':
                        # Draw a filled circle at the release point
                        pygame.draw.circle(canvas, color, end_pos, radius)
                    elif tool == 'rectangle':
                        # Draw a rectangle from start_pos to current mouse position
                        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        pygame.draw.rect(canvas, color, rect)
                    elif tool == 'square':
                        # Draw a square (equal width and height)
                        size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        # Adjust position to maintain square when dragging in any direction
                        x = start_pos[0] if end_pos[0] > start_pos[0] else start_pos[0] - size
                        y = start_pos[1] if end_pos[1] > start_pos[1] else start_pos[1] - size
                        pygame.draw.rect(canvas, color, (x, y, size, size))
                    elif tool == 'right_triangle':
                        # Draw a right triangle with right angle at start position
                        points = [
                            start_pos,
                            (start_pos[0], end_pos[1]),
                            end_pos
                        ]
                        pygame.draw.polygon(canvas, color, points)
                    elif tool == 'equilateral_triangle':
                        # Draw an equilateral triangle
                        width = end_pos[0] - start_pos[0]
                        height = int(width * math.sqrt(3) / 2)
                        points = [
                            start_pos,
                            (start_pos[0] + width, start_pos[1]),
                            (start_pos[0] + width // 2, start_pos[1] - height)
                        ]
                        pygame.draw.polygon(canvas, color, points)
                    elif tool == 'rhombus':
                        # Draw a rhombus (diamond shape)
                        center_x = (start_pos[0] + end_pos[0]) // 2
                        center_y = (start_pos[1] + end_pos[1]) // 2
                        width = abs(end_pos[0] - start_pos[0]) // 2
                        height = abs(end_pos[1] - start_pos[1]) // 2
                        points = [
                            (center_x, center_y - height),  # Top
                            (center_x + width, center_y),    # Right
                            (center_x, center_y + height),   # Bottom
                            (center_x - width, center_y)     # Left
                        ]
                        pygame.draw.polygon(canvas, color, points)

            # Mouse is moving while a button is held
            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                if tool == 'brush':
                    # Add current position to points list for smooth drawing
                    points.append(position)
                    if len(points) >= 2:
                        # Draw a smooth line between last two points
                        drawLineBetween(canvas, len(points)-2, points[-2], points[-1], radius, mode)
                elif tool == 'eraser':
                    # Draw a black circle (eraser effect)
                    pygame.draw.circle(canvas, (0, 0, 0), position, radius)

        # Display the canvas
        screen.blit(canvas, (0, 0))
        
        # Display current tool and color in the corner
        font = pygame.font.SysFont('Arial', 16)
        tool_text = font.render(f"Tool: {tool} | Color: {mode}", True, (255, 255, 255))
        screen.blit(tool_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

# Draw a gradient-style line between two points using circles
def drawLineBetween(surface, index, start, end, width, color_mode):
    color = getColor(color_mode)  # Используем текущий цвет без градиента
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)
# Return the RGB color based on the mode
def getColor(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)  # Default white

if __name__ == "__main__":
    main()
