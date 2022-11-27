import pygame
import win32api
import win32con
import win32gui

pygame.init()
scrres = pygame.display.Info()
screen = pygame.display.set_mode((scrres.current_w, scrres.current_h),pygame.NOFRAME) # For borderless, use pygame.NOFRAME
px, py, width, hight = 45, 45, 250, 200
fuchsia = (255, 0, 128)  # Transparency color
black = (0, 0, 0)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

def main():
    ndone = True
    while ndone:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ndone = False
            #if event.type == pygame.MOUSEMOTION():
            px, py = pygame.mouse.get_pos()
            
            if px >= scrres.current_w - width:
                px = scrres.current_w - width
            if py >= scrres.current_h - hight:
                py = scrres.current_h - hight
        
        
        screen.fill(black)
        # Transparent Rectangle
        drawtransparentrectangle(px, py)
        pygame.display.update()
        
def drawtransparentrectangle(px, py):
    pygame.draw.rect(screen, fuchsia, pygame.Rect(px-width, py-hight, width, hight))
    
main()