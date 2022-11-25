
import pyautogui
# X:   41 Y:  250
#X:  642 Y:  670 
#RGB: (255, 219, 195)

'''esse aqui consegue fazer ate 3 acertos por segundo em uma tela com posição ja pre definida.
mas da pra melhorar'''

while True:
   
    sc = pyautogui.screenshot(region=(41, 250, (642-41), (670-250)))
    width, height = sc.size
    
    for x in range(0,width,5):
        achou = 0
        for y in range(0,height,5):
            r,g,b = sc.getpixel((x,y))
            
            if  r == 255 and g == 219 and b == 195:
                achou = 1
                pyautogui.leftClick(41+x,250+y)
                break
        if achou ==1:
            break