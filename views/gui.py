from pathlib import Path
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, filedialog
from PIL import Image, ImageTk
from operations.neuron import open_csv as start

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\views\assets\frame0")
csv_route = ""
csv_opened = False
eta = ''
learning_rate = ''
iterations = ''


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Neuron Simulation")
window.geometry("500x500")
window.configure(bg = "#E5E5E5")


canvas = Canvas(
    window,
    bg = "#E5E5E5",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    128.0,
    91.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    208.0,
    202.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    449.0,
    204.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    447.0,
    202.0,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    448.5,
    202.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EEEEEE",
    fg="#000716",
    highlightthickness=0,
    font=('Comic Sans MS', 12, 'normal')
)
entry_1.place(
    x=421.0,
    y=192.0,
    width=55.0,
    height=19.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    255.0,
    392.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    250.0,
    387.0,
    image=image_image_6
)

image_correct = Image.open(Path(r"..\views\assets\frame0\correct.png")).resize((27, 27))
image_tk_correct = ImageTk.PhotoImage(image_correct)


image_incorrect = Image.open(Path(r"..\views\assets\frame0\error.png")).resize((27, 27))
image_tk_incorrect = ImageTk.PhotoImage(image_incorrect)


def search_csv():
    global csv_route, csv_opened
    file = filedialog.askopenfilename(filetypes=[("Archivo CSV", "*.csv")])
    if file:
        try:
            csv_route = file
            csv_opened = True
            Label(window, image=image_tk_correct).place(x=445, y=75)
        except Exception as e:
            print(f"Error al cargar: \n{e}")
    else:
        csv_opened = False
        Label(window, image=image_tk_incorrect).place(x=445, y=75)


def do_operations():
    if csv_opened:
        Label(window, image=image_tk_correct).place(x=330, y=305)
        start(csv_route, entry_2.get(), entry_1.get())
    else:
        Label(window, image=image_tk_incorrect).place(x=330, y=258)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=do_operations,
    relief="flat"
)
button_1.place(
    x=175.0,
    y=250.0,
    width=151.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=search_csv,
    relief="flat"
)
button_2.place(
    x=271.0,
    y=71.0,
    width=171.0,
    height=40.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    250.0,
    28.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    161.0,
    144.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    378.0,
    146.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    377.0,
    143.0,
    image=image_image_10
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    380.5,
    143.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EEEEEE",
    fg="#000716",
    highlightthickness=0,
    font=('Comic Sans MS', 12, 'normal')
)
entry_2.place(
    x=340.0,
    y=132.0,
    width=81.0,
    height=21.0
)

if __name__ == '__main__':
    window.resizable(False, False)
    window.mainloop()

