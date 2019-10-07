import tkinter as tk

def start():
    root = tk.Tk()
    logo = tk.PhotoImage(file="scarlett.gif")
    w1 = tk.Label(root, image=logo).pack(side="right")
    texto = "Scarlett is mine!!!"
    w2 = tk.Label(root, justify=tk.LEFT, padx=10,text=texto).pack(side="left")
    root.mainloop()

start()
