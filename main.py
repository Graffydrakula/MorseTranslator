from tkinter import Label, Tk, PhotoImage, Entry, IntVar, Radiobutton, Button, END
from decoder import Decoder
import pyperclip

class MorseGui:
    def __init__(self, tk_window):

        #--------- Set up Window ---------#
        self.tk_window = tk_window
        self.decoder = Decoder()
        self.tk_window.title("Morse Code Translator")
        self.tk_window.minsize(width=620, height=500)
        self.tk_window.config(padx=20, pady=20)

        # --------- Input Fields ---------#

        self.encode_field = Entry(width=40)
        self.encode_field.grid(row=3, column=0)

        self.decode_field = Entry(width=40)
        self.decode_field.grid(row=3, column=4)

        # --------- Labels ---------#

        self.name = Label(text="Morse Code Translator", font=("Ariel", 22, "bold"))
        self.name.grid(row=0, column=1, columnspan=3)

        self.img = PhotoImage(file="morse.gif", width=200, height=150)
        self.image = Label(image=self.img, bd=5, bg="black")
        self.image.grid(row=1, column=1, columnspan=3)

        self.encode_label = Label(text="English 🡺 Morse", font=("Ariel", 15, "bold"))
        self.encode_label.grid(row=2, column=0)

        self.decode_label = Label(text="English 🡸 Morse", font=("Ariel", 15, "bold"))
        self.decode_label.grid(row=2, column=4)

        self.mode_label = Label(text="Choose Your Mode", font=("Ariel", 12, "bold"))
        self.mode_label.grid(row=4, column=2)

        self.output = Label(text="", font=("Ariel", 15, "bold"))
        self.output.config(bg="white", width=30, height=5, relief="solid")
        self.output.grid(row=5, column=1, columnspan=3)

        # --------- Buttons ---------#

        self.translate_button = Button(text="Translate", command=self.translation)
        self.translate_button.config(font=("Ariel", 12, "bold"), cursor="hand2", width=11, height=1,
                                activebackground="black",
                                activeforeground="white", background="gray")
        self.translate_button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

        self.copy_button = Button(text="copy", command=self.copy)
        self.copy_button.config(activebackground="gray", background="white", cursor="hand2")
        self.copy_button.grid(row=6, column=2, padx=10, pady=10)

        self.clear_encode = Button(text="clear", command=self.encode_delete)
        self.clear_encode.config(activebackground="gray", background="white", cursor="hand2")
        self.clear_encode.grid(row=4, column=0, padx=10, pady=10)

        self.clear_decode = Button(text="clear", command=self.decode_delete)
        self.clear_decode.config(activebackground="gray", background="white", cursor="hand2")
        self.clear_decode.grid(row=4, column=4, padx=10, pady=10)

        self.paste_encode = Button(text="paste", command=self.paste)
        self.paste_encode.config(activebackground="gray", background="white", cursor="hand2")
        self.paste_encode.grid(row=3, column=1, padx=10, pady=10)

        self.paste_decode = Button(text="paste", command=self.paste)
        self.paste_decode.config(activebackground="gray", background="white", cursor="hand2")
        self.paste_decode.grid(row=3, column=3, padx=10, pady=10)

        # --------- Radiobuttons ---------#

        self.mode = IntVar()

        self.encode_radio = Radiobutton(text="To Morse", value=0, variable=self.mode, command=self.choose_mode)
        self.encode_radio.config(cursor="hand2", indicatoron=False, width=10, activebackground="black",
                            activeforeground="white", selectcolor="grey", font=("Ariel", 10, "bold"))
        self.encode_radio.grid(row=4, column=1)

        self.decode_radio = Radiobutton(text="To English", value=1, variable=self.mode, command=self.choose_mode)
        self.decode_radio.config(cursor="hand2", indicatoron=False, width=10, activebackground="black",
                            activeforeground="white", selectcolor="grey", font=("Ariel", 10, "bold"))
        self.decode_radio.grid(row=4, column=3)

        self.encode_radio.select()
        self.choose_mode()

        # --------- Variables ---------#
        self.text_to_encode = self.encode_field.get()
        self.text_to_decode = self.decode_field.get()
        self.output_text = self.output.cget("text")

    # --------- Scripts ---------#

    def encode_delete(self):
        self.encode_field.delete(0, last=END)

    def decode_delete(self):
        self.decode_field.delete(0, last=END)

    # When changing mode the program clears input fields, disable input to another mode and set focus to current mode
    def choose_mode(self):
        if self.mode.get() == 0:
            self.decode_delete()
            self.decode_field.config(state="disabled", justify="center")
            self.encode_field.config(state="normal", justify="left")
            self.encode_delete()
            self.encode_field.focus()
        elif self.mode.get() == 1:
            self.encode_delete()
            self.encode_field.config(state="disabled", justify="center")
            self.decode_field.config(state="normal", justify="left")
            self.decode_delete()
            self.decode_field.focus()

    def paste(self):
        if self.mode.get() == 0:
            self.encode_field.insert(END, string=pyperclip.paste())
            self.encode_field.focus()
        elif self.mode.get() == 1:
            self.decode_field.insert(END, string=pyperclip.paste())
            self.decode_field.focus()

    def copy(self):
        pyperclip.copy(self.output_text)

    def translation(self):
        if self.mode.get() == 0:
            self.output.config(text=self.decoder.encode(message=self.text_to_encode))

        elif self.mode.get() == 1:
            self.output.config(text=self.decoder.decode(message=self.text_to_decode))

# --------- Run ---------#

tkinter_window = Tk()
window = MorseGui(tk_window=tkinter_window)

tkinter_window.mainloop()