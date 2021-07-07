import tkinter as tk
import pyautogui
import time

window = tk.Tk()
window.title("Spammer")
spamming = False

entry = tk.Entry(fg="black", bg="white", width=40)
label = tk.Label(text="Text that will be spammer")

texta = tk.Label(text="how often do you want to spam?")
often = tk.Entry(fg="black", bg="white", width=40)


def spamm():
    spammer = True
    if(spammer == True):
        time.sleep(4)
        if(entry != ""): 
            spammtext = entry.get()
            howoften = int(often.get())
            if(howoften != ""):
                for i in range (0, howoften):
                    pyautogui.typewrite(spammtext)                 
                    pyautogui.press("enter")
                    time.sleep(0.6)

        else: 
            tk.Label(text="exiting...")
            spammer = False
            window.destroy()
        window.destroy()

def destroy():
    time.sleep(1)
    window.destroy()


button = tk.Button(
    text="Start Spamming",
    width=15,
    height=2,
    bg="white",
    fg="black",
    command=spamm
)
exiting = tk.Button(
    text="exit...",
    width=5,
    height=2,
    bg="white",
    fg="red",
    command=destroy
)



label.pack()
entry.pack()
texta.pack()
often.pack()
button.pack()
exiting.pack()
window.mainloop()
