from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import webbrowser
from sys import exit

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\turbo\Desktop\Py\Psychology project\develope\psychology_exam_for_couples\v.2\Psychology project\NEW interface\figma_signup\build\assets\frame0")

class Logininterface:
    def address(self,file):
        return "../Psychology project/bak/login/"+file

    def on_closing(self):
        exit()

    
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#E2E2E2")



        # Load images
        self.image_1 = PhotoImage(file=self.address("image_1.png"))
        self.image_2 = PhotoImage(file=self.address("image_2.png"))
        self.image_3 = PhotoImage(file=self.address("image_3.png"))
        self.image_4 = PhotoImage(file=self.address("image_4.png"))
        self.image_5 = PhotoImage(file=self.address("image_5.png"))
        self.button_image = PhotoImage(file=self.address("button_1.png"))
        self.entry_image_1 = PhotoImage(file=self.address("entry_1.png"))
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.setup_ui()

    def setup_ui(self):
        # basic items that exist in both mode sign up and login
        self.canvas = Canvas(
            self.window,
            bg="#E2E2E2",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            7.0,
            6.0,
            36.0,
            33.0,
            fill="#7FD1B9",
            outline="")

        image_1 = self.canvas.create_image(
            643.0,
            360.0,
            image=self.image_1
        )

        image_2 = self.canvas.create_image(
        632.0,
        376.0,
            image=self.image_2
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            38.0,
            fill="#7FD1B9",
            outline="")

        self.canvas.create_text(
            42.0,
            690.0,
            anchor="nw",
            text="Developed with ❤By Rezza Emamhasani",
            fill="#BC3800",
            activefill="#E2E2E2",
            font=("Inter", 10 * -1),
            tags="link"
        )
        self.canvas.tag_bind("link", "<Button-1>", self.callback)


        image_3 = self.canvas.create_image(
        632.0,
        183.0,
        image=self.image_3
        )


        self.canvas.create_text(
            635.0, # x
            180.0, # y
            text="سلام به برنامه پرسشنامه  خوش آمدید",
            fill="#000000",
            font=("Arial Bold", 24 * -1)
        )
        self.canvas.create_text(
        635.0, #x
        270.0, # y
        text="نام کاربری خود را وارد کنید",
        fill="#000000",
        font=("Arial bold", 24 * -1)
        )
        self.canvas.create_text(
        735.0,
        335.0,
        anchor="nw",
        text="نام کاربری",
        fill="#000000",
        font=("Arial", 16 * -1)
        )
        self.canvas.create_rectangle(
            7.0,
            9.0,
            27.0,
            29.0,
            fill="#D3A588",
            outline="")

        self.canvas.create_rectangle(
            40.0,
            9.0,
            60.0,
            29.0,
            fill="#7A6563",
            outline="")
        self.canvas.create_rectangle(
            79.0,
            9.0,
            99.0,
            29.0,
            fill="#BC3800",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.address("button_1.png"))
        self.button_1 = Button(
            image=self.button_image,
            borderwidth=2,
            highlightthickness=1,
            command=lambda: print("button_1 clicked"),
            relief="raised"
        )
        self.button_1.place(
            x=534.0,
            y=447.0,
            width=186.0,
            height=52.0
        )


        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            justify="center",
            highlightthickness=2,
            font=("arial",14)
        )
        self.entry_1.place(
            x=441.0,
            y=360.0,
            width=370.0,
            height=38.0
        )
        self.image_image_5 = PhotoImage(
            file=self.address("image_5.png"))
        self.image_5 = self.canvas.create_image(
            810.0,
            340.0,
            image=self.image_image_5
        )
        self.image_image_4 = PhotoImage(
            file=self.address("image_4.png"))
        image_4 = self.canvas.create_image(
            423.0,
            124.0,
            image=self.image_image_4
        )
        
    def callback(self,event):
        webbrowser.open_new("https://www.instagram.com/rezza.code/")

    def run(self):
        self.window.mainloop()
    
if __name__ == "__main__":
    interf = Logininterface()
    interf.run()