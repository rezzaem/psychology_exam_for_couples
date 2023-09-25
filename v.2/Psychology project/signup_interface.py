from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\turbo\Desktop\Py\Psychology project\develope\psychology_exam_for_couples\v.2\Psychology project\NEW interface\figma_signup\build\assets\frame0")

class SignupInterface:
    def address(self,file):
        return "../Psychology project/bak/signup/"+file

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
        self.image_7= PhotoImage(file=self.address("image_7.png"))
        self.button_image = PhotoImage(file=self.address("button_1.png"))
        self.entry_image_1 = PhotoImage(file=self.address("entry_1.png"))
        self.entry_image_2 = PhotoImage(file=self.address("entry_2.png"))
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
            641.0,
            435.0,
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
            text="Developed with ❤By Rezza.code",
            fill="#BC3800",
            font=("Inter", 12 * -1)
        )

        image_3 = self.canvas.create_image(
            641.0,
            179.0,
            image=self.image_3
        )



        image_7 = self.canvas.create_image(
            327.0,
            560.0,
            image=self.image_7
        )
        #-----------------------------------------------------------------------------------
            
        self.canvas.create_text(
            635.0, # x
            180.0, # y
            text="سلام به برنامه پرسشنامه اولیه خوش آمدید",
            fill="#000000",
            font=("Arial Bold", 24 * -1)
        )

        self.canvas.create_text(
            650.0, #x
            270.0, # y
            text="نام و نام کاربری جدید خود را وارد کنید",
            fill="#000000",
            font=("RobotoRoman Bold", 24 * -1)
        )
        
        self.canvas.create_text(
            770.0, #x
            340.0, # y
            text="نام",
            fill="#000000",
            font=("Arial", 18 * -1)
         )
        
        self.canvas.create_text(
            755, #x
            445.0, #y
            
            text="نام کاربری",
            fill="#000000",
            font=("Arial", 18 * -1)
        )

        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            justify="right"  # Set justify attribute to "right"
        )
        self.entry_2.place(
            x=441.0,
            y=462.0,
            width=370.0,
            height=38.0
        )
        entry_bg_2 = self.canvas.create_image(
            630.5,
            482.0,
            image=self.entry_image_2
        )
        mage_5 = self.canvas.create_image(
            810.0,
            446.0,
            image=self.image_5
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

        self.button = Button(
            image=self.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(self.entry_1.get(),self.entry_2.get()),
            relief="flat"
        )
        self.button.place(
            x=548.0,
            y=561.0,
            width=186.0,
            height=52.0
        )

        entry_bg_1 = self.canvas.create_image(
            630.5,
            380.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            justify="right"  # Set justify attribute to "right"
        )
        self.entry_1.place(
            x=441.0,
            y=360.0,
            width=370.0,
            height=38.0
        )

        image_4 = self.canvas.create_image(
            810.0,
            340.0,
            image=self.image_4
        )

        

        self.window.resizable(False, False)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    interf = SignupInterface()
    interf.run()
