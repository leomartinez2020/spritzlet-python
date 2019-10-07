import tkinter as tk
from extract_text import extract_pickle

counter = 0 
d = extract_pickle()

def counter_msg(msg):
  def count():
    global counter
    word = d[counter]
    word_len = len(word)
    padding = (30 - word_len)//2
    pad = ''.join([" "]*4)
    word = pad + word + pad
    counter += 1
    msg.config(text="{:-^30}".format(word), fg="white", bg="grey", font=('arial', 64, 'bold'), width=900, aspect=300, justify=tk.RIGHT)
    msg.after(120, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
msg = tk.Message(root)
msg.pack()
counter_msg(msg)
button = tk.Button(root, text='Stop', width=80, command=root.destroy)
button.pack()
root.mainloop()
