import sys
import tkinter as tk
from extract_text import extract_pickle

counter = 0
def get_data(filename):
    return extract_pickle(filename)

#d = get_data("www.geekwire.com")
if len(sys.argv) > 1:
    d = get_data(sys.argv[1])

def counter_msg(msg):
  def count():
    global counter
    word = d[counter]
    word_len = len(word)
    padding = (30 - word_len)//2
    pad = ''.join([" "]*4)
    word = pad + word + pad
    counter += 1
    msg.config(text="{:-^30}".format(word), fg="black", bg="grey", font=('arial', 64, 'bold'), width=900, aspect=300, justify=tk.RIGHT)
    msg.after(220, count)
  count()
 
 
root = tk.Tk()
root.geometry("1300x700")
root.configure(background="grey")
root.title("Counting Seconds")

msg = tk.Message(root)
msg.pack(pady=300)
counter_msg(msg)
#button = tk.Button(root, text='Stop', width=80, command=root.destroy)
#button.pack()
root.mainloop()
