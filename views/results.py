from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Label, Toplevel
import matplotlib.pyplot as plt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\views\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class SecondWindow(Toplevel):
    def __init__(self, root, e=None):
        super().__init__(root)

        self.geometry("1161x524")
        self.title("Results")
        self.configure(bg="#E5E5E5")

        self.canvas = Canvas(
            self,
            bg="#E5E5E5",
            height=524,
            width=1161,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            295.0,
            294.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            866.0,
            294.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            580.0,
            35.0,
            image=self.image_image_3
        )

        self.resizable(False, False)

        # First graph
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(e, marker='o', linestyle='-', label='Error', color='green')
        ax.set_xlabel('Épocas')
        ax.set_ylabel('|E|')
        ax.set_title('Evolución de la norma del error ')
        ax.legend()
        fig.savefig("graph1.png")
        self.img_label1 = Label(self)
        self.img_label1.image = PhotoImage(file="graph1.png")
        self.img_label1.config(image=self.img_label1.image)
        self.img_label1.place(x=45, y=90)

'''
        # Second graph
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        ax2.plot(e, marker='o', linestyle='-', label='Graph 2')
        ax2.set_xlabel('Index')
        ax2.set_ylabel('Value')
        ax2.set_title('Another graph with given values')
        ax2.legend()
        fig2.savefig("graph2.png")
        self.img_label2 = Label(self)
        self.img_label2.image = PhotoImage(file="graph2.png")
        self.img_label2.config(image=self.img_label2.image)
        self.img_label2.place(x=619, y=90)
'''
