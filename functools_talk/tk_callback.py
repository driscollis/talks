import tkinter

from functools import partial

def btn_event(label):
    print(f"You pressed the {label} button")


def main():
    root = tkinter.Tk()
    root.title("Partial Callbacks")
    root.geometry("200x200")
    evt_handler = lambda: btn_event("Press me")
    btn = tkinter.Button(root, text="Press me", command=evt_handler)
    btn.pack()
    root.mainloop()
    
main()
    