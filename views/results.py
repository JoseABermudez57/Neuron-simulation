import os
import random
from pathlib import Path
from tkinter import Canvas, PhotoImage, Label, Toplevel
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\views\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class SecondWindow(Toplevel):
    def __init__(self, root, e=None, w=None):
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

        output_folder = 'graphics/'
        os.makedirs(output_folder, exist_ok=True)

        # First graph
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(e, marker='o', linestyle='-', label='Error', color='green')
        ax.set_xlabel('Épocas')
        ax.set_ylabel('|E|')
        ax.set_title('Evolución de la norma del error ')
        ax.legend()
        filename = os.path.join(output_folder, 'norm_e_evolution.png')
        fig.savefig(filename)
        self.img_label1 = Label(self)
        self.img_label1.image = PhotoImage(file=filename)
        self.img_label1.config(image=self.img_label1.image)
        self.img_label1.place(x=45, y=90)

        w = np.squeeze(np.array(w))

        # Second graph
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        ax2.spines['left'].set_position('zero')
        ax2.spines['left'].set_color('gray')
        ax2.spines['bottom'].set_position('zero')
        ax2.spines['bottom'].set_color('gray')
        marks = ['s', 'o', '^']
        for i in range(w.shape[1]):
            ax2.plot(range(w.shape[0]), w[:, i], label=f'Peso {i}', marker=random.choice(marks), linestyle='-')
        ax2.set_xlim((0 - 1), (len(w) + 1))
        if np.min(w) >= 0:
            ax2.set_ylim((0 - 1), (np.max(w) + 1))
        else:
            ax2.set_ylim((np.min(w) - 1), (np.max(w) + 1))
        ax2.set_xlabel('Épocas')
        ax2.set_ylabel('Pesos (w)')
        ax2.set_title('Evolución de los pesos')
        ax2.legend()
        filename2 = os.path.join(output_folder, 'weight_evolution.png')
        fig2.savefig(filename2)
        self.img_label2 = Label(self)
        self.img_label2.image = PhotoImage(file=filename2)
        self.img_label2.config(image=self.img_label2.image)
        self.img_label2.place(x=619, y=90)
