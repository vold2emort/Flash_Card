from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash_Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right)
right_button.config(highlightthickness=0)
right_button.grid(row=2, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong)
wrong_button.config(highlightthickness=0)
wrong_button.grid(row=2, column=1)

window.mainloop()
