import tkinter as tk


def encrypt():
    text = ent_words.get()
    shift = int(ent_shift.get())
    if text.isalpha():
        result = ""
        for i in range(0, len(text)):
            if (text[i].islower()):
                if ((ord(text[i])+shift) > 122):
                    result +=chr(ord(text[i])+shift -26)
                else:
                    result +=chr(ord(text[i])+shift)
            elif (text[i].isupper()):
                if ((ord(text[i])+shift) > 90):
                    result +=chr(ord(text[i])+shift -26)
                else:
                    result +=chr(ord(text[i])+shift)
        lbl_result["text"] = "Encrypted->" , result
    else:
        lbl_result["text"] = "Invalid input"
        
    return result

window = tk.Tk()
window.title("Ceaser Cipher Encryption")
window.resizable(width=False, height=False)


frm_entry = tk.Frame(master = window,
                     relief = tk.RAISED,
                     borderwidth=10)


lbl_result = tk.Label(master = window)
ent_words = tk.Entry(master = frm_entry, width=20)
lbl_words = tk.Label(
    master = frm_entry,
    text=" \nEnter words to be encrypted\n"
    )
ent_words.grid(row = 0, column = 1, sticky = "w")
lbl_words.grid(row= 0, column = 0, sticky="e")

ent_shift = tk.Entry(master = frm_entry, width=20)
lbl_shift = tk.Label(
    master = frm_entry,
    text=" \nEnter shift\n"
    )
ent_words.grid(row = 0, column = 1, sticky = "w")
lbl_words.grid(row= 0, column = 0, sticky="e")
ent_shift.grid(row = 1, column = 1, sticky = "w")
lbl_shift.grid(row= 1, column = 0, sticky="e")

btn_convert = tk.Button(
    master = window,
    text ="Encrypt",
    command = encrypt
    )
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=2, column=0, pady=10)
lbl_result.grid(row=3, column=0, padx=10)


window.mainloop()
