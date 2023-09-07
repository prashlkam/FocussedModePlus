import pygame
import win32api
import win32con
import win32gui

pygame.init()
scrres = pygame.display.Info()
screen = pygame.display.set_mode((scrres.current_w, scrres.current_h),pygame.NOFRAME) # For borderless, use pygame.NOFRAME
px, py, width, hight, horstepval, vertstepval = 45, 45, 250, 150, 150, 100
fuchsia = (255, 0, 128)  # Transparency color
black = (0, 0, 0)
white = (255, 255, 255)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

# Set always on top window
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)

def main():
    ndone = True
    width, hight = 250, 150
    px, py = 50, 50
    lx, ly = 0, 0
    horstepval, vertstepval = 150, 100
    while ndone:
        
        #px, py = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if lx == px and ly == py:
                px, py = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                ndone = False
                pygame.quit()
                #Quit()
            
            if event.type == pygame.MOUSEMOTION:    
                px, py = pygame.mouse.get_pos()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    ndone = False
                
                if event.key == pygame.K_LEFT:
                    if px >= 0:
                        px -= horstepval
                    else:
                        px = 0
                if event.key == pygame.K_RIGHT:
                    if px <= scrres.current_w:
                        px += horstepval
                    else:
                        px = scrres.current_w
                if event.key == pygame.K_UP:
                    if py >= 0:
                        py -= vertstepval
                    else:
                        py = 0
                if event.key == pygame.K_DOWN:
                    if py <= scrres.current_h:
                        py += vertstepval
                    else:
                        py = scrres.current_h
                
                if event.key == pygame.K_m:
                    pygame.display.iconify()
                # if event.key == pygame.K_x:
                #     pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                                                
                # for increasing / decreasing
                # hight of visible area 
                if event.key == pygame.K_MINUS:
                    if hight > 0 + vertstepval:
                        hight -= vertstepval
                    else:
                        hight = 150
                if event.key == pygame.K_EQUALS:
                    if hight < scrres.current_h - vertstepval:
                        hight += vertstepval
                    else:
                        hight = 5
                

                # for increasing / decreasing
                # vertical speed
                if event.key == pygame.K_UNDERSCORE:
                    if vertstepval > 25:
                        vertstepval -= 25
                    else:
                        vertstepval = hight
                if event.key == pygame.K_PLUS:
                    if horstepval < hight:
                        horstepval += 25
                    else:
                        horstepval = 25
                
                # for increasing / decreasing
                # width of visible area 
                if event.key == pygame.K_COMMA:
                    if width > 0 + horstepval:
                        width -= horstepval
                    else:
                        width = 250
                if event.key == pygame.K_PERIOD:
                    if width < scrres.current_w - horstepval:
                        width += horstepval
                    else:
                        width = 5
                
                # for increasing / decreasing
                # horizontal speed
                if event.key == pygame.K_LESS:
                    if vertstepval > 20:
                        vertstepval -= 20
                    else:
                        vertstepval = width 
                if event.key == pygame.K_GREATER:
                    if vertstepval < width:
                        vertstepval += 20
                    else:
                        vertstepval = 20
                lx, ly = pygame.mouse.get_pos()
            
                                
        screen.fill(black)
        # Transparent Rectangle
        drawtransparentrectangle(px, py, width, hight)
        pygame.display.update()
        
def drawtransparentrectangle(px, py, width, hight):
    pygame.draw.rect(screen, white, pygame.Rect((px-int(width/2)-2), (py-int(hight/2))-2, width+4, hight+4))
    pygame.draw.rect(screen, fuchsia, pygame.Rect(px-int(width/2), py-int(hight/2), width, hight))
    
main()
