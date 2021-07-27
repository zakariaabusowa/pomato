import pyautogui
import time
import tkinter as tk
import keyboard



def refreash():
    while True:
        pyautogui.hotkey('win','F5')
        pyautogui.sleep(25)


root= tk.Tk() 
   
#canvas1 = tk.Canvas(root, width = 300, height = 300) 
#canvas1.pack()
canvas2 = tk.Canvas(root, width = 300, height = 300) 
canvas2.pack()
      
#button1 = tk.Button (root, text='Exit Application', command=root.destroy) 
button2 = tk.Button (root, text='Run', command=refreash)
#canvas1.create_window(150, 150, window=button1) 
canvas2.create_window(150, 150, window=button2)
   
root.mainloop()

   