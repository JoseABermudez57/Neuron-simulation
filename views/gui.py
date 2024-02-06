from pathlib import Path
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, filedialog, Frame
from PIL import Image, ImageTk
from operations.neuron import open_csv as start
from results import SecondWindow

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
window.geometry("500x550")
window.configure(bg="#E5E5E5")

canvas = Canvas(
    window,
    bg="#E5E5E5",
    height=550,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
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
    147.0,
    201.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    209.0,
    255.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    328.0,
    202.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    453.0,
    255.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    326.0,
    200.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    451.0,
    253.0,
    image=image_image_7
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    327.5,
    200.5,
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
    x=300.0,
    y=190.0,
    width=55.0,
    height=19.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    452.5,
    253.5,
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
    x=425.0,
    y=243.0,
    width=55.0,
    height=19.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    253.0,
    451.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    248.0,
    447.0,
    image=image_image_9
)

image_correct = Image.open(Path(r"..\views\assets\frame0\correct.png")).resize((27, 27))
image_tk_correct = ImageTk.PhotoImage(image_correct)

image_incorrect = Image.open(Path(r"..\views\assets\frame0\error.png")).resize((27, 27))
image_tk_incorrect = ImageTk.PhotoImage(image_incorrect)

image_results = Image.open(Path(r"..\views\assets\frame0\results_template.png")).resize((315, 105))
image_tk_results = ImageTk.PhotoImage(image_results)


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
        eta_value = entry_3.get() if entry_3.get() != '' else 0
        epochs = entry_2.get() if entry_2.get() != '' else 0
        if (float(eta_value) > 0) and (float(epochs) > 0):
            Label(window, image=image_tk_correct).place(x=330, y=305)
            tolerance = entry_1.get() if entry_1.get() != '' else False
            w, e = start(csv_route, entry_1.get(), entry_3.get(), entry_2.get())
            w = [[round(value, 4) for value in sub_w[0]] for sub_w in w]
            Label(window, image=image_tk_results).place(x=86, y=392)
            Label(window, text=f"Peso inicial: {w[0]}", font=('Comic Sans MS', 9, 'bold')).place(x=92, y=394)
            Label(window, text=f"Peso final: \n{w[-1]}", font=('Comic Sans MS', 9, 'bold')).place(x=96, y=414)
            Label(window, text=eta_value, font=('Comic Sans MS', 12, 'normal')).place(x=105, y=470)
            Label(window, text=epochs, font=('Comic Sans MS', 12, 'normal')).place(x=198, y=470)
            Label(window, text=tolerance, font=('Comic Sans MS', 12, 'normal')).place(x=315, y=470)
            SecondWindow(window, e, w)
        else:
            Label(window, image=image_tk_incorrect).place(x=330, y=310)
    else:
        Label(window, image=image_tk_incorrect).place(x=330, y=310)


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
    y=302.0,
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

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    250.0,
    28.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    161.0,
    144.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    378.0,
    146.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    377.0,
    143.0,
    image=image_image_13
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    380.5,
    143.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EEEEEE",
    fg="#000716",
    highlightthickness=0,
    font=('Comic Sans MS', 12, 'normal')
)
entry_3.place(
    x=340.0,
    y=132.0,
    width=81.0,
    height=21.0
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    244.0,
    400.0,
    image=image_image_14
)

if __name__ == '__main__':
    window.resizable(False, False)
    window.mainloop()
