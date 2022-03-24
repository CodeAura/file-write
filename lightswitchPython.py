import tkinter as tk
import logging
window = tk.Tk()

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "actions.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()


button = tk.Button(text='Lamp aan', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
def buttonPress(event):
    if button.config('text')[-1] == 'Switch light on':
        button.config(text='Switch light off',bg="white",fg="black")
        window.config(bg="black")  
        print("light is off")
        logger.info("Light is off")
    else:
        button.config(text='Switch light on',bg="white",fg="yellow")
        window.config(bg="Yellow")      
        print("Lamp is aan!")
        logger.info("Light is on")
button.bind('<Button>', buttonPress)

window.mainloop()
